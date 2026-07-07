"""Value conversions for Behringer X-Air OSC parameters.

The mixer stores almost every continuous parameter as a float 0.0-1.0.
These functions convert between human units (dB, Hz, ms, etc.) and the
normalized floats, using the scaling laws documented in Patrick-Gilles
Maillot's "Unofficial X-Air OSC" protocol notes (same laws as X32).
"""
from __future__ import annotations

import math

# ---------------------------------------------------------------------------
# Fader law (channels, buses, sends, LR): piecewise linear in dB
# ---------------------------------------------------------------------------

def fader_to_db(f: float) -> float:
    """Normalized fader position 0..1 -> dB (-inf..+10)."""
    f = max(0.0, min(1.0, f))
    if f >= 0.5:
        return f * 40.0 - 30.0        # -10 .. +10
    if f >= 0.25:
        return f * 80.0 - 50.0        # -30 .. -10
    if f >= 0.0625:
        return f * 160.0 - 70.0       # -60 .. -30
    if f > 0.0:
        return f * 480.0 - 90.0       # -90 .. -60
    return float("-inf")


def db_to_fader(db: float) -> float:
    """dB -> normalized fader position 0..1. Accepts -inf / <=-90 as 0."""
    if db == float("-inf") or db <= -90.0:
        return 0.0
    if db >= -10.0:
        return min(1.0, (db + 30.0) / 40.0)
    if db >= -30.0:
        return (db + 50.0) / 80.0
    if db >= -60.0:
        return (db + 70.0) / 160.0
    return (db + 90.0) / 480.0


# ---------------------------------------------------------------------------
# Generic linear / log scalings
# ---------------------------------------------------------------------------

def lin_to_norm(value: float, lo: float, hi: float) -> float:
    return max(0.0, min(1.0, (value - lo) / (hi - lo)))


def norm_to_lin(f: float, lo: float, hi: float) -> float:
    return lo + max(0.0, min(1.0, f)) * (hi - lo)


def log_to_norm(value: float, lo: float, hi: float) -> float:
    value = max(lo, min(hi, value))
    return math.log(value / lo) / math.log(hi / lo)


def norm_to_log(f: float, lo: float, hi: float) -> float:
    f = max(0.0, min(1.0, f))
    return lo * math.exp(f * math.log(hi / lo))


# ---------------------------------------------------------------------------
# Named unit helpers (used by the units table in osc_map)
# ---------------------------------------------------------------------------

def freq_to_norm(hz: float, lo: float = 20.0, hi: float = 20000.0) -> float:
    return log_to_norm(hz, lo, hi)


def norm_to_freq(f: float, lo: float = 20.0, hi: float = 20000.0) -> float:
    return norm_to_log(f, lo, hi)


def headamp_gain_to_norm(db: float) -> float:
    """XR18 preamp gain: -12..+60 dB, linear, 144 steps of 0.5 dB."""
    return lin_to_norm(db, -12.0, 60.0)


def norm_to_headamp_gain(f: float) -> float:
    return norm_to_lin(f, -12.0, 60.0)


# Ratio enum used by the compressor
DYN_RATIOS = [1.1, 1.3, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 10.0, 20.0, 100.0]


UNIT_CONVERTERS = {
    # unit-name: (human->norm, norm->human, description)
    "fader_db":   (db_to_fader, fader_to_db, "Fader level in dB (-90..+10, -inf=off)"),
    "freq":       (lambda v: freq_to_norm(v), lambda f: norm_to_freq(f), "Frequency in Hz (20..20k, log)"),
    "freq_hpf":   (lambda v: freq_to_norm(v, 20, 400), lambda f: norm_to_freq(f, 20, 400), "Low-cut frequency Hz (20..400, log)"),
    "eq_gain":    (lambda v: lin_to_norm(v, -15, 15), lambda f: norm_to_lin(f, -15, 15), "EQ gain dB (-15..+15)"),
    "eq_q":       (lambda v: 1.0 - log_to_norm(v, 0.3, 10.0), lambda f: norm_to_log(1.0 - f, 0.3, 10.0), "EQ Q (0.3..10, log, inverted)"),
    "gate_thr":   (lambda v: lin_to_norm(v, -80, 0), lambda f: norm_to_lin(f, -80, 0), "Gate threshold dB (-80..0)"),
    "gate_range": (lambda v: lin_to_norm(v, 3, 60), lambda f: norm_to_lin(f, 3, 60), "Gate range dB (3..60)"),
    "dyn_thr":    (lambda v: lin_to_norm(v, -60, 0), lambda f: norm_to_lin(f, -60, 0), "Comp threshold dB (-60..0)"),
    "dyn_knee":   (lambda v: lin_to_norm(v, 0, 5), lambda f: norm_to_lin(f, 0, 5), "Comp knee (0..5)"),
    "dyn_mgain":  (lambda v: lin_to_norm(v, 0, 24), lambda f: norm_to_lin(f, 0, 24), "Makeup gain dB (0..24)"),
    "dyn_mix":    (lambda v: lin_to_norm(v, 0, 100), lambda f: norm_to_lin(f, 0, 100), "Dry/wet mix % (0..100)"),
    "attack":     (lambda v: lin_to_norm(v, 0, 120), lambda f: norm_to_lin(f, 0, 120), "Attack ms (0..120, linear)"),
    "hold":       (lambda v: log_to_norm(max(v, 0.02), 0.02, 2000), lambda f: norm_to_log(f, 0.02, 2000), "Hold ms (0.02..2000, log)"),
    "release":    (lambda v: log_to_norm(max(v, 5), 5, 4000), lambda f: norm_to_log(f, 5, 4000), "Release ms (5..4000, log)"),
    "pan":        (lambda v: lin_to_norm(v, -100, 100), lambda f: norm_to_lin(f, -100, 100), "Pan (-100=L .. +100=R)"),
    "headamp":    (headamp_gain_to_norm, norm_to_headamp_gain, "Preamp gain dB (-12..+60)"),
    "automix_w":  (lambda v: lin_to_norm(v, -12, 12), lambda f: norm_to_lin(f, -12, 12), "Automix weight dB (-12..+12)"),
    "solo_dim":   (lambda v: lin_to_norm(v, -40, 0), lambda f: norm_to_lin(f, -40, 0), "Dim attenuation dB (-40..0)"),
    "solo_trim":  (lambda v: lin_to_norm(v, -18, 18), lambda f: norm_to_lin(f, -18, 18), "Solo source trim dB (-18..+18)"),
}


def human_to_norm(unit: str, value: float) -> float:
    if unit not in UNIT_CONVERTERS:
        raise ValueError(f"Unknown unit '{unit}'. Known: {sorted(UNIT_CONVERTERS)}")
    return UNIT_CONVERTERS[unit][0](value)


def norm_to_human(unit: str, f: float) -> float:
    if unit not in UNIT_CONVERTERS:
        raise ValueError(f"Unknown unit '{unit}'. Known: {sorted(UNIT_CONVERTERS)}")
    return UNIT_CONVERTERS[unit][1](f)
