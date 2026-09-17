# CORE_MAPPING_INDEX

## SCOPE
Core MCP/API mapping only. No mixer, Ableton, playback, scene, macro, gain, mute, fader or routing changes. No readiness judgments, signal tests, gain-stage procedures or Gremlins procedures. Existing source modifications were preserved; this pass changes documentation only.

## EVIDENCE_STATUS
- VERIFIED_SOURCE: implementation or advertised schema inspected; not proof of hardware support.
- VERIFIED_READ: recorded read-only API response for this capture.
- INFERRED: correspondence supported by structure but not exhaustively demonstrated.
- UNKNOWN: missing or conflicting evidence; never substitute a default.

Capture: 2026-09-17T00:34:14.810846+00:00. Values are time-bound, sequential observations, not an atomic mixer snapshot. The routing guide is intended configuration only. This map does not certify routing or sound.

## FILES
- [01_MCP_ARCHITECTURE.md](01_MCP_ARCHITECTURE.md)
- [02_RUNTIME_AND_CONFIGURATION.md](02_RUNTIME_AND_CONFIGURATION.md)
- [03_TOOL_INVENTORY.md](03_TOOL_INVENTORY.md)
- [04_XR18_OSC_MAP.md](04_XR18_OSC_MAP.md)
- [05_MIXING_STATION_API_MAP.md](05_MIXING_STATION_API_MAP.md)
- [06_MIXING_STATION_DATA_TREE.md](06_MIXING_STATION_DATA_TREE.md)
- [07_CHANNEL_INPUT_SOURCE_MAP.md](07_CHANNEL_INPUT_SOURCE_MAP.md)
- [08_CHANNEL_STRIP_PARAMETER_MAP.md](08_CHANNEL_STRIP_PARAMETER_MAP.md)
- [09_USB_ROUTING_MAP.md](09_USB_ROUTING_MAP.md)
- [10_BUSES_RETURNS_FX_AND_MONITOR_MAP.md](10_BUSES_RETURNS_FX_AND_MONITOR_MAP.md)
- [11_SNAPSHOT_SCENE_MACRO_MAP.md](11_SNAPSHOT_SCENE_MACRO_MAP.md)
- [12_MIDI_INTERFACE_MAP.md](12_MIDI_INTERFACE_MAP.md)
- [13_ERROR_TIMEOUT_AND_RECONNECT_MAP.md](13_ERROR_TIMEOUT_AND_RECONNECT_MAP.md)
- [14_KNOWN_LIMITATIONS.md](14_KNOWN_LIMITATIONS.md)
- [15_TEST_COVERAGE.md](15_TEST_COVERAGE.md)
- [16_FUTURE_DIAGNOSTIC_TASKS.md](16_FUTURE_DIAGNOSTIC_TASKS.md)
- [mixing_station_mcp_map.json](mixing_station_mcp_map.json)
- [mixing_station_enum_map.json](mixing_station_enum_map.json)

## COVERAGE
33 tools; 51 advertised API operations; 405 OSC patterns / 2,757 expansions; 3,775 live data leaves with 3,775 definitions; 706 enum-bearing paths / 38 distinct enum tables. The empty root node definition returned 404; all leaf definitions succeeded. Expansion counts do not prove native support.

## EVIDENCE_FILES
Raw schemas, tree, leaf and node definitions, console architecture, runtime versions, source reads and WebSocket probes are in `mapping_evidence/`. `mixing_station_mcp_map.json` carries full tool schemas and return expressions, API schemas and data definitions. `mixing_station_enum_map.json` deduplicates labels by stable content hash and maps each exact path to its table.

## ROUTING_AUTHORITY
`/Users/tomservo/Desktop/# Neon Blonde Live Audio Patch & Routing Guide/# Neon Blonde Live Audio Patch & Routing Guide.md` was read and not changed. Its U labels are annotated as USB returns according to this task's explicit example; the guide's table heading alone must not be interpreted as a bus assignment.

## REPOSITORY_IMPLEMENTATION_BOUNDARY
This documentation maps a local deployment with pre-existing, uncommitted `server.py` and `ms_client.py` additions. Those code changes are not part of this documentation publication. The four additional mapped tools are `xair_routing_overview`, `xair_input_config`, `ms_data_tree`, and `ms_data_value`. Check the source hash manifest before treating this map as an exact description of a deployed Git revision.
