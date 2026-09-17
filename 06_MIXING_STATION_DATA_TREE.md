# MIXING_STATION_DATA_TREE

## STRUCTURE
`GET /console/data/paths` returns nested `{name, child, val}` objects. `child` maps path segments to nodes; `val` lists leaf suffixes. Join segments with dots. Arrays are represented by string index segments. Use actual paths rather than assuming channel-number equivalence. All 3,775 concrete leaves and definitions are preserved in JSON.

## ROOTS
| Root | Leaf count |
| --- | --- |
| fx | 59 |
| headamp | 33 |
| ch | 3555 |
| automix | 2 |
| idca | 23 |
| monitor | 10 |
| mutegrp | 8 |
| rta | 3 |
| outRouting | 82 |

## CHANNEL_INDEX_SPACE
| MS indices | Type | Native equivalent |
| --- | --- | --- |
| 0..15 | 16 mono inputs | /ch/01..16 |
| 16 | Stereo Aux | /rtn/aux |
| 17..20 | 4 stereo FX returns | /rtn/1..4 |
| 21..26 | 6 buses | /bus/1..6 |
| 27..30 | 4 FX sends | /fxsend/1..4 |
| 31 | Stereo main | /lr |
| 32..35 | 4 DCA controls | /dca/1..4 (static mapping; not probed) |

## DEFINITION_CONTRACT
Leaf definitions have type/title and may have unit/min/max/delta/tap/enums. Store enum id and name together; do not confuse array position with ID. Missing fields are unknown, not zero. Node definitions are usually empty in this capture; root definition gave 404. FX rack leaves vary by current algorithm, so this is the currently exposed model, not every possible algorithm's tree. App reconnect or topology/algorithm changes require rediscovery.

## LOOKUP
Read `mixing_station_mcp_map.json.leaf_definitions[exact_path]`. Resolve enum labels through `mixing_station_enum_map.json.path_to_enum_id`, then `enums[id]`. Unit normalization is parameter-specific; use advertised converter endpoints or definitions rather than applying one law globally.
