# TEST_COVERAGE

## EXECUTED
`venv/bin/python -m pytest tests/ -q`: 15 passed in 0.36s. Inspected tests use local mock UDP endpoints and codec bytes; no live mixer writes. No test or implementation changes made.

## TEST_INVENTORY
- `test_fader_law_roundtrip`
- `test_fader_law_anchors`
- `test_freq_log_law`
- `test_headamp`
- `test_all_units_roundtrip`
- `test_codec_roundtrip`
- `test_meter_blob_decode`
- `test_map_stats_and_expansion`
- `test_find_entry`
- `test_search`
- `test_every_unit_in_map_exists`
- `test_client_get_set_roundtrip`
- `test_client_timeout_message`
- `test_resolve_strip`
- `test_macro_expansion`

## COVERED
Conversion anchors/roundtrips, supported codec roundtrips, one valid meter blob, static map lookup/search/expansion and unit references, local mock get/set/info/node, timeout text, aliases and macro expansion.

## NOT_COVERED
MS HTTP/WS transport, source-field decoder, stale/invalid data, definition/enum drift, real native range correctness, partial datagrams, meter freshness, socket restart lifecycle, duplicate concurrent address requests, end-to-end scene completion, authorization, partial batch errors and native/MS naming divergence. No numeric coverage percentage measured.

## READ_PROBES
Captured full local OpenAPI, console architecture, tree and every leaf definition. All 3,775 leaf reads succeeded; root node definition 404 is retained. Bounded WS probes verified app state and current GET value route, and reproduced legacy route rejection. Native empty-argument source reads and node dumps corroborated numbering. No meters, faders, gain changes, signal tests or readiness audit.

## ARTIFACT_VALIDATION
JSON strict parse, tool/path/definition counts, complete file existence and internal Markdown links checked after generation. Source hash manifest records source read for this mapping.
