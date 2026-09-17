# TOOL_INVENTORY

## RETURN_CONTRACT
All 33 Python tools return `str`; most success strings contain JSON, some contain native text or a help/error sentence. FastMCP output schema wraps a string as `result`; do not assume every result parses as JSON. Exact input/output schemas and return expressions are retained in the JSON map. Exceptions may propagate as MCP tool errors; many MS tools instead return help strings.

## SAFETY_TABLE
| Tool | Class | Effects |
| --- | --- | --- |
| xair_discover | diagnostic | Broadcast discovery packets; no audio parameter write. |
| xair_connect | diagnostic | Replaces server client/target; does not change mixer parameters. |
| xair_info | read-only | Reads only; generic addresses still require an allowlist. |
| xair_map_search | read-only | Reads only; generic addresses still require an allowlist. |
| xair_map_describe | read-only | Reads only; generic addresses still require an allowlist. |
| xair_get | read-only | Reads only; generic addresses still require an allowlist. |
| xair_set | write-capable | Mixer/app writes possible. |
| xair_batch_set | write-capable | Mixer/app writes possible. |
| xair_node_dump | read-only | Reads only; generic addresses still require an allowlist. |
| xair_routing_overview | read-only | Reads only; generic addresses still require an allowlist. |
| xair_channel_overview | read-only | Reads only; generic addresses still require an allowlist. |
| xair_input_config | read-only | Reads only; generic addresses still require an allowlist. |
| xair_fader | write-capable | Mixer/app writes possible. |
| xair_mute | write-capable | Mixer/app writes possible. |
| xair_mute_group | write-capable | Mixer/app writes possible. |
| xair_send_level | write-capable | Mixer/app writes possible. |
| xair_channel_detail | read-only | Reads only; generic addresses still require an allowlist. |
| xair_eq_band | write-capable | Mixer/app writes possible. |
| xair_headamp | write-capable | Mixer/app writes possible. |
| xair_fx | write-capable | Read with slot only; write with fx_type or params. |
| xair_snapshot_list | read-only | Reads only; generic addresses still require an allowlist. |
| xair_snapshot_save | write-capable | Mixer/app writes possible. |
| xair_snapshot_load | write-capable | Mixer/app writes possible. |
| xair_backup_dump | diagnostic | Queries mixer; creates local backup file. |
| xair_meters | diagnostic | Creates telemetry subscription; no audio parameter write. |
| xair_macro_list | read-only | Reads only; generic addresses still require an allowlist. |
| xair_macro_run | write-capable | Mixer/app writes possible. |
| xair_macro_save | write-capable | Writes local presets JSON; no immediate mixer change. |
| ms_app_state | read-only | Reads only; generic addresses still require an allowlist. |
| ms_data_tree | read-only | Reads only; generic addresses still require an allowlist. |
| ms_data_value | read-only | Reads only; generic addresses still require an allowlist. |
| ms_api | write-capable | Arbitrary endpoint; GET is not sufficient to establish safety. |
| ms_value | write-capable | Read when set_to omitted; write otherwise; legacy path currently rejected. |

## xair_discover
Source: `xair_mcp/server.py:149`.

Broadcast /xinfo on UDP 10024 and list every X-Air mixer that answers.

    Returns JSON list of {ip, name, model, firmware}. Use xair_connect with the
    IP afterwards. If nothing is found: mixer off, different subnet/VLAN, or
    an AP client-isolation issue.


### PARAMETERS
```json
{
  "properties": {
    "wait_seconds": {
      "default": 2.0,
      "title": "Wait Seconds",
      "type": "number"
    }
  },
  "title": "xair_discoverArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(found, indent=2)
found
'No X-Air mixers replied to broadcast. Check: mixer powered on, same network/subnet as this Mac, no VLAN/client isolation. You can still connect directly with xair_connect if you know the IP.'
```

## xair_connect
Source: `xair_mcp/server.py:187`.

Set the mixer IP and verify the connection via /xinfo.

    Args: host - IP address of the XAir18 (e.g. '192.168.1.50').
    Returns mixer info on success.


### PARAMETERS
```json
{
  "properties": {
    "host": {
      "title": "Host",
      "type": "string"
    }
  },
  "required": [
    "host"
  ],
  "title": "xair_connectArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'connected': True, 'host': host, 'xinfo': info})
```

## xair_info
Source: `xair_mcp/server.py:202`.

Get mixer identity (/xinfo) and status (/status) from the connected XAir18.

### PARAMETERS
```json
{
  "properties": {},
  "title": "xair_infoArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'host': c.host, 'xinfo': info, 'status': status})
```

## xair_map_search
Source: `xair_mcp/server.py:220`.

Search the complete XAir18 OSC command map by keywords.

    THE starting point for any parameter you don't know the address of.
    Query terms are ANDed against path + description, e.g. 'gate threshold',
    'phantom', 'snapshot load', 'fx type'.
    Categories: channel, aux_return, fx_return, bus, fx_send, main_lr, fx,
    headamp, config, dca, snapshot, status, command.
    Returns patterned entries; {ch:02d} etc. expand per 'expand' ranges
    (addresses are 1-based zero-padded, e.g. /ch/05/...).


### PARAMETERS
```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "category": {
      "default": "",
      "title": "Category",
      "type": "string"
    },
    "limit": {
      "default": 30,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "xair_map_searchArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'count': len(res), 'entries': slim}, indent=1)
f"No entries match '{query}'. Try broader terms, or use xair_node_dump to explore the live mixer tree. Stats: {json.dumps(osc_map.stats())}"
```

## xair_map_describe
Source: `xair_mcp/server.py:242`.

Explain a concrete OSC address: type, range/enum, unit conversion law,
    verified flag. E.g. '/ch/05/dyn/thr'. Also lists all available unit names.


### PARAMETERS
```json
{
  "properties": {
    "address": {
      "title": "Address",
      "type": "string"
    }
  },
  "required": [
    "address"
  ],
  "title": "xair_map_describeArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(out, indent=1, default=str)
f"'{address}' is not in the map (may still exist on the mixer - try xair_get or xair_node_dump). Use xair_map_search to browse."
```

## xair_get
Source: `xair_mcp/server.py:265`.

Read any OSC parameter from the mixer, e.g. '/ch/05/mix/fader'.

    Returns raw wire value plus human units (dB, Hz, ...) when the map knows
    the conversion. Works for unmapped addresses too.


### PARAMETERS
```json
{
  "properties": {
    "address": {
      "title": "Address",
      "type": "string"
    }
  },
  "required": [
    "address"
  ],
  "title": "xair_getArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(_fmt_value(address, args))
```

## xair_set
Source: `xair_mcp/server.py:279`.

Set any OSC parameter on the mixer and read back for confirmation.

    Args:
        address: OSC address, e.g. '/ch/05/mix/fader'
        value: the value. If `unit` given (or the map defines one for a float
               param), human units are converted to wire format automatically:
               e.g. address='/ch/05/mix/fader', value=-6, unit='fader_db'.
        unit: '', a unit name from xair_map_describe, or 'raw' to skip conversion.
    Returns the confirmed value after setting.


### PARAMETERS
```json
{
  "properties": {
    "address": {
      "title": "Address",
      "type": "string"
    },
    "value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "integer"
        },
        {
          "type": "string"
        }
      ],
      "title": "Value"
    },
    "unit": {
      "default": "",
      "title": "Unit",
      "type": "string"
    }
  },
  "required": [
    "address",
    "value"
  ],
  "title": "xair_setArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(out)
```

## xair_batch_set
Source: `xair_mcp/server.py:302`.

Fire a list of OSC sets in order (fast, ~1ms apart).

    Each operation: {"address": str, "value": num|str, "unit": optional str}.
    Set confirm_each=true to read back every value (slower).


### PARAMETERS
```json
{
  "properties": {
    "operations": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Operations",
      "type": "array"
    },
    "confirm_each": {
      "default": false,
      "title": "Confirm Each",
      "type": "boolean"
    }
  },
  "required": [
    "operations"
  ],
  "title": "xair_batch_setArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'count': len(results), 'results': results})
```

## xair_node_dump
Source: `xair_mcp/server.py:326`.

Dump a node of the mixer's config tree as native console text via /node.

    THE tool for exploring/verifying the real parameter tree ("hacking").
    Examples: 'ch/01/config', 'ch/05/dyn', 'lr/eq', 'bus/1', '-snap/01',
    'config/solo', 'fx/1'. Returns the raw line(s) with current values in order.


### PARAMETERS
```json
{
  "properties": {
    "node": {
      "title": "Node",
      "type": "string"
    }
  },
  "required": [
    "node"
  ],
  "title": "xair_node_dumpArguments",
  "type": "object"
}
```

### RETURNS
```python
text or f"(empty reply for node '{node}')"
```

## xair_routing_overview
Source: `xair_mcp/server.py:341`.

Read the XR18's global USB, Aux, Main, and Monitor routing nodes.

    These native /routing nodes are separate from Mixing Station's
    /console/data/paths tree, so this is the programmatic equivalent of the
    Routing -> Outputs pages. It only reads state.


### PARAMETERS
```json
{
  "properties": {},
  "title": "xair_routing_overviewArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _run(read), indent=2)
result
```

## xair_channel_overview
Source: `xair_mcp/server.py:385`.

Snapshot of the whole board: every strip's name, color, fader (dB),
    mute state and LR assignment. Use this FIRST to map human names
    ('lead vox') to strip numbers. Covers ch1-16, aux, fx returns, buses,
    fx sends, LR.


### PARAMETERS
```json
{
  "properties": {},
  "title": "xair_channel_overviewArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _run(read), indent=1)
rows
```

## xair_input_config
Source: `xair_mcp/server.py:429`.

Read the configured source for one or all XR18 input strips.

    This reports the Mixing Station input page's three decisive fields:
    analog source, USB source, and the active A/D-versus-USB selector. It also
    preserves the raw XR18 config tuple. It is distinct from global USB-send
    routing: it answers what feeds each channel strip.


### PARAMETERS
```json
{
  "properties": {
    "channel": {
      "default": "",
      "title": "Channel",
      "type": "string"
    }
  },
  "title": "xair_input_configArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await read(), indent=1)
rows
'Error: channel must be ch1-ch16.'
```

## xair_fader
Source: `xair_mcp/server.py:501`.

Set any strip's fader in dB (-90..+10; <=-90 = -inf/off).

    strip: 'ch1'..'ch16', 'aux', 'rtn1-4', 'bus1-6', 'fxsend1-4', 'dca1-4', 'lr'.
    For named channels ('lead vox'), first find the number via xair_channel_overview.


### PARAMETERS
```json
{
  "properties": {
    "strip": {
      "title": "Strip",
      "type": "string"
    },
    "level_db": {
      "title": "Level Db",
      "type": "number"
    }
  },
  "required": [
    "strip",
    "level_db"
  ],
  "title": "xair_faderArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'strip': base, 'fader_db': round(conv.fader_to_db(args[0]), 1)})
```

## xair_mute
Source: `xair_mcp/server.py:516`.

Mute (true) or unmute (false) a strip. Same strip syntax as xair_fader.
    Note: wire format is inverted ('on': 1=unmuted); this tool handles that.


### PARAMETERS
```json
{
  "properties": {
    "strip": {
      "title": "Strip",
      "type": "string"
    },
    "muted": {
      "title": "Muted",
      "type": "boolean"
    }
  },
  "required": [
    "strip",
    "muted"
  ],
  "title": "xair_muteArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'strip': base, 'muted': not bool(args[0])})
```

## xair_mute_group
Source: `xair_mcp/server.py:529`.

Engage (true) or release (false) mute group 1-4. Engaging mutes all members.

### PARAMETERS
```json
{
  "properties": {
    "group": {
      "title": "Group",
      "type": "integer"
    },
    "engaged": {
      "title": "Engaged",
      "type": "boolean"
    }
  },
  "required": [
    "group",
    "engaged"
  ],
  "title": "xair_mute_groupArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'mute_group': group, 'engaged': bool(args[0])})
'Error: mute group must be 1-4.'
```

## xair_send_level
Source: `xair_mcp/server.py:541`.

Set how much of a channel goes to a bus (monitor) or FX.

    channel: 'ch1'..'ch16', 'aux', 'rtn1-4'.
    destination: 'bus1'..'bus6' (monitor/aux mixes) or 'fx1'..'fx4'.
    level_db: -90..+10.
    E.g. 'more vocal in the drummer's wedge on bus 2' -> channel='ch5',
    destination='bus2', level_db=-5.


### PARAMETERS
```json
{
  "properties": {
    "channel": {
      "title": "Channel",
      "type": "string"
    },
    "destination": {
      "title": "Destination",
      "type": "string"
    },
    "level_db": {
      "title": "Level Db",
      "type": "number"
    }
  },
  "required": [
    "channel",
    "destination",
    "level_db"
  ],
  "title": "xair_send_levelArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'address': addr, 'level_db': round(conv.fader_to_db(args[0]), 1)})
'Error: destination must be bus1-6 or fx1-4.'
```

## xair_channel_detail
Source: `xair_mcp/server.py:569`.

Read a strip's full processing chain via /node dumps: config, preamp/
    headamp, gate, dynamics, insert, EQ, mix, sends. Native console text format
    (values in order as documented by the map).


### PARAMETERS
```json
{
  "properties": {
    "strip": {
      "title": "Strip",
      "type": "string"
    }
  },
  "required": [
    "strip"
  ],
  "title": "xair_channel_detailArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _run(read), indent=1)
out
```

## xair_eq_band
Source: `xair_mcp/server.py:599`.

Adjust one parametric EQ band on any strip.

    strip: same syntax as xair_fader. band: 1-4 on channels, 1-6 on buses/LR.
    Provide any of freq_hz (20-20000), gain_db (-15..+15), q (0.3-10),
    band_type ('LCut','LShv','PEQ','VEQ','HShv','HCut').
    E.g. 'cut 3k on the vocal by 4dB' -> strip='ch5', band=3, freq_hz=3000,
    gain_db=-4.


### PARAMETERS
```json
{
  "properties": {
    "strip": {
      "title": "Strip",
      "type": "string"
    },
    "band": {
      "title": "Band",
      "type": "integer"
    },
    "freq_hz": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Freq Hz"
    },
    "gain_db": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Gain Db"
    },
    "q": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Q"
    },
    "band_type": {
      "default": "",
      "title": "Band Type",
      "type": "string"
    }
  },
  "required": [
    "strip",
    "band"
  ],
  "title": "xair_eq_bandArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(out, indent=1)
'Error: provide at least one of band_type/freq_hz/gain_db/q.'
f'Error: band_type must be one of {osc_map.EQ_TYPES}'
```

## xair_headamp
Source: `xair_mcp/server.py:634`.

Set preamp gain (-12..+60 dB) and/or 48V phantom for input 1-16.

    CAUTION: toggling phantom while a condenser mic is hot can pop the PA;
    gain changes affect everything post-preamp. Confirm with the user before
    large changes during a show.


### PARAMETERS
```json
{
  "properties": {
    "channel": {
      "title": "Channel",
      "type": "integer"
    },
    "gain_db": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Gain Db"
    },
    "phantom": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Phantom"
    }
  },
  "required": [
    "channel"
  ],
  "title": "xair_headampArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'channel': channel, **out}) if out else 'Error: provide gain_db and/or phantom.'
'Error: channel must be 1-16 (physical XLR inputs).'
```

## xair_fx
Source: `xair_mcp/server.py:661`.

Inspect or modify FX slot 1-4.

    No args beyond slot: returns current type + all parameter values.
    fx_type: set algorithm by name from the FX_TYPES list (see xair_map_search
    'fx type'). params: {"01": 0.5, ...} normalized 0..1 (param meanings depend
    on the algorithm - dump first, tweak, re-check).


### PARAMETERS
```json
{
  "properties": {
    "slot": {
      "title": "Slot",
      "type": "integer"
    },
    "fx_type": {
      "default": "",
      "title": "Fx Type",
      "type": "string"
    },
    "params": {
      "anyOf": [
        {
          "additionalProperties": {
            "type": "number"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Params"
    }
  },
  "required": [
    "slot"
  ],
  "title": "xair_fxArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(out, indent=1)
'Error: slot must be 1-4.'
f'Error: unknown fx_type. Known: {osc_map.FX_TYPES}'
```

## xair_snapshot_list
Source: `xair_mcp/server.py:698`.

List all 64 snapshot slots with names (empty names = unused slots).
    NOTE: slot 64 may hold Mixing Station's bus password protection - avoid
    overwriting it if bus passwords are in use.


### PARAMETERS
```json
{
  "properties": {},
  "title": "xair_snapshot_listArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'used_slots': rows, 'note': '64 slots total; only named/used shown'})
rows
```

## xair_snapshot_save
Source: `xair_mcp/server.py:723`.

Save the mixer's CURRENT state into snapshot slot 1-64 (overwrites!).
    Optionally set the slot name. Avoid slot 64 if Mixing Station bus
    passwords are used.


### PARAMETERS
```json
{
  "properties": {
    "slot": {
      "title": "Slot",
      "type": "integer"
    },
    "name": {
      "default": "",
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "slot"
  ],
  "title": "xair_snapshot_saveArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'saved_to_slot': slot, 'name': stored})
'Error: slot must be 1-64.'
```

## xair_snapshot_load
Source: `xair_mcp/server.py:743`.

LOAD snapshot slot 1-64. DANGER: instantly changes the entire mixer
    state (faders, mutes, routing). Confirm with the user before doing this
    during a live show.


### PARAMETERS
```json
{
  "properties": {
    "slot": {
      "title": "Slot",
      "type": "integer"
    }
  },
  "required": [
    "slot"
  ],
  "title": "xair_snapshot_loadArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'loaded_slot': slot, 'name': name, 'note': 'Full mixer state replaced.'})
'Error: slot must be 1-64.'
```

## xair_backup_dump
Source: `xair_mcp/server.py:778`.

Dump the ENTIRE mixer state (all channels/buses/fx/config) via /node
    to a timestamped text file in the backups/ folder next to the server.
    The format matches the console's native scene lines - great for
    versioning gigs ('Neon Blonde @ Riverside 2026-07-04') and diffing.
    Takes ~30-60s.


### PARAMETERS
```json
{
  "properties": {
    "label": {
      "default": "",
      "title": "Label",
      "type": "string"
    }
  },
  "title": "xair_backup_dumpArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'file': str(fp), 'nodes_ok': ok, 'nodes_failed': fail})
(ok, fail)
```

## xair_meters
Source: `xair_mcp/server.py:826`.

Sample live levels for ~duration and return peak+mean dB per slot.

    meter_id 1 = all strips (in1-16, aux, fx returns, buses, fx sends, LR, mon).
    Other ids (0-8) return raw unlabeled arrays (input/dynamics/rta banks).
    Use for questions like 'is the kick clipping?' (ch levels near 0 dBFS clip;
    good gig level peaks around -18..-9).


### PARAMETERS
```json
{
  "properties": {
    "meter_id": {
      "default": 1,
      "title": "Meter Id",
      "type": "integer"
    },
    "duration_seconds": {
      "default": 1.0,
      "title": "Duration Seconds",
      "type": "number"
    }
  },
  "title": "xair_metersArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'meter': addr, 'frames': len(frames), 'values': data})
frames
'No meter data received. The mixer streams meters for ~10s per subscription; check connection with xair_info and retry.'
```

## xair_macro_list
Source: `xair_mcp/server.py:890`.

List saved band macros (break_music, kill_fx, mute_all_inputs, ...)
    with descriptions and operation counts.


### PARAMETERS
```json
{
  "properties": {},
  "title": "xair_macro_listArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'presets_file': str(_PRESETS_PATH), 'macros': out}, indent=1)
```

## xair_macro_run
Source: `xair_mcp/server.py:904`.

Execute a saved macro by name (see xair_macro_list). Runs all its OSC
    operations in order against the mixer.


### PARAMETERS
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "title": "xair_macro_runArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'ran': name, 'operations': len(ops), 'description': macro.get('description', '')})
f"Error: no macro '{name}'. Available: {sorted(p.get('macros', {}))}"
```

## xair_macro_save
Source: `xair_mcp/server.py:925`.

Create or overwrite a named macro in the presets file.

    operations: [{"address": "/ch/05/mix/on", "value": 0, "unit": optional,
    "repeat_ch": optional [first,last] to repeat over channels}].
    Tip: build the ops with xair_map_search, test with xair_batch_set, then save.


### PARAMETERS
```json
{
  "properties": {
    "name": {
      "title": "Name",
      "type": "string"
    },
    "description": {
      "title": "Description",
      "type": "string"
    },
    "operations": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Operations",
      "type": "array"
    }
  },
  "required": [
    "name",
    "description",
    "operations"
  ],
  "title": "xair_macro_saveArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps({'saved': name, 'operations': len(operations), 'file': str(_PRESETS_PATH)})
```

## ms_app_state
Source: `xair_mcp/server.py:950`.

Get the Mixing Station desktop app's state (connection, current mixer).
    Requires the desktop app running with its REST API enabled
    (app settings -> APIs). Set env MS_API_URL if not on port 8080.


### PARAMETERS
```json
{
  "properties": {},
  "title": "ms_app_stateArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _ms.app_state(), indent=1, default=str)
connection_help(e, _ms.base_url)
```

## ms_data_tree
Source: `xair_mcp/server.py:964`.

Read Mixing Station's complete live console-data path tree.

    This uses the HTTP REST endpoint directly, not the WebSocket passthrough.
    It is read-only and is intended for discovering valid data paths before
    inspecting routing or other console state.


### PARAMETERS
```json
{
  "properties": {},
  "title": "ms_data_treeArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _ms.data_paths(), indent=1, default=str)
connection_help(e, _ms.base_url)
```

## ms_data_value
Source: `xair_mcp/server.py:980`.

Read one live Mixing Station console-data value via REST.

    Use dotted paths from ms_data_tree, for example
    ``ch.0.routing.srcCfg.0``. This tool cannot write values.


### PARAMETERS
```json
{
  "properties": {
    "data_path": {
      "title": "Data Path",
      "type": "string"
    },
    "fmt": {
      "default": "val",
      "title": "Fmt",
      "type": "string"
    }
  },
  "required": [
    "data_path"
  ],
  "title": "ms_data_valueArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _ms.data_value_rest(data_path, fmt), indent=1, default=str)
connection_help(e, _ms.base_url)
```

## ms_api
Source: `xair_mcp/server.py:996`.

Call ANY Mixing Station WebSocket-API endpoint: app control, console
    data, subscriptions. E.g. path='/console/data/val/ch.0.mix.lvl' (NOTE:
    Mixing Station data paths are 0-BASED: ch.0 = channel 1!).
    Open http://localhost:8080 for the interactive API explorer listing all
    endpoints of the connected mixer. body_json: JSON string for POST bodies.


### PARAMETERS
```json
{
  "properties": {
    "path": {
      "title": "Path",
      "type": "string"
    },
    "method": {
      "default": "GET",
      "title": "Method",
      "type": "string"
    },
    "body_json": {
      "default": "",
      "title": "Body Json",
      "type": "string"
    }
  },
  "required": [
    "path"
  ],
  "title": "ms_apiArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(result, indent=1, default=str)
connection_help(e, _ms.base_url)
```

## ms_value
Source: `xair_mcp/server.py:1014`.

Read or write a console value through Mixing Station's data model.

    data_path example: 'ch.0.mix.lvl' (0-based channel index!). fmt: 'val'
    (plain, e.g. dB) or 'norm' (0..1). Leave set_to empty to read.
    Useful when you want Mixing Station's UI to reflect/log the change, or for
    MS-only features; otherwise prefer the direct xair_* tools.


### PARAMETERS
```json
{
  "properties": {
    "data_path": {
      "title": "Data Path",
      "type": "string"
    },
    "set_to": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Set To"
    },
    "fmt": {
      "default": "val",
      "title": "Fmt",
      "type": "string"
    }
  },
  "required": [
    "data_path"
  ],
  "title": "ms_valueArguments",
  "type": "object"
}
```

### RETURNS
```python
json.dumps(await _ms.set_value(data_path, set_to, fmt), default=str)
json.dumps(await _ms.get_value(data_path, fmt), default=str)
connection_help(e, _ms.base_url)
```
