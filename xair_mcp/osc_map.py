"""Complete OSC address map for the Behringer X-Air 18 (X18/XR18).

Sources: Patrick-Gilles Maillot "Unofficial X-Air OSC" protocol notes,
bitfocus/companion-module-behringer-xair, xair-remote, xair-api-python,
and the X AIR EDIT data model. Firmware family V1.12-V1.28.

Entries are *patterned*: `{ch}` expands to channel numbers etc. Each leaf
has type, range/enum, unit (see conversions.UNIT_CONVERTERS) and a
`verified` flag. Unverified leaves are believed correct but should be
confirmed against the live mixer with xair_discover_tree / raw get.

Index conventions (IMPORTANT):
- OSC addresses are 1-based, zero padded: /ch/01 .. /ch/16
- Buses: /bus/1 .. /bus/6 (NOT zero padded)
- FX: /fx/1 .. /fx/4, FX returns /rtn/1 .. /rtn/4, sends /fxsend/1 .. /fxsend/4
- Channel send slots: /ch/NN/mix/01..06 = Bus1-6, /mix/07..10 = FX1-4
- Headamps: /headamp/01 .. /headamp/24 (01-16 = XLR preamps XR18)
"""
from __future__ import annotations

import re
from typing import Any, Iterator

# --------------------------------------------------------------------------
# Enum tables
# --------------------------------------------------------------------------

COLORS = ["OFF", "RD", "GN", "YE", "BL", "MG", "CY", "WH",
          "OFFi", "RDi", "GNi", "YEi", "BLi", "MGi", "CYi", "WHi"]

GATE_MODES = ["EXP2", "EXP3", "EXP4", "GATE", "DUCK"]
DYN_MODES = ["COMP", "EXP"]
DYN_DET = ["PEAK", "RMS"]
DYN_ENV = ["LIN", "LOG"]
DYN_POS = ["PRE", "POST"]
DYN_RATIO = ["1.1", "1.3", "1.5", "2.0", "2.5", "3.0", "4.0", "5.0", "7.0", "10", "20", "100"]
EQ_TYPES = ["LCut", "LShv", "PEQ", "VEQ", "HShv", "HCut"]
INSERT_SEL = ["OFF", "FX1", "FX2", "FX3", "FX4"]
KEYSRC = (["SELF"] + [f"CH{i:02d}" for i in range(1, 17)] + ["BUS1", "BUS2", "BUS3", "BUS4", "BUS5", "BUS6"])
TAP_POINTS = ["IN", "PREEQ", "POSTEQ", "PRE", "POST", "GRP"]
HP_SLOPES = ["12", "18", "24"]
AUTOMIX_GROUPS = ["OFF", "X", "Y"]
SOLO_SOURCES = ["OFF", "LR", "LR+M", "LR PFL", "LR AFL", "AUX 5/6", "AUX 7/8"]

FX_TYPES = [
    "HALL", "AMBI", "RPLT", "ROOM", "CHAM", "PLAT", "VREV", "VRM", "GATE", "RVRS",
    "DLY", "3TAP", "4TAP", "CRS", "FLNG", "PHAS", "DIMC", "FILT", "ROTA", "PAN",
    "SUB", "D/RV", "CR/R", "FL/R", "D/CR", "D/FL", "MODD", "GEQ2", "GEQ", "TEQ2",
    "TEQ", "DES2", "DES", "P1A", "P1A2", "PQ5", "PQ5S", "WAVD", "LIM", "CMB",
    "CMB2", "FAC", "FAC1M", "FAC2", "LEC", "LEC2", "ULC", "ULC2", "ENH2", "ENH",
    "EXC2", "EXC", "IMG", "EDI", "SON", "AMP2", "AMP", "DRV2", "DRV", "PIT2", "PIT",
]  # order approximate for high indices; verify with /fx/N/type on device

# --------------------------------------------------------------------------
# Leaf parameter groups (reused across strip kinds)
# --------------------------------------------------------------------------

def _leaf(path, type_, desc, unit=None, enum=None, rng=None, verified=True, readonly=False):
    return {
        "path": path, "type": type_, "desc": desc, "unit": unit,
        "enum": enum, "range": rng, "verified": verified, "readonly": readonly,
    }


def _config(base, name_desc, with_insrc=False):
    leaves = [
        _leaf(f"{base}/config/name", "s", f"{name_desc} name (scribble strip)"),
        _leaf(f"{base}/config/color", "i", f"{name_desc} color", enum=COLORS),
    ]
    if with_insrc:
        leaves.append(_leaf(f"{base}/config/insrc", "i",
                            "Input source (0-based: XLR1-16=0-15, Aux17/18=16/17)",
                            rng=[0, 17]))
    return leaves


def _preamp(base):
    return [
        _leaf(f"{base}/preamp/invert", "i", "Polarity invert (0=normal, 1=inverted)", rng=[0, 1]),
        _leaf(f"{base}/preamp/hpon", "i", "Low-cut filter on/off", rng=[0, 1]),
        _leaf(f"{base}/preamp/hpslope", "i", "Low-cut slope dB/oct", enum=HP_SLOPES),
        _leaf(f"{base}/preamp/hpf", "f", "Low-cut frequency", unit="freq_hpf"),
        _leaf(f"{base}/preamp/rtnsw", "i", "USB return switch (0=analog input, 1=USB DAW return)",
              rng=[0, 1], verified=True),
    ]


def _gate(base):
    return [
        _leaf(f"{base}/gate/on", "i", "Gate on/off", rng=[0, 1]),
        _leaf(f"{base}/gate/mode", "i", "Gate mode", enum=GATE_MODES),
        _leaf(f"{base}/gate/thr", "f", "Gate threshold", unit="gate_thr"),
        _leaf(f"{base}/gate/range", "f", "Gate range", unit="gate_range"),
        _leaf(f"{base}/gate/attack", "f", "Gate attack", unit="attack"),
        _leaf(f"{base}/gate/hold", "f", "Gate hold", unit="hold"),
        _leaf(f"{base}/gate/release", "f", "Gate release", unit="release"),
        _leaf(f"{base}/gate/keysrc", "i", "Gate key/sidechain source", enum=KEYSRC),
        _leaf(f"{base}/gate/filter/on", "i", "Gate sidechain filter on/off", rng=[0, 1]),
        _leaf(f"{base}/gate/filter/type", "i", "Sidechain filter type (0-8: LC6..HC12, various slopes/BP)", rng=[0, 8]),
        _leaf(f"{base}/gate/filter/f", "f", "Sidechain filter frequency", unit="freq"),
    ]


def _dyn(base):
    return [
        _leaf(f"{base}/dyn/on", "i", "Compressor on/off", rng=[0, 1]),
        _leaf(f"{base}/dyn/mode", "i", "Dynamics mode", enum=DYN_MODES),
        _leaf(f"{base}/dyn/det", "i", "Detector", enum=DYN_DET),
        _leaf(f"{base}/dyn/env", "i", "Envelope", enum=DYN_ENV),
        _leaf(f"{base}/dyn/thr", "f", "Compressor threshold", unit="dyn_thr"),
        _leaf(f"{base}/dyn/ratio", "i", "Compression ratio", enum=DYN_RATIO),
        _leaf(f"{base}/dyn/knee", "f", "Knee", unit="dyn_knee"),
        _leaf(f"{base}/dyn/mgain", "f", "Makeup gain", unit="dyn_mgain"),
        _leaf(f"{base}/dyn/attack", "f", "Attack", unit="attack"),
        _leaf(f"{base}/dyn/hold", "f", "Hold", unit="hold"),
        _leaf(f"{base}/dyn/release", "f", "Release", unit="release"),
        _leaf(f"{base}/dyn/pos", "i", "Position pre/post EQ", enum=DYN_POS),
        _leaf(f"{base}/dyn/keysrc", "i", "Sidechain key source", enum=KEYSRC),
        _leaf(f"{base}/dyn/mix", "f", "Dry/wet mix (parallel compression)", unit="dyn_mix"),
        _leaf(f"{base}/dyn/auto", "i", "Auto time constants on/off", rng=[0, 1]),
        _leaf(f"{base}/dyn/filter/on", "i", "Dyn sidechain filter on/off", rng=[0, 1]),
        _leaf(f"{base}/dyn/filter/type", "i", "Dyn sidechain filter type (0-8)", rng=[0, 8]),
        _leaf(f"{base}/dyn/filter/f", "f", "Dyn sidechain filter frequency", unit="freq"),
    ]


def _insert(base):
    return [
        _leaf(f"{base}/insert/on", "i", "Insert on/off", rng=[0, 1]),
        _leaf(f"{base}/insert/sel", "i", "Insert FX slot", enum=INSERT_SEL),
    ]


def _eq(base, bands, with_mode=False):
    leaves = [_leaf(f"{base}/eq/on", "i", "EQ on/off", rng=[0, 1])]
    if with_mode:
        leaves.append(_leaf(f"{base}/eq/mode", "i", "EQ mode (0=PEQ,1=GEQ,2=TEQ)",
                            rng=[0, 2], verified=True))
    for b in range(1, bands + 1):
        leaves += [
            _leaf(f"{base}/eq/{b}/type", "i", f"EQ band {b} type", enum=EQ_TYPES),
            _leaf(f"{base}/eq/{b}/f", "f", f"EQ band {b} frequency", unit="freq"),
            _leaf(f"{base}/eq/{b}/g", "f", f"EQ band {b} gain", unit="eq_gain"),
            _leaf(f"{base}/eq/{b}/q", "f", f"EQ band {b} Q (width)", unit="eq_q"),
        ]
    return leaves


def _geq(base):
    """Bus/LR graphic EQ, 20Hz..20kHz in 1/3 octave: slots named by freq."""
    slots = ["20", "25", "31.5", "40", "50", "63", "80", "100", "125", "160",
             "200", "250", "315", "400", "500", "630", "800", "1k", "1k25",
             "1k6", "2k", "2k5", "3k15", "4k", "5k", "6k3", "8k", "10k",
             "12k5", "16k", "20k"]
    return [_leaf(f"{base}/geq/{s}", "f", f"GEQ band {s}Hz gain (-15..+15 dB)",
                  unit="eq_gain", verified=True) for s in slots]


def _mix_master(base, with_pan=True, with_lr=False):
    leaves = [
        _leaf(f"{base}/mix/on", "i", "Channel ON (1=unmuted, 0=MUTED). Note inverted vs 'mute'!", rng=[0, 1]),
        _leaf(f"{base}/mix/fader", "f", "Fader level", unit="fader_db"),
    ]
    if with_lr:
        leaves.append(_leaf(f"{base}/mix/lr", "i", "Assign to main LR (1=assigned)", rng=[0, 1]))
    if with_pan:
        leaves.append(_leaf(f"{base}/mix/pan", "f", "Pan/Balance", unit="pan"))
    return leaves


def _mix_sends(base):
    """Send slots 01-06 = Bus 1-6 (monitors/FOH aux), 07-10 = FX 1-4."""
    leaves = []
    for s in range(1, 11):
        tgt = f"Bus {s}" if s <= 6 else f"FX {s - 6}"
        ss = f"{s:02d}"
        leaves.append(_leaf(f"{base}/mix/{ss}/level", "f", f"Send level to {tgt}", unit="fader_db"))
        if s <= 6:
            if s % 2 == 1:
                leaves.append(_leaf(f"{base}/mix/{ss}/pan", "f",
                                    f"Send pan to {tgt} (only when bus {s}/{s+1} stereo-linked)",
                                    unit="pan"))
            leaves.append(_leaf(f"{base}/mix/{ss}/grpon", "i",
                                f"Send to {tgt}: DCA/mute-group inheritance on/off",
                                rng=[0, 1], verified=True))
            leaves.append(_leaf(f"{base}/mix/{ss}/tap", "i",
                                f"Send tap point to {tgt}", enum=TAP_POINTS))
    return leaves


def _grp(base):
    return [
        _leaf(f"{base}/grp/dca", "i", "DCA group assignment bitmask (bit0=DCA1..bit3=DCA4)", rng=[0, 15]),
        _leaf(f"{base}/grp/mute", "i", "Mute group assignment bitmask (bit0=MG1..bit3=MG4)", rng=[0, 15]),
    ]


# --------------------------------------------------------------------------
# Build the tree
# --------------------------------------------------------------------------

def _build() -> list[dict]:
    entries: list[dict] = []

    # ---- Input channels 1-16 ------------------------------------------------
    for section in [
        lambda b: _config(b, "Channel", with_insrc=True),
        _preamp, _gate, _dyn, _insert,
        lambda b: _eq(b, 4),
        lambda b: _mix_master(b, with_pan=True, with_lr=True),
        _mix_sends, _grp,
    ]:
        for leaf in section("/ch/{ch:02d}"):
            leaf["expand"] = {"ch": list(range(1, 17))}
            leaf["category"] = "channel"
            entries.append(leaf)
    for leaf in [
        _leaf("/ch/{ch:02d}/automix/group", "i", "Automix group", enum=AUTOMIX_GROUPS),
        _leaf("/ch/{ch:02d}/automix/weight", "f", "Automix weight", unit="automix_w"),
    ]:
        leaf["expand"] = {"ch": list(range(1, 17))}
        leaf["category"] = "channel"
        entries.append(leaf)

    # ---- Aux/USB return channel (17/18) -------------------------------------
    for section in [
        lambda b: _config(b, "Aux/USB return"),
        lambda b: [_leaf(f"{b}/preamp/invert", "i", "Polarity invert", rng=[0, 1], verified=False)],
        lambda b: _eq(b, 4),
        lambda b: _mix_master(b, with_pan=True, with_lr=True),
        _mix_sends, _grp,
    ]:
        for leaf in section("/rtn/aux"):
            leaf["category"] = "aux_return"
            entries.append(leaf)

    # ---- FX return strips 1-4 ------------------------------------------------
    for section in [
        lambda b: _config(b, "FX return"),
        lambda b: _eq(b, 4),
        lambda b: _mix_master(b, with_pan=True, with_lr=True),
        _mix_sends, _grp,
    ]:
        for leaf in section("/rtn/{fx}"):
            leaf["expand"] = {"fx": [1, 2, 3, 4]}
            leaf["category"] = "fx_return"
            entries.append(leaf)

    # ---- Buses 1-6 -------------------------------------------------------------
    for section in [
        lambda b: _config(b, "Bus"),
        _dyn, _insert,
        lambda b: _eq(b, 6, with_mode=True),
        _geq,
        lambda b: _mix_master(b, with_pan=True),
        _grp,
    ]:
        for leaf in section("/bus/{bus}"):
            leaf["expand"] = {"bus": [1, 2, 3, 4, 5, 6]}
            leaf["category"] = "bus"
            entries.append(leaf)

    # ---- FX sends 1-4 ----------------------------------------------------------
    for section in [
        lambda b: _config(b, "FX send"),
        lambda b: _mix_master(b, with_pan=False),
        _grp,
    ]:
        for leaf in section("/fxsend/{fx}"):
            leaf["expand"] = {"fx": [1, 2, 3, 4]}
            leaf["category"] = "fx_send"
            entries.append(leaf)

    # ---- Main LR ---------------------------------------------------------------
    for section in [
        _dyn, _insert,
        lambda b: _eq(b, 6, with_mode=True),
        _geq,
        lambda b: _mix_master(b, with_pan=True),
    ]:
        for leaf in section("/lr"):
            leaf["category"] = "main_lr"
            entries.append(leaf)

    # ---- FX processors ----------------------------------------------------------
    for leaf in [
        _leaf("/fx/{fx}/type", "i", "FX algorithm type index", enum=FX_TYPES),
    ]:
        leaf["expand"] = {"fx": [1, 2, 3, 4]}
        leaf["category"] = "fx"
        entries.append(leaf)
    for leaf in [
        _leaf("/fx/{fx}/par/{par:02d}", "f",
              "FX parameter (meaning depends on /fx/N/type; normalized 0..1)",
              rng=[0.0, 1.0]),
    ]:
        leaf["expand"] = {"fx": [1, 2, 3, 4], "par": list(range(1, 65))}
        leaf["category"] = "fx"
        entries.append(leaf)

    # ---- Headamps ---------------------------------------------------------------
    for leaf in [
        _leaf("/headamp/{ha:02d}/gain", "f", "Preamp gain (-12..+60 dB; 01-16=XLR inputs, 17/18=aux line-level trim)", unit="headamp"),
        _leaf("/headamp/{ha:02d}/phantom", "i", "48V phantom power on/off", rng=[0, 1]),
    ]:
        leaf["expand"] = {"ha": list(range(1, 25))}
        leaf["category"] = "headamp"
        entries.append(leaf)

    # ---- Config / global ----------------------------------------------------------
    cfg = [
        _leaf("/config/mute/{mg}", "i", "Mute group N master (1=engaged mutes members)", rng=[0, 1]),
        _leaf("/config/chlink/{pair}", "i", "Channel stereo link (1=linked)", rng=[0, 1]),
        _leaf("/config/buslink/{buspair}", "i", "Bus stereo link (1=linked)", rng=[0, 1]),
        _leaf("/config/linkcfg/hadly", "i", "Link preamps in stereo pairs", rng=[0, 1], verified=True),
        _leaf("/config/linkcfg/eq", "i", "Link EQ in stereo pairs", rng=[0, 1]),
        _leaf("/config/linkcfg/dyn", "i", "Link dynamics in stereo pairs", rng=[0, 1]),
        _leaf("/config/linkcfg/fdrmute", "i", "Link fader/mute in stereo pairs", rng=[0, 1]),
        _leaf("/config/solo/level", "f", "Solo bus level", unit="fader_db"),
        _leaf("/config/solo/source", "i", "Monitor/solo source", enum=SOLO_SOURCES, verified=True),
        _leaf("/config/solo/sourcetrim", "f", "Solo source trim", unit="solo_trim"),
        _leaf("/config/solo/chmode", "i", "Channel solo mode (0=PFL,1=AFL)", rng=[0, 1]),
        _leaf("/config/solo/busmode", "i", "Bus solo mode (0=PFL,1=AFL)", rng=[0, 1]),
        _leaf("/config/solo/dimatt", "f", "Dim attenuation", unit="solo_dim"),
        _leaf("/config/solo/dim", "i", "Dim on/off", rng=[0, 1]),
        _leaf("/config/solo/mono", "i", "Solo mono on/off", rng=[0, 1]),
        _leaf("/config/solo/delay", "i", "Solo delay on/off", rng=[0, 1]),
        _leaf("/config/solo/delaytime", "f", "Solo delay time (0.3..500 ms)", verified=True),
        _leaf("/config/solo/exclusive", "i", "Exclusive solo (last pressed wins)", rng=[0, 1], verified=True),
        _leaf("/config/amixenable/X", "i", "Automix group X enable", rng=[0, 1], verified=True),
        _leaf("/config/amixenable/Y", "i", "Automix group Y enable", rng=[0, 1], verified=True),
    ]
    for leaf in cfg:
        if "{mg}" in leaf["path"]:
            leaf["expand"] = {"mg": [1, 2, 3, 4]}
        if "{pair}" in leaf["path"]:
            leaf["expand"] = {"pair": ["1-2", "3-4", "5-6", "7-8", "9-10", "11-12", "13-14", "15-16"]}
        if "{buspair}" in leaf["path"]:
            leaf["expand"] = {"buspair": ["1-2", "3-4", "5-6"]}
        leaf["category"] = "config"
        entries.append(leaf)

    # ---- DCA groups (XAir DCAs are virtual: assignment via /ch/N/grp/dca) --------
    for leaf in [
        _leaf("/dca/{dca}/on", "i", "DCA N on (1=unmuted)", rng=[0, 1]),
        _leaf("/dca/{dca}/fader", "f", "DCA N fader", unit="fader_db"),
        _leaf("/dca/{dca}/config/name", "s", "DCA N name"),
        _leaf("/dca/{dca}/config/color", "i", "DCA N color", enum=COLORS),
    ]:
        leaf["expand"] = {"dca": [1, 2, 3, 4]}
        leaf["category"] = "dca"
        entries.append(leaf)

    # ---- Snapshots -----------------------------------------------------------------
    snap = [
        _leaf("/-snap/{snap:02d}/name", "s", "Snapshot slot name (1-64)"),
        _leaf("/-snap/save", "i", "SAVE current state to snapshot slot N (send int 1-64). ACTION.", rng=[1, 64]),
        _leaf("/-snap/load", "i", "LOAD snapshot slot N (send int 1-64). ACTION - changes everything at once.", rng=[1, 64]),
        _leaf("/-snap/index", "i", "Last loaded snapshot index", readonly=True, verified=False),
    ]
    for leaf in snap:
        if "{snap" in leaf["path"]:
            leaf["expand"] = {"snap": list(range(1, 65))}
        leaf["category"] = "snapshot"
        entries.append(leaf)

    # ---- Status / prefs (read-mostly) ------------------------------------------------
    stat = [
        _leaf("/-stat/solosw/{sw:02d}", "i", "Solo switch per strip (01-16=ch,17=aux,18-21=fxrtn,22-27=bus,28-31=fxsend? 32? verify order)", rng=[0, 1], verified=False),
        _leaf("/-stat/solo", "i", "Any solo active (read-only)", readonly=True),
        _leaf("/-prefs/lan/addr", "s", "Mixer IP address (static mode)", verified=False),
        _leaf("/-prefs/lan/mode", "i", "LAN mode (0=DHCP,1=static?)", verified=False),
        _leaf("/-prefs/name", "s", "Mixer device name", verified=False),
    ]
    for leaf in stat:
        if "{sw" in leaf["path"]:
            leaf["expand"] = {"sw": list(range(1, 40))}
        leaf["category"] = "status"
        entries.append(leaf)

    # ---- Special commands (not get/set parameters) -------------------------------------
    for leaf in [
        _leaf("/xinfo", None, "Query mixer info: replies IP, name, model, firmware. Send with no args.", readonly=True),
        _leaf("/info", None, "Query server version info", readonly=True),
        _leaf("/status", None, "Query mixer status", readonly=True),
        _leaf("/xremote", None, "Subscribe to ALL parameter changes for 10s (resend to keep alive)"),
        _leaf("/unsubscribe", None, "Cancel subscriptions"),
        _leaf("/renew", None, "Renew subscription (optionally with alias arg)"),
        _leaf("/node", "s", "Dump a config node as text, e.g. arg 'ch/01/config'. THE discovery/hack tool."),
        _leaf("/meters", "s", "Subscribe to meter blob, arg '/meters/0'..'/meters/8' (see metering docs)"),
    ]:
        leaf["category"] = "command"
        entries.append(leaf)

    return entries


ENTRIES: list[dict] = _build()


# --------------------------------------------------------------------------
# Expansion & search helpers
# --------------------------------------------------------------------------

def expand_entry(entry: dict) -> Iterator[str]:
    """Yield every concrete OSC address for a patterned entry."""
    path = entry["path"]
    expand = entry.get("expand")
    if not expand:
        yield path
        return
    keys = list(expand.keys())

    def rec(p: str, idx: int) -> Iterator[str]:
        if idx == len(keys):
            yield p
            return
        k = keys[idx]
        for v in expand[k]:
            if isinstance(v, int):
                np = re.sub(r"\{%s(:[^}]*)?\}" % k,
                            lambda m: format(v, m.group(1)[1:] if m.group(1) else ""), p)
            else:
                np = p.replace("{%s}" % k, str(v))
            yield from rec(np, idx + 1)

    yield from rec(path, 0)


def find_entry(address: str) -> dict | None:
    """Match a concrete OSC address back to its map entry."""
    for entry in ENTRIES:
        pattern = re.sub(r"\{[a-z]+(:[^}]*)?\}", r"__NUM__", entry["path"])
        pattern = re.escape(pattern).replace("__NUM__", r"[\w\-]+")
        if re.fullmatch(pattern, address):
            return entry
    return None


def search(query: str, category: str | None = None, limit: int = 40) -> list[dict]:
    """Keyword search over paths + descriptions. Query terms are ANDed."""
    terms = [t.lower() for t in query.split() if t]
    out = []
    for e in ENTRIES:
        if category and e["category"] != category:
            continue
        hay = (e["path"] + " " + e["desc"] + " " + e["category"]).lower()
        if all(t in hay for t in terms):
            out.append(e)
            if len(out) >= limit:
                break
    return out


CATEGORIES = sorted({e["category"] for e in ENTRIES})


def stats() -> dict:
    total = sum(len(list(expand_entry(e))) for e in ENTRIES)
    return {"patterned_entries": len(ENTRIES), "concrete_addresses": total,
            "categories": CATEGORIES}
