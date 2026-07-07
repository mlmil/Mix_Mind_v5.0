"""Minimal, dependency-free OSC client for Behringer X-Air mixers.

X-Air specifics (why we don't use a generic OSC library):
- The mixer answers a bare address (no args) with the current value at
  the same address -> request/reply over one UDP socket (port 10024).
- Replies to /node and /xinfo use loose addresses ('node', '/xinfo').
- /meters delivers OSC blobs of little-endian int16 levels (1/256 dB).
- OSC bundles are NOT supported by the mixer.
"""
from __future__ import annotations

import socket
import struct
import threading
import time
from dataclasses import dataclass, field
from typing import Any

XAIR_PORT = 10024


# --------------------------------------------------------------------------
# OSC wire codec
# --------------------------------------------------------------------------

def _pad(b: bytes) -> bytes:
    return b + b"\x00" * ((4 - len(b) % 4) % 4)


def encode(address: str, *args: Any) -> bytes:
    msg = _pad(address.encode() + b"\x00")
    tags = ","
    payload = b""
    for a in args:
        if isinstance(a, bool):
            a = int(a)
        if isinstance(a, int):
            tags += "i"
            payload += struct.pack(">i", a)
        elif isinstance(a, float):
            tags += "f"
            payload += struct.pack(">f", a)
        elif isinstance(a, str):
            tags += "s"
            payload += _pad(a.encode() + b"\x00")
        elif isinstance(a, (bytes, bytearray)):
            tags += "b"
            payload += struct.pack(">i", len(a)) + _pad(bytes(a))
        else:
            raise TypeError(f"Unsupported OSC arg type: {type(a)}")
    return msg + _pad(tags.encode() + b"\x00") + payload


def decode(data: bytes) -> tuple[str, list[Any]]:
    def read_str(buf: bytes, off: int) -> tuple[str, int]:
        end = buf.index(b"\x00", off)
        s = buf[off:end].decode(errors="replace")
        return s, (end + 4) & ~3

    address, off = read_str(data, 0)
    args: list[Any] = []
    if off < len(data) and data[off:off + 1] == b",":
        tags, off = read_str(data, off)
        for t in tags[1:]:
            if t == "i":
                args.append(struct.unpack(">i", data[off:off + 4])[0]); off += 4
            elif t == "f":
                args.append(struct.unpack(">f", data[off:off + 4])[0]); off += 4
            elif t == "s":
                s, off = read_str(data, off); args.append(s)
            elif t == "b":
                n = struct.unpack(">i", data[off:off + 4])[0]; off += 4
                args.append(data[off:off + n]); off += (n + 3) & ~3
    return address, args


def decode_meter_blob(blob: bytes) -> list[float]:
    """Meter blob -> list of dB floats. int32 count + little-endian int16s (1/256 dB)."""
    if len(blob) < 4:
        return []
    count = struct.unpack("<i", blob[:4])[0]
    vals = struct.unpack(f"<{count}h", blob[4:4 + count * 2])
    return [v / 256.0 for v in vals]


# --------------------------------------------------------------------------
# Client
# --------------------------------------------------------------------------

@dataclass
class XAirClient:
    host: str
    port: int = XAIR_PORT
    timeout: float = 1.5
    retries: int = 2

    _sock: socket.socket | None = None
    _lock: threading.Lock = field(default_factory=threading.Lock)
    _rx_thread: threading.Thread | None = None
    _running: bool = False
    # address -> (event, [reply]) for pending requests
    _pending: dict[str, tuple[threading.Event, list]] = field(default_factory=dict)
    # passive caches
    last_values: dict[str, list] = field(default_factory=dict)
    meters: dict[str, tuple[float, list[float]]] = field(default_factory=dict)

    def start(self) -> None:
        if self._running:
            return
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind(("", 0))
        self._sock.settimeout(0.2)
        self._running = True
        self._rx_thread = threading.Thread(target=self._rx_loop, daemon=True)
        self._rx_thread.start()

    def stop(self) -> None:
        self._running = False
        if self._sock:
            self._sock.close()
            self._sock = None

    # -- low level ----------------------------------------------------------

    def send(self, address: str, *args: Any) -> None:
        self.start()
        assert self._sock
        self._sock.sendto(encode(address, *args), (self.host, self.port))

    def _rx_loop(self) -> None:
        while self._running and self._sock:
            try:
                data, _ = self._sock.recvfrom(65536)
            except socket.timeout:
                continue
            except OSError:
                break
            try:
                address, args = decode(data)
            except Exception:
                continue
            if address.startswith("/meters/") and args and isinstance(args[0], (bytes, bytearray)):
                self.meters[address] = (time.time(), decode_meter_blob(args[0]))
            self.last_values[address] = args
            # fulfil pending request (exact or loose match e.g. 'node')
            with self._lock:
                waiter = self._pending.get(address) or self._pending.get(address.lstrip("/"))
                if waiter is None and address in ("node", "/node"):
                    # /node replies: match the single outstanding node request
                    waiter = self._pending.get("__node__")
                if waiter:
                    waiter[1].append((address, args))
                    waiter[0].set()

    def request(self, address: str, *args: Any, expect: str | None = None) -> tuple[str, list]:
        """Send and wait for the reply. `expect` overrides the reply address key."""
        self.start()
        key = expect or address
        ev = threading.Event()
        box: list = []
        with self._lock:
            self._pending[key] = (ev, box)
        try:
            for attempt in range(self.retries + 1):
                self.send(address, *args)
                if ev.wait(self.timeout):
                    return box[-1]
            raise TimeoutError(
                f"No reply from mixer at {self.host}:{self.port} for '{address}' "
                f"after {self.retries + 1} attempts. Check the mixer is on, on the same "
                f"network, and the IP is correct (find it in Mixing Station's connection screen).")
        finally:
            with self._lock:
                self._pending.pop(key, None)

    # -- high level -----------------------------------------------------------

    def get(self, address: str) -> list:
        return self.request(address)[1]

    def set(self, address: str, value: Any) -> None:
        self.send(address, value)

    def set_and_confirm(self, address: str, value: Any) -> list:
        """Set, then read back the value for verification."""
        self.send(address, value)
        time.sleep(0.05)
        return self.get(address)

    def xinfo(self) -> list:
        return self.request("/xinfo", expect="/xinfo")[1]

    def node_dump(self, node: str) -> str:
        """Dump a config node as the console's native text line(s)."""
        _, args = self.request("/node", node.lstrip("/"), expect="__node__")
        return "".join(a for a in args if isinstance(a, str))

    def subscribe_meters(self, meter: str = "/meters/1") -> None:
        self.send("/meters", meter)

    def renew(self) -> None:
        self.send("/renew")
