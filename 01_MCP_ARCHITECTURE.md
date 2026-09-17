# MCP_ARCHITECTURE

## COMPONENTS
| File | Responsibility |
| --- | --- |
| xair_mcp/server.py | FastMCP tool registration, global clients, macros and output shaping |
| xair_mcp/osc_client.py | OSC codec; UDP receiver thread; pending request events; caches |
| xair_mcp/osc_map.py | 405 patterned metadata entries; ranges/enums/conversion keys |
| xair_mcp/conversions.py | 21 named human/wire converters |
| xair_mcp/ms_client.py | HTTP and single-request WebSocket client |
| presets/band_presets.json | Local macro definitions |
| tests/test_xair_mcp.py | Offline conversion/codec/map/mock tests |

## CONTROL_FLOW
MCP stdio → FastMCP → tool → direct OSC client → XR18 UDP 10024, or tool → MixingStationClient → local app HTTP/WebSocket → app's console adapter → mixer. Direct OSC does not require Mixing Station. Mixing Station data is an app model and may differ from a contemporaneous native reply. Neither transport is the USB audio stream.

## OWNERSHIP
XR18 owns native channel processing, routing and console snapshots. Mixing Station owns its normalized cross-console data tree, app UI, IDCA objects, app settings, preset subsystem and client subscriptions. Local MCP owns aliases, unit conversion, macro files and text backup generation. Ableton owns track I/O and transport; it is outside this pass.

## LIFECYCLE
`main()` calls `mcp.run()` with default stdio. `_ms` and preset path are created at import. `_mixer()` lazily constructs `_client` from XAIR_HOST. `xair_connect` replaces it. Async tools normally move blocking OSC calls to the default executor with `_run`; `xair_input_config` is an exception and calls blocking `c.get` inside its async loop.

## SAFETY
Tool annotations are hints, not enforcement. No server authorization boundary or read-only execution mode exists. Generic OSC and API tools require semantic allowlists. Local-file writes, session changes, telemetry subscriptions and audio mutations have distinct effects; see inventory.
