"""Tests for xair_mcp: codec, conversions, map, and a mock-mixer round trip."""
from __future__ import annotations

import math
import socket
import struct
import threading
import time

import pytest

from xair_mcp import conversions as conv
from xair_mcp import osc_map
from xair_mcp.osc_client import XAirClient, encode, decode, decode_meter_blob


# --------------------------------------------------------------------------
# Conversions
# --------------------------------------------------------------------------

def test_fader_law_roundtrip():
    for db in [-89.5, -60, -30, -10, 0, 10, -6.02, -18.5]:
        f = conv.db_to_fader(db)
        assert 0.0 <= f <= 1.0
        assert conv.fader_to_db(f) == pytest.approx(db, abs=0.01)


def test_fader_law_anchors():
    assert conv.db_to_fader(0.0) == pytest.approx(0.75)      # unity = 3/4 fader
    assert conv.db_to_fader(10.0) == pytest.approx(1.0)
    assert conv.fader_to_db(0.0) == float("-inf")
    assert conv.db_to_fader(float("-inf")) == 0.0


def test_freq_log_law():
    assert conv.norm_to_freq(0.0) == pytest.approx(20.0)
    assert conv.norm_to_freq(1.0) == pytest.approx(20000.0)
    assert conv.norm_to_freq(0.5) == pytest.approx(math.sqrt(20 * 20000), rel=0.01)
    assert conv.freq_to_norm(1000.0) == pytest.approx(
        math.log(50) / math.log(1000), rel=0.001)


def test_headamp():
    assert conv.norm_to_headamp_gain(0.0) == -12.0
    assert conv.norm_to_headamp_gain(1.0) == 60.0
    assert conv.headamp_gain_to_norm(24.0) == pytest.approx(0.5)


def test_all_units_roundtrip():
    samples = {"fader_db": -12.0, "freq": 2500.0, "freq_hpf": 100.0,
               "eq_gain": -4.0, "eq_q": 2.0, "gate_thr": -40.0,
               "gate_range": 30.0, "dyn_thr": -20.0, "dyn_knee": 2.0,
               "dyn_mgain": 6.0, "dyn_mix": 50.0, "attack": 30.0,
               "hold": 10.0, "release": 200.0, "pan": -25.0,
               "headamp": 30.0, "automix_w": 3.0, "solo_dim": -20.0,
               "solo_trim": 6.0}
    for unit, val in samples.items():
        f = conv.human_to_norm(unit, val)
        assert 0.0 <= f <= 1.0, unit
        assert conv.norm_to_human(unit, f) == pytest.approx(val, rel=0.02, abs=0.05), unit


# --------------------------------------------------------------------------
# OSC codec
# --------------------------------------------------------------------------

def test_codec_roundtrip():
    for addr, args in [
        ("/ch/01/mix/fader", [0.75]),
        ("/ch/01/config/name", ["Lead Vox"]),
        ("/-snap/load", [12]),
        ("/xremote", []),
        ("/node", ["ch/01/config"]),
    ]:
        a2, args2 = decode(encode(addr, *args))
        assert a2 == addr
        for x, y in zip(args, args2):
            if isinstance(x, float):
                assert y == pytest.approx(x)
            else:
                assert y == x


def test_meter_blob_decode():
    vals = [-128 * 256, -18 * 256, 0]
    blob = struct.pack("<i", len(vals)) + struct.pack(f"<{len(vals)}h", *vals)
    assert decode_meter_blob(blob) == [-128.0, -18.0, 0.0]


# --------------------------------------------------------------------------
# OSC map integrity
# --------------------------------------------------------------------------

def test_map_stats_and_expansion():
    st = osc_map.stats()
    assert st["concrete_addresses"] > 1500
    ch5 = list(osc_map.expand_entry(
        next(e for e in osc_map.ENTRIES if e["path"] == "/ch/{ch:02d}/mix/fader")))
    assert "/ch/05/mix/fader" in ch5 and len(ch5) == 16


def test_find_entry():
    e = osc_map.find_entry("/ch/05/dyn/thr")
    assert e and e["unit"] == "dyn_thr"
    e = osc_map.find_entry("/bus/3/mix/fader")
    assert e and e["category"] == "bus"
    e = osc_map.find_entry("/headamp/09/phantom")
    assert e and e["category"] == "headamp"
    assert osc_map.find_entry("/nonsense/path") is None


def test_search():
    hits = osc_map.search("gate threshold")
    assert any("/gate/thr" in e["path"] for e in hits)
    hits = osc_map.search("phantom")
    assert any("phantom" in e["path"] for e in hits)
    hits = osc_map.search("fader", category="bus")
    assert all(e["category"] == "bus" for e in hits)


def test_every_unit_in_map_exists():
    for e in osc_map.ENTRIES:
        if e.get("unit"):
            assert e["unit"] in conv.UNIT_CONVERTERS, e["path"]


# --------------------------------------------------------------------------
# Mock mixer round trip
# --------------------------------------------------------------------------

class MockXAir(threading.Thread):
    """Tiny UDP server that emulates the X-Air OSC request/reply behavior."""

    def __init__(self):
        super().__init__(daemon=True)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.settimeout(0.2)
        self.port = self.sock.getsockname()[1]
        self.state = {"/ch/05/mix/fader": [0.75],
                      "/ch/05/mix/on": [1],
                      "/ch/05/config/name": ["Lead Vox"]}
        self.running = True

    def run(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
            except socket.timeout:
                continue
            except OSError:
                return
            a, args = decode(data)
            if a == "/xinfo":
                self.sock.sendto(encode("/xinfo", "192.168.1.99", "XR18-Mock",
                                        "XR18", "1.28"), addr)
            elif a == "/node" and args:
                self.sock.sendto(
                    encode("node", f'/{args[0]} "Lead Vox" 1 RD\n'), addr)
            elif args:  # set
                self.state[a] = list(args)
                self.sock.sendto(encode(a, *args), addr)
            else:       # get
                val = self.state.get(a, [0.0])
                self.sock.sendto(encode(a, *val), addr)

    def stop(self):
        self.running = False
        self.sock.close()


@pytest.fixture()
def mock_mixer():
    m = MockXAir()
    m.start()
    yield m
    m.stop()


def test_client_get_set_roundtrip(mock_mixer):
    c = XAirClient("127.0.0.1", port=mock_mixer.port, timeout=1.0)
    try:
        assert c.get("/ch/05/mix/fader") == [pytest.approx(0.75)]
        assert c.get("/ch/05/config/name") == ["Lead Vox"]
        got = c.set_and_confirm("/ch/05/mix/fader", conv.db_to_fader(-6.0))
        assert conv.fader_to_db(got[0]) == pytest.approx(-6.0, abs=0.05)
        info = c.xinfo()
        assert info[2] == "XR18"
        dump = c.node_dump("ch/05/config")
        assert "Lead Vox" in dump
    finally:
        c.stop()


def test_client_timeout_message():
    c = XAirClient("127.0.0.1", port=1, timeout=0.1, retries=0)
    try:
        with pytest.raises(TimeoutError) as ei:
            c.get("/ch/01/mix/fader")
        assert "Mixing Station" in str(ei.value)
    finally:
        c.stop()


# --------------------------------------------------------------------------
# Server-level helpers
# --------------------------------------------------------------------------

def test_resolve_strip():
    from xair_mcp.server import _resolve_strip
    assert _resolve_strip("ch5") == "/ch/05"
    assert _resolve_strip("Channel 12") == "/ch/12"
    assert _resolve_strip("bus2") == "/bus/2"
    assert _resolve_strip("fx3") == "/fxsend/3"
    assert _resolve_strip("rtn1") == "/rtn/1"
    assert _resolve_strip("LR") == "/lr"
    assert _resolve_strip("usb") == "/rtn/aux"
    assert _resolve_strip("dca2") == "/dca/2"
    with pytest.raises(ValueError):
        _resolve_strip("ch99")


def test_macro_expansion():
    from xair_mcp.server import _expand_macro_ops
    ops = _expand_macro_ops([{"address": "/ch/01/mix/on", "value": 0,
                              "repeat_ch": [1, 16]}])
    assert len(ops) == 16
    assert ops[4]["address"] == "/ch/05/mix/on"
    assert all("repeat_ch" not in o for o in ops)
