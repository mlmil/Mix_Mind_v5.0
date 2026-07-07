#!/usr/bin/env python3
"""xair_mcp - MCP server for the Behringer X-Air 18 + Mixing Station app.

Natural-language mixer control for Neon Blonde / Sin Chonies:
- Full X-Air OSC address map (searchable) + generic get/set with human units
- Ergonomic tools: faders, mutes, sends, EQ, preamps, FX, snapshots
- Band macros (break music, kill FX, ...) stored in presets/band_presets.json
- Live metering, full-state backup via /node dumps
- Mixing Station Desktop app API passthrough (REST/WebSocket)

Env config:
  XAIR_HOST     mixer IP (else use xair_discover / xair_connect)
  MS_API_URL    Mixing Station REST url (default http://127.0.0.1:8080)
  XAIR_PRESETS  path to band presets json (default: repo presets/band_presets.json)
"""
from __future__ import annotations

import asyncio
import copy
import datetime as _dt
import json
import os
import re
import socket
import time
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from . import conversions as conv
from . import osc_map
from .osc_client import XAirClient, XAIR_PORT, encode, decode
from .ms_client import MixingStationClient, connection_help, DEFAULT_URL

mcp = FastMCP("xair_mcp")

# --------------------------------------------------------------------------
# State
# --------------------------------------------------------------------------

_client: XAirClient | None = None
_PRESETS_PATH = Path(os.environ.get(
    "XAIR_PRESETS",
    Path(__file__).resolve().parent.parent / "presets" / "band_presets.json"))
_ms = MixingStationClient(os.environ.get("MS_API_URL", DEFAULT_URL))


def _mixer() -> XAirClient:
    global _client
    if _client is None:
        host = os.environ.get("XAIR_HOST")
        if not host:
            raise RuntimeError(
                "No mixer configured. Run xair_discover to find the XAir18 on the "
                "network, then xair_connect with its IP (or set env XAIR_HOST).")
        _client = XAirClient(host)
    return _client


STRIP_ALIASES = {
    "lr": "/lr", "main": "/lr", "master": "/lr",
    "aux": "/rtn/aux", "usb": "/rtn/aux", "ch17": "/rtn/aux", "ch18": "/rtn/aux",
}


def _resolve_strip(strip: str) -> str:
    """'ch5'/'channel 5'/'bus 2'/'fx3'/'rtn2'/'dca1'/'lr' -> OSC base path."""
    s = strip.strip().lower().replace(" ", "")
    if s in STRIP_ALIASES:
        return STRIP_ALIASES[s]
    m = re.fullmatch(r"(?:ch|channel|input)?0*(\d{1,2})", s)
    if m and 1 <= int(m.group(1)) <= 16:
        return f"/ch/{int(m.group(1)):02d}"
    m = re.fullmatch(r"bus0*(\d)", s)
    if m and 1 <= int(m.group(1)) <= 6:
        return f"/bus/{int(m.group(1))}"
    m = re.fullmatch(r"(?:fxsend|fxs|fx)0*(\d)", s)
    if m and 1 <= int(m.group(1)) <= 4:
        return f"/fxsend/{int(m.group(1))}"
    m = re.fullmatch(r"(?:rtn|fxrtn|return)0*(\d)", s)
    if m and 1 <= int(m.group(1)) <= 4:
        return f"/rtn/{int(m.group(1))}"
    m = re.fullmatch(r"dca0*(\d)", s)
    if m and 1 <= int(m.group(1)) <= 4:
        return f"/dca/{int(m.group(1))}"
    raise ValueError(
        f"Cannot resolve strip '{strip}'. Use ch1-ch16, aux/usb, bus1-6, fxsend1-4, "
        "rtn1-4, dca1-4, or lr. To target by channel NAME, first call "
        "xair_channel_overview to see which number has that name.")


def _auto_norm(entry: dict | None, value: Any, unit: str | None) -> Any:
    """Convert a human value to the wire value using explicit or mapped unit."""
    if unit and unit != "raw":
        return float(conv.human_to_norm(unit, float(value)))
    if unit == "raw" or entry is None:
        return value
    map_unit = entry.get("unit")
    if map_unit and isinstance(value, (int, float)) and not (
            isinstance(value, (int, float)) and entry["type"] == "i"):
        return float(conv.human_to_norm(map_unit, float(value)))
    if entry["type"] == "i" and isinstance(value, float) and value.is_integer():
        return int(value)
    if entry["type"] == "f" and isinstance(value, int):
        return float(value)
    return value


def _fmt_value(address: str, args: list) -> dict:
    """Wire value -> {raw, human?} using the map."""
    entry = osc_map.find_entry(address)
    out: dict[str, Any] = {"address": address, "raw": args[0] if len(args) == 1 else args}
    if entry:
        if entry.get("unit") and args and isinstance(args[0], float):
            human = conv.norm_to_human(entry["unit"], args[0])
            desc = conv.UNIT_CONVERTERS[entry["unit"]][2]
            out["human"] = round(human, 2)
            out["human_unit"] = desc
        if entry.get("enum") and args and isinstance(args[0], int) and 0 <= args[0] < len(entry["enum"]):
            out["enum_label"] = entry["enum"][args[0]]
        out["desc"] = entry["desc"]
    return out


def _run(fn, *a, **kw):
    return asyncio.get_event_loop().run_in_executor(None, lambda: fn(*a, **kw))


# ==========================================================================
# Discovery / connection
# ==========================================================================

@mcp.tool(name="xair_discover",
          annotations={"title": "Discover X-Air mixers on the network",
                       "readOnlyHint": True, "openWorldHint": True})
async def xair_discover(wait_seconds: float = 2.0) -> str:
    """Broadcast /xinfo on UDP 10024 and list every X-Air mixer that answers.

    Returns JSON list of {ip, name, model, firmware}. Use xair_connect with the
    IP afterwards. If nothing is found: mixer off, different subnet/VLAN, or
    an AP client-isolation issue.
    """
    def scan() -> list[dict]:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.settimeout(0.3)
        s.sendto(encode("/xinfo"), ("255.255.255.255", XAIR_PORT))
        found, deadline = [], time.time() + wait_seconds
        while time.time() < deadline:
            try:
                data, addr = s.recvfrom(4096)
                _, args = decode(data)
                found.append({"ip": addr[0],
                              "reported_ip": args[0] if args else None,
                              "name": args[1] if len(args) > 1 else None,
                              "model": args[2] if len(args) > 2 else None,
                              "firmware": args[3] if len(args) > 3 else None})
            except socket.timeout:
                continue
        s.close()
        return found

    found = await _run(scan)
    if not found:
        return ("No X-Air mixers replied to broadcast. Check: mixer powered on, same "
                "network/subnet as this Mac, no VLAN/client isolation. You can still "
                "connect directly with xair_connect if you know the IP.")
    return json.dumps(found, indent=2)


@mcp.tool(name="xair_connect",
          annotations={"title": "Connect to the XAir18", "readOnlyHint": True,
                       "openWorldHint": True})
async def xair_connect(host: str) -> str:
    """Set the mixer IP and verify the connection via /xinfo.

    Args: host - IP address of the XAir18 (e.g. '192.168.1.50').
    Returns mixer info on success.
    """
    global _client
    _client = XAirClient(host)
    info = await _run(_client.xinfo)
    return json.dumps({"connected": True, "host": host, "xinfo": info})


@mcp.tool(name="xair_info",
          annotations={"title": "Mixer info/status", "readOnlyHint": True,
                       "openWorldHint": True})
async def xair_info() -> str:
    """Get mixer identity (/xinfo) and status (/status) from the connected XAir18."""
    c = _mixer()
    info = await _run(c.xinfo)
    try:
        status = (await _run(c.request, "/status", expect="/status"))[1]
    except Exception:
        status = None
    return json.dumps({"host": c.host, "xinfo": info, "status": status})


# ==========================================================================
# OSC map (the "language dictionary")
# ==========================================================================

@mcp.tool(name="xair_map_search",
          annotations={"title": "Search the X-Air OSC address map",
                       "readOnlyHint": True})
async def xair_map_search(query: str, category: str = "", limit: int = 30) -> str:
    """Search the complete XAir18 OSC command map by keywords.

    THE starting point for any parameter you don't know the address of.
    Query terms are ANDed against path + description, e.g. 'gate threshold',
    'phantom', 'snapshot load', 'fx type'.
    Categories: channel, aux_return, fx_return, bus, fx_send, main_lr, fx,
    headamp, config, dca, snapshot, status, command.
    Returns patterned entries; {ch:02d} etc. expand per 'expand' ranges
    (addresses are 1-based zero-padded, e.g. /ch/05/...).
    """
    res = osc_map.search(query, category or None, limit)
    if not res:
        return (f"No entries match '{query}'. Try broader terms, or use "
                f"xair_node_dump to explore the live mixer tree. Stats: "
                f"{json.dumps(osc_map.stats())}")
    slim = [{k: v for k, v in e.items() if v not in (None, False)} for e in res]
    return json.dumps({"count": len(res), "entries": slim}, indent=1)


@mcp.tool(name="xair_map_describe",
          annotations={"title": "Describe one OSC address", "readOnlyHint": True})
async def xair_map_describe(address: str) -> str:
    """Explain a concrete OSC address: type, range/enum, unit conversion law,
    verified flag. E.g. '/ch/05/dyn/thr'. Also lists all available unit names.
    """
    entry = osc_map.find_entry(address)
    if not entry:
        return (f"'{address}' is not in the map (may still exist on the mixer - "
                "try xair_get or xair_node_dump). Use xair_map_search to browse.")
    out = dict(entry)
    unit = entry.get("unit")
    if unit:
        out["unit_desc"] = conv.UNIT_CONVERTERS[unit][2]
    out["all_units"] = {k: v[2] for k, v in conv.UNIT_CONVERTERS.items()}
    return json.dumps(out, indent=1, default=str)


# ==========================================================================
# Generic get / set - the "hack anything" layer
# ==========================================================================

@mcp.tool(name="xair_get",
          annotations={"title": "Get any OSC parameter", "readOnlyHint": True,
                       "openWorldHint": True})
async def xair_get(address: str) -> str:
    """Read any OSC parameter from the mixer, e.g. '/ch/05/mix/fader'.

    Returns raw wire value plus human units (dB, Hz, ...) when the map knows
    the conversion. Works for unmapped addresses too.
    """
    c = _mixer()
    args = await _run(c.get, address)
    return json.dumps(_fmt_value(address, args))


@mcp.tool(name="xair_set",
          annotations={"title": "Set any OSC parameter", "readOnlyHint": False,
                       "destructiveHint": True, "openWorldHint": True})
async def xair_set(address: str, value: float | int | str, unit: str = "") -> str:
    """Set any OSC parameter on the mixer and read back for confirmation.

    Args:
        address: OSC address, e.g. '/ch/05/mix/fader'
        value: the value. If `unit` given (or the map defines one for a float
               param), human units are converted to wire format automatically:
               e.g. address='/ch/05/mix/fader', value=-6, unit='fader_db'.
        unit: '', a unit name from xair_map_describe, or 'raw' to skip conversion.
    Returns the confirmed value after setting.
    """
    c = _mixer()
    entry = osc_map.find_entry(address)
    wire = _auto_norm(entry, value, unit or None)
    args = await _run(c.set_and_confirm, address, wire)
    out = _fmt_value(address, args)
    out["sent_wire_value"] = wire
    return json.dumps(out)


@mcp.tool(name="xair_batch_set",
          annotations={"title": "Set many OSC parameters", "readOnlyHint": False,
                       "destructiveHint": True, "openWorldHint": True})
async def xair_batch_set(operations: list[dict], confirm_each: bool = False) -> str:
    """Fire a list of OSC sets in order (fast, ~1ms apart).

    Each operation: {"address": str, "value": num|str, "unit": optional str}.
    Set confirm_each=true to read back every value (slower).
    """
    c = _mixer()
    results = []
    for op in operations:
        entry = osc_map.find_entry(op["address"])
        wire = _auto_norm(entry, op["value"], op.get("unit"))
        if confirm_each:
            args = await _run(c.set_and_confirm, op["address"], wire)
            results.append(_fmt_value(op["address"], args))
        else:
            await _run(c.set, op["address"], wire)
            results.append({"address": op["address"], "sent": wire})
        await asyncio.sleep(0.002)
    return json.dumps({"count": len(results), "results": results})


@mcp.tool(name="xair_node_dump",
          annotations={"title": "Dump mixer config node (discovery)",
                       "readOnlyHint": True, "openWorldHint": True})
async def xair_node_dump(node: str) -> str:
    """Dump a node of the mixer's config tree as native console text via /node.

    THE tool for exploring/verifying the real parameter tree ("hacking").
    Examples: 'ch/01/config', 'ch/05/dyn', 'lr/eq', 'bus/1', '-snap/01',
    'config/solo', 'fx/1'. Returns the raw line(s) with current values in order.
    """
    c = _mixer()
    text = await _run(c.node_dump, node)
    return text or f"(empty reply for node '{node}')"


# ==========================================================================
# Ergonomic mixer tools
# ==========================================================================

@mcp.tool(name="xair_channel_overview",
          annotations={"title": "Board overview: names, faders, mutes",
                       "readOnlyHint": True, "openWorldHint": True})
async def xair_channel_overview() -> str:
    """Snapshot of the whole board: every strip's name, color, fader (dB),
    mute state and LR assignment. Use this FIRST to map human names
    ('lead vox') to strip numbers. Covers ch1-16, aux, fx returns, buses,
    fx sends, LR.
    """
    c = _mixer()

    def read() -> list[dict]:
        strips = ([(f"ch{i}", f"/ch/{i:02d}") for i in range(1, 17)]
                  + [("aux(17/18)", "/rtn/aux")]
                  + [(f"rtn{i}", f"/rtn/{i}") for i in range(1, 5)]
                  + [(f"bus{i}", f"/bus/{i}") for i in range(1, 7)]
                  + [(f"fxsend{i}", f"/fxsend/{i}") for i in range(1, 5)]
                  + [("lr", "/lr")])
        rows = []
        for label, base in strips:
            row: dict[str, Any] = {"strip": label}
            try:
                if base != "/lr":
                    row["name"] = (c.get(f"{base}/config/name") or [""])[0]
                    color = (c.get(f"{base}/config/color") or [0])[0]
                    row["color"] = osc_map.COLORS[color] if isinstance(color, int) and color < 16 else color
                fader = (c.get(f"{base}/mix/fader") or [0.0])[0]
                row["fader_db"] = round(conv.fader_to_db(fader), 1)
                row["muted"] = not bool((c.get(f"{base}/mix/on") or [1])[0])
                if base.startswith("/ch") or base == "/rtn/aux":
                    row["to_lr"] = bool((c.get(f"{base}/mix/lr") or [1])[0])
            except TimeoutError as e:
                row["error"] = str(e)
                rows.append(row)
                break
            rows.append(row)
        return rows

    return json.dumps(await _run(read), indent=1)


@mcp.tool(name="xair_fader",
          annotations={"title": "Set a fader", "readOnlyHint": False,
                       "openWorldHint": True})
async def xair_fader(strip: str, level_db: float) -> str:
    """Set any strip's fader in dB (-90..+10; <=-90 = -inf/off).

    strip: 'ch1'..'ch16', 'aux', 'rtn1-4', 'bus1-6', 'fxsend1-4', 'dca1-4', 'lr'.
    For named channels ('lead vox'), first find the number via xair_channel_overview.
    """
    base = _resolve_strip(strip)
    c = _mixer()
    args = await _run(c.set_and_confirm, f"{base}/mix/fader", conv.db_to_fader(level_db))
    return json.dumps({"strip": base, "fader_db": round(conv.fader_to_db(args[0]), 1)})


@mcp.tool(name="xair_mute",
          annotations={"title": "Mute/unmute a strip", "readOnlyHint": False,
                       "openWorldHint": True})
async def xair_mute(strip: str, muted: bool) -> str:
    """Mute (true) or unmute (false) a strip. Same strip syntax as xair_fader.
    Note: wire format is inverted ('on': 1=unmuted); this tool handles that.
    """
    base = _resolve_strip(strip)
    c = _mixer()
    args = await _run(c.set_and_confirm, f"{base}/mix/on", 0 if muted else 1)
    return json.dumps({"strip": base, "muted": not bool(args[0])})


@mcp.tool(name="xair_mute_group",
          annotations={"title": "Engage/release a mute group",
                       "readOnlyHint": False, "openWorldHint": True})
async def xair_mute_group(group: int, engaged: bool) -> str:
    """Engage (true) or release (false) mute group 1-4. Engaging mutes all members."""
    if not 1 <= group <= 4:
        return "Error: mute group must be 1-4."
    c = _mixer()
    args = await _run(c.set_and_confirm, f"/config/mute/{group}", 1 if engaged else 0)
    return json.dumps({"mute_group": group, "engaged": bool(args[0])})


@mcp.tool(name="xair_send_level",
          annotations={"title": "Set a monitor/FX send level", "readOnlyHint": False,
                       "openWorldHint": True})
async def xair_send_level(channel: str, destination: str, level_db: float) -> str:
    """Set how much of a channel goes to a bus (monitor) or FX.

    channel: 'ch1'..'ch16', 'aux', 'rtn1-4'.
    destination: 'bus1'..'bus6' (monitor/aux mixes) or 'fx1'..'fx4'.
    level_db: -90..+10.
    E.g. 'more vocal in the drummer's wedge on bus 2' -> channel='ch5',
    destination='bus2', level_db=-5.
    """
    base = _resolve_strip(channel)
    d = destination.strip().lower().replace(" ", "")
    m = re.fullmatch(r"bus0*([1-6])", d)
    if m:
        slot = int(m.group(1))
    else:
        m = re.fullmatch(r"fx0*([1-4])", d)
        if not m:
            return "Error: destination must be bus1-6 or fx1-4."
        slot = 6 + int(m.group(1))
    c = _mixer()
    addr = f"{base}/mix/{slot:02d}/level"
    args = await _run(c.set_and_confirm, addr, conv.db_to_fader(level_db))
    return json.dumps({"address": addr, "level_db": round(conv.fader_to_db(args[0]), 1)})


@mcp.tool(name="xair_channel_detail",
          annotations={"title": "Full channel strip detail", "readOnlyHint": True,
                       "openWorldHint": True})
async def xair_channel_detail(strip: str) -> str:
    """Read a strip's full processing chain via /node dumps: config, preamp/
    headamp, gate, dynamics, insert, EQ, mix, sends. Native console text format
    (values in order as documented by the map).
    """
    base = _resolve_strip(strip).lstrip("/")
    c = _mixer()
    nodes = [f"{base}/config", f"{base}/preamp", f"{base}/gate", f"{base}/dyn",
             f"{base}/insert", f"{base}/eq", f"{base}/mix", f"{base}/grp"]
    if base.startswith("ch/"):
        ch_num = int(base.split("/")[1])
        nodes.insert(1, f"headamp/{ch_num:02d}")
        nodes += [f"{base}/mix/{s:02d}" for s in range(1, 11)]
        nodes.append(f"{base}/automix")

    def read() -> dict:
        out = {}
        for n in nodes:
            try:
                out[n] = c.node_dump(n).strip()
            except TimeoutError:
                out[n] = "(no reply - node may not exist for this strip type)"
        return out

    return json.dumps(await _run(read), indent=1)


@mcp.tool(name="xair_eq_band",
          annotations={"title": "Set an EQ band", "readOnlyHint": False,
                       "openWorldHint": True})
async def xair_eq_band(strip: str, band: int, freq_hz: float | None = None,
                       gain_db: float | None = None, q: float | None = None,
                       band_type: str = "") -> str:
    """Adjust one parametric EQ band on any strip.

    strip: same syntax as xair_fader. band: 1-4 on channels, 1-6 on buses/LR.
    Provide any of freq_hz (20-20000), gain_db (-15..+15), q (0.3-10),
    band_type ('LCut','LShv','PEQ','VEQ','HShv','HCut').
    E.g. 'cut 3k on the vocal by 4dB' -> strip='ch5', band=3, freq_hz=3000,
    gain_db=-4.
    """
    base = _resolve_strip(strip)
    c = _mixer()
    ops, out = [], {}
    if band_type:
        if band_type not in osc_map.EQ_TYPES:
            return f"Error: band_type must be one of {osc_map.EQ_TYPES}"
        ops.append((f"{base}/eq/{band}/type", osc_map.EQ_TYPES.index(band_type)))
    if freq_hz is not None:
        ops.append((f"{base}/eq/{band}/f", conv.freq_to_norm(freq_hz)))
    if gain_db is not None:
        ops.append((f"{base}/eq/{band}/g", conv.human_to_norm("eq_gain", gain_db)))
    if q is not None:
        ops.append((f"{base}/eq/{band}/q", conv.human_to_norm("eq_q", q)))
    if not ops:
        return "Error: provide at least one of band_type/freq_hz/gain_db/q."
    for addr, wire in ops:
        args = await _run(c.set_and_confirm, addr, wire)
        out[addr] = _fmt_value(addr, args)
    return json.dumps(out, indent=1)


@mcp.tool(name="xair_headamp",
          annotations={"title": "Preamp gain / phantom power", "readOnlyHint": False,
                       "destructiveHint": True, "openWorldHint": True})
async def xair_headamp(channel: int, gain_db: float | None = None,
                       phantom: bool | None = None) -> str:
    """Set preamp gain (-12..+60 dB) and/or 48V phantom for input 1-16.

    CAUTION: toggling phantom while a condenser mic is hot can pop the PA;
    gain changes affect everything post-preamp. Confirm with the user before
    large changes during a show.
    """
    if not 1 <= channel <= 16:
        return "Error: channel must be 1-16 (physical XLR inputs)."
    c = _mixer()
    out = {}
    if gain_db is not None:
        addr = f"/headamp/{channel:02d}/gain"
        args = await _run(c.set_and_confirm, addr, conv.headamp_gain_to_norm(gain_db))
        out["gain_db"] = round(conv.norm_to_headamp_gain(args[0]), 1)
    if phantom is not None:
        addr = f"/headamp/{channel:02d}/phantom"
        args = await _run(c.set_and_confirm, addr, 1 if phantom else 0)
        out["phantom"] = bool(args[0])
    return json.dumps({"channel": channel, **out}) if out else \
        "Error: provide gain_db and/or phantom."


@mcp.tool(name="xair_fx",
          annotations={"title": "Get/set FX slot", "readOnlyHint": False,
                       "openWorldHint": True})
async def xair_fx(slot: int, fx_type: str = "", params: dict[str, float] | None = None) -> str:
    """Inspect or modify FX slot 1-4.

    No args beyond slot: returns current type + all parameter values.
    fx_type: set algorithm by name from the FX_TYPES list (see xair_map_search
    'fx type'). params: {"01": 0.5, ...} normalized 0..1 (param meanings depend
    on the algorithm - dump first, tweak, re-check).
    """
    if not 1 <= slot <= 4:
        return "Error: slot must be 1-4."
    c = _mixer()
    out: dict[str, Any] = {"slot": slot}
    if fx_type:
        if fx_type not in osc_map.FX_TYPES:
            return f"Error: unknown fx_type. Known: {osc_map.FX_TYPES}"
        args = await _run(c.set_and_confirm, f"/fx/{slot}/type", osc_map.FX_TYPES.index(fx_type))
        out["type_set_to"] = osc_map.FX_TYPES[args[0]] if args[0] < len(osc_map.FX_TYPES) else args[0]
    if params:
        for p, v in params.items():
            addr = f"/fx/{slot}/par/{int(p):02d}"
            await _run(c.set, addr, float(v))
        out["params_sent"] = params
    if not fx_type and not params:
        t = (await _run(c.get, f"/fx/{slot}/type"))[0]
        out["type"] = osc_map.FX_TYPES[t] if isinstance(t, int) and t < len(osc_map.FX_TYPES) else t
        out["type_index"] = t
        out["node_dump"] = await _run(c.node_dump, f"fx/{slot}")
    return json.dumps(out, indent=1)


# ==========================================================================
# Snapshots & backup
# ==========================================================================

@mcp.tool(name="xair_snapshot_list",
          annotations={"title": "List mixer snapshots", "readOnlyHint": True,
                       "openWorldHint": True})
async def xair_snapshot_list() -> str:
    """List all 64 snapshot slots with names (empty names = unused slots).
    NOTE: slot 64 may hold Mixing Station's bus password protection - avoid
    overwriting it if bus passwords are in use.
    """
    c = _mixer()

    def read() -> list[dict]:
        rows = []
        for i in range(1, 65):
            try:
                name = (c.get(f"/-snap/{i:02d}/name") or [""])[0]
            except TimeoutError:
                name = "(no reply)"
            if name:
                rows.append({"slot": i, "name": name})
        return rows

    rows = await _run(read)
    return json.dumps({"used_slots": rows, "note": "64 slots total; only named/used shown"})


@mcp.tool(name="xair_snapshot_save",
          annotations={"title": "Save snapshot", "readOnlyHint": False,
                       "destructiveHint": True, "openWorldHint": True})
async def xair_snapshot_save(slot: int, name: str = "") -> str:
    """Save the mixer's CURRENT state into snapshot slot 1-64 (overwrites!).
    Optionally set the slot name. Avoid slot 64 if Mixing Station bus
    passwords are used.
    """
    if not 1 <= slot <= 64:
        return "Error: slot must be 1-64."
    c = _mixer()
    await _run(c.send, "/-snap/save", slot)
    await asyncio.sleep(0.3)
    if name:
        await _run(c.set, f"/-snap/{slot:02d}/name", name)
        await asyncio.sleep(0.1)
    stored = (await _run(c.get, f"/-snap/{slot:02d}/name") or [""])[0]
    return json.dumps({"saved_to_slot": slot, "name": stored})


@mcp.tool(name="xair_snapshot_load",
          annotations={"title": "Load snapshot", "readOnlyHint": False,
                       "destructiveHint": True, "openWorldHint": True})
async def xair_snapshot_load(slot: int) -> str:
    """LOAD snapshot slot 1-64. DANGER: instantly changes the entire mixer
    state (faders, mutes, routing). Confirm with the user before doing this
    during a live show.
    """
    if not 1 <= slot <= 64:
        return "Error: slot must be 1-64."
    c = _mixer()
    name = (await _run(c.get, f"/-snap/{slot:02d}/name") or [""])[0]
    await _run(c.send, "/-snap/load", slot)
    return json.dumps({"loaded_slot": slot, "name": name,
                       "note": "Full mixer state replaced."})


BACKUP_NODES = (
    [f"ch/{i:02d}/{s}" for i in range(1, 17)
     for s in ["config", "preamp", "gate", "dyn", "insert", "eq", "mix", "grp", "automix"]]
    + [f"ch/{i:02d}/mix/{s:02d}" for i in range(1, 17) for s in range(1, 11)]
    + [f"rtn/aux/{s}" for s in ["config", "eq", "mix", "grp"]]
    + [f"rtn/{i}/{s}" for i in range(1, 5) for s in ["config", "eq", "mix", "grp"]]
    + [f"bus/{i}/{s}" for i in range(1, 7) for s in ["config", "dyn", "insert", "eq", "mix", "grp"]]
    + [f"fxsend/{i}/{s}" for i in range(1, 5) for s in ["config", "mix", "grp"]]
    + [f"lr/{s}" for s in ["config", "dyn", "insert", "eq", "mix"]]
    + [f"fx/{i}" for i in range(1, 5)]
    + [f"headamp/{i:02d}" for i in range(1, 17)]
    + ["config/mute", "config/linkcfg", "config/solo", "config/chlink", "config/buslink"]
)


@mcp.tool(name="xair_backup_dump",
          annotations={"title": "Backup full mixer state to file",
                       "readOnlyHint": True, "openWorldHint": True})
async def xair_backup_dump(label: str = "") -> str:
    """Dump the ENTIRE mixer state (all channels/buses/fx/config) via /node
    to a timestamped text file in the backups/ folder next to the server.
    The format matches the console's native scene lines - great for
    versioning gigs ('Neon Blonde @ Riverside 2026-07-04') and diffing.
    Takes ~30-60s.
    """
    c = _mixer()
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    safe = re.sub(r"[^\w\-]+", "_", label) if label else "backup"
    path = Path(__file__).resolve().parent.parent / "backups"
    path.mkdir(exist_ok=True)
    fp = path / f"{safe}-{stamp}.xair.txt"

    def dump() -> tuple[int, int]:
        ok = fail = 0
        with open(fp, "w") as f:
            f.write(f"# XAir18 state dump - {label or 'backup'} - {stamp}\n")
            f.write(f"# host {c.host}\n")
            for node in BACKUP_NODES:
                try:
                    line = c.node_dump(node).strip()
                    f.write(line + "\n")
                    ok += 1
                except TimeoutError:
                    f.write(f"# NO-REPLY {node}\n")
                    fail += 1
        return ok, fail

    ok, fail = await _run(dump)
    return json.dumps({"file": str(fp), "nodes_ok": ok, "nodes_failed": fail})


# ==========================================================================
# Metering
# ==========================================================================

METERS1_LABELS = (
    [f"ch{i}" for i in range(1, 17)] + ["auxL", "auxR"]
    + [f"rtn{i}{lr}" for i in range(1, 5) for lr in ("L", "R")]
    + [f"bus{i}" for i in range(1, 7)] + [f"fxsend{i}" for i in range(1, 5)]
    + ["mainL", "mainR", "monL", "monR"]
)  # 40 values - labeling per community docs, verify against your unit


@mcp.tool(name="xair_meters",
          annotations={"title": "Read live meters", "readOnlyHint": True,
                       "openWorldHint": True})
async def xair_meters(meter_id: int = 1, duration_seconds: float = 1.0) -> str:
    """Sample live levels for ~duration and return peak+mean dB per slot.

    meter_id 1 = all strips (in1-16, aux, fx returns, buses, fx sends, LR, mon).
    Other ids (0-8) return raw unlabeled arrays (input/dynamics/rta banks).
    Use for questions like 'is the kick clipping?' (ch levels near 0 dBFS clip;
    good gig level peaks around -18..-9).
    """
    c = _mixer()
    addr = f"/meters/{meter_id}"

    def sample() -> list[list[float]]:
        c.subscribe_meters(addr)
        frames: list[list[float]] = []
        end = time.time() + max(0.3, min(duration_seconds, 10.0))
        while time.time() < end:
            time.sleep(0.05)
            got = c.meters.get(addr)
            if got and (not frames or got[1] != frames[-1]):
                frames.append(got[1])
        return frames

    frames = await _run(sample)
    if not frames:
        return ("No meter data received. The mixer streams meters for ~10s per "
                "subscription; check connection with xair_info and retry.")
    n = len(frames[0])
    peaks = [round(max(f[i] for f in frames), 1) for i in range(n)]
    means = [round(sum(f[i] for f in frames) / len(frames), 1) for i in range(n)]
    if meter_id == 1 and n == len(METERS1_LABELS):
        data = [{"slot": METERS1_LABELS[i], "peak_db": peaks[i], "mean_db": means[i]}
                for i in range(n)]
    else:
        data = [{"index": i, "peak_db": peaks[i], "mean_db": means[i]} for i in range(n)]
    return json.dumps({"meter": addr, "frames": len(frames), "values": data})


# ==========================================================================
# Band macros
# ==========================================================================

def _load_presets() -> dict:
    if _PRESETS_PATH.exists():
        return json.loads(_PRESETS_PATH.read_text())
    return {"macros": {}}


def _expand_macro_ops(ops: list[dict]) -> list[dict]:
    out = []
    for op in ops:
        rep = op.get("repeat_ch")
        if rep:
            for chn in range(rep[0], rep[1] + 1):
                o = copy.deepcopy(op)
                o.pop("repeat_ch")
                o["address"] = re.sub(r"/ch/\d\d/", f"/ch/{chn:02d}/", op["address"])
                out.append(o)
        else:
            out.append(op)
    return out


@mcp.tool(name="xair_macro_list",
          annotations={"title": "List band macros", "readOnlyHint": True})
async def xair_macro_list() -> str:
    """List saved band macros (break_music, kill_fx, mute_all_inputs, ...)
    with descriptions and operation counts.
    """
    p = _load_presets()
    out = [{"name": k, "description": v.get("description", ""),
            "operations": len(_expand_macro_ops(v.get("operations", [])))}
           for k, v in p.get("macros", {}).items()]
    return json.dumps({"presets_file": str(_PRESETS_PATH), "macros": out}, indent=1)


@mcp.tool(name="xair_macro_run",
          annotations={"title": "Run a band macro", "readOnlyHint": False,
                       "destructiveHint": True, "openWorldHint": True})
async def xair_macro_run(name: str) -> str:
    """Execute a saved macro by name (see xair_macro_list). Runs all its OSC
    operations in order against the mixer.
    """
    p = _load_presets()
    macro = p.get("macros", {}).get(name)
    if not macro:
        return f"Error: no macro '{name}'. Available: {sorted(p.get('macros', {}))}"
    ops = _expand_macro_ops(macro.get("operations", []))
    c = _mixer()
    for op in ops:
        entry = osc_map.find_entry(op["address"])
        wire = _auto_norm(entry, op["value"], op.get("unit"))
        await _run(c.set, op["address"], wire)
        await asyncio.sleep(0.002)
    return json.dumps({"ran": name, "operations": len(ops),
                       "description": macro.get("description", "")})


@mcp.tool(name="xair_macro_save",
          annotations={"title": "Save a band macro", "readOnlyHint": False})
async def xair_macro_save(name: str, description: str,
                          operations: list[dict]) -> str:
    """Create or overwrite a named macro in the presets file.

    operations: [{"address": "/ch/05/mix/on", "value": 0, "unit": optional,
    "repeat_ch": optional [first,last] to repeat over channels}].
    Tip: build the ops with xair_map_search, test with xair_batch_set, then save.
    """
    name = re.sub(r"[^\w\-]+", "_", name.strip().lower())
    p = _load_presets()
    p.setdefault("macros", {})[name] = {"description": description,
                                        "operations": operations}
    _PRESETS_PATH.parent.mkdir(parents=True, exist_ok=True)
    _PRESETS_PATH.write_text(json.dumps(p, indent=2))
    return json.dumps({"saved": name, "operations": len(operations),
                       "file": str(_PRESETS_PATH)})


# ==========================================================================
# Mixing Station app API
# ==========================================================================

@mcp.tool(name="ms_app_state",
          annotations={"title": "Mixing Station app state", "readOnlyHint": True,
                       "openWorldHint": True})
async def ms_app_state() -> str:
    """Get the Mixing Station desktop app's state (connection, current mixer).
    Requires the desktop app running with its REST API enabled
    (app settings -> APIs). Set env MS_API_URL if not on port 8080.
    """
    try:
        return json.dumps(await _ms.app_state(), indent=1, default=str)
    except Exception as e:
        return connection_help(e, _ms.base_url)


@mcp.tool(name="ms_api",
          annotations={"title": "Mixing Station API passthrough",
                       "readOnlyHint": False, "openWorldHint": True})
async def ms_api(path: str, method: str = "GET", body_json: str = "") -> str:
    """Call ANY Mixing Station WebSocket-API endpoint: app control, console
    data, subscriptions. E.g. path='/console/data/val/ch.0.mix.lvl' (NOTE:
    Mixing Station data paths are 0-BASED: ch.0 = channel 1!).
    Open http://localhost:8080 for the interactive API explorer listing all
    endpoints of the connected mixer. body_json: JSON string for POST bodies.
    """
    try:
        body = json.loads(body_json) if body_json else None
        result = await _ms.ws_call(path, method, body)
        return json.dumps(result, indent=1, default=str)
    except Exception as e:
        return connection_help(e, _ms.base_url)


@mcp.tool(name="ms_value",
          annotations={"title": "Get/set value via Mixing Station",
                       "readOnlyHint": False, "openWorldHint": True})
async def ms_value(data_path: str, set_to: float | None = None,
                   fmt: str = "val") -> str:
    """Read or write a console value through Mixing Station's data model.

    data_path example: 'ch.0.mix.lvl' (0-based channel index!). fmt: 'val'
    (plain, e.g. dB) or 'norm' (0..1). Leave set_to empty to read.
    Useful when you want Mixing Station's UI to reflect/log the change, or for
    MS-only features; otherwise prefer the direct xair_* tools.
    """
    try:
        if set_to is None:
            return json.dumps(await _ms.get_value(data_path, fmt), default=str)
        return json.dumps(await _ms.set_value(data_path, set_to, fmt), default=str)
    except Exception as e:
        return connection_help(e, _ms.base_url)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
