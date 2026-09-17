# XR18_OSC_MAP

## WIRE_PROTOCOL
Implementation: UDP 10024; unconnected ephemeral receive socket. Empty-argument requests read parameter values. OSC codec handles big-endian i32/float32, padded strings, blobs and bool→integer. No bundles, timetags or general OSC type support. `/node` requests carry a node string and receive native text via `node` or `/node`.

## COVERAGE
405 patterns expand to 2,757 addresses. `verified` in source is a pre-existing assertion, not a hardware certification. Full pattern, expansion dimensions, type, range, enum, unit, readonly and category fields are in the JSON map.

## SOURCE_CROSSWALK
`/ch/NN/config/insrc`: native zero-based analog choice; observed 0 maps to native text In01 and MS ID 1. `/ch/NN/config/rtnsrc`: observed 16/17 maps to U17/U18 and MS IDs 16/17. `/ch/NN/preamp/rtnsw`: 0 analog / 1 USB per source map; live 1 observed for both examples. Native config tuple alone excludes active selector. Native `rtnsrc` is missing from static OSC map even though readable. MS None analog ID 0 has no verified native counterpart.

## CATEGORY_COUNTS
| Category | Patterns | Expansions |
| --- | --- | --- |
| aux_return | 51 | 51 |
| bus | 84 | 504 |
| channel | 89 | 1424 |
| command | 8 | 8 |
| config | 20 | 32 |
| dca | 4 | 16 |
| fx | 2 | 260 |
| fx_return | 50 | 200 |
| fx_send | 6 | 24 |
| headamp | 2 | 48 |
| main_lr | 80 | 80 |
| snapshot | 4 | 67 |
| status | 5 | 43 |

## PATTERN_CATALOG
| Path | Type | Unit | Range or enum | Source verified |
| --- | --- | --- | --- | --- |
| /ch/{ch:02d}/config/name | s | None | None | True |
| /ch/{ch:02d}/config/color | i | None | ['OFF', 'RD', 'GN', 'YE', 'BL', 'MG', 'CY', 'WH', 'OFFi', 'RDi', 'GNi', 'YEi', 'BLi', 'MGi', 'CYi', 'WHi'] | True |
| /ch/{ch:02d}/config/insrc | i | None | [0, 17] | True |
| /ch/{ch:02d}/preamp/invert | i | None | [0, 1] | True |
| /ch/{ch:02d}/preamp/hpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/preamp/hpslope | i | None | ['12', '18', '24'] | True |
| /ch/{ch:02d}/preamp/hpf | f | freq_hpf | None | True |
| /ch/{ch:02d}/preamp/rtnsw | i | None | [0, 1] | True |
| /ch/{ch:02d}/gate/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/gate/mode | i | None | ['EXP2', 'EXP3', 'EXP4', 'GATE', 'DUCK'] | True |
| /ch/{ch:02d}/gate/thr | f | gate_thr | None | True |
| /ch/{ch:02d}/gate/range | f | gate_range | None | True |
| /ch/{ch:02d}/gate/attack | f | attack | None | True |
| /ch/{ch:02d}/gate/hold | f | hold | None | True |
| /ch/{ch:02d}/gate/release | f | release | None | True |
| /ch/{ch:02d}/gate/keysrc | i | None | ['SELF', 'CH01', 'CH02', 'CH03', 'CH04', 'CH05', 'CH06', 'CH07', 'CH08', 'CH09', 'CH10', 'CH11', 'CH12', 'CH13', 'CH14', 'CH15', 'CH16', 'BUS1', 'BUS2', 'BUS3', 'BUS4', 'BUS5', 'BUS6'] | True |
| /ch/{ch:02d}/gate/filter/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/gate/filter/type | i | None | [0, 8] | True |
| /ch/{ch:02d}/gate/filter/f | f | freq | None | True |
| /ch/{ch:02d}/dyn/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/dyn/mode | i | None | ['COMP', 'EXP'] | True |
| /ch/{ch:02d}/dyn/det | i | None | ['PEAK', 'RMS'] | True |
| /ch/{ch:02d}/dyn/env | i | None | ['LIN', 'LOG'] | True |
| /ch/{ch:02d}/dyn/thr | f | dyn_thr | None | True |
| /ch/{ch:02d}/dyn/ratio | i | None | ['1.1', '1.3', '1.5', '2.0', '2.5', '3.0', '4.0', '5.0', '7.0', '10', '20', '100'] | True |
| /ch/{ch:02d}/dyn/knee | f | dyn_knee | None | True |
| /ch/{ch:02d}/dyn/mgain | f | dyn_mgain | None | True |
| /ch/{ch:02d}/dyn/attack | f | attack | None | True |
| /ch/{ch:02d}/dyn/hold | f | hold | None | True |
| /ch/{ch:02d}/dyn/release | f | release | None | True |
| /ch/{ch:02d}/dyn/pos | i | None | ['PRE', 'POST'] | True |
| /ch/{ch:02d}/dyn/keysrc | i | None | ['SELF', 'CH01', 'CH02', 'CH03', 'CH04', 'CH05', 'CH06', 'CH07', 'CH08', 'CH09', 'CH10', 'CH11', 'CH12', 'CH13', 'CH14', 'CH15', 'CH16', 'BUS1', 'BUS2', 'BUS3', 'BUS4', 'BUS5', 'BUS6'] | True |
| /ch/{ch:02d}/dyn/mix | f | dyn_mix | None | True |
| /ch/{ch:02d}/dyn/auto | i | None | [0, 1] | True |
| /ch/{ch:02d}/dyn/filter/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/dyn/filter/type | i | None | [0, 8] | True |
| /ch/{ch:02d}/dyn/filter/f | f | freq | None | True |
| /ch/{ch:02d}/insert/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/insert/sel | i | None | ['OFF', 'FX1', 'FX2', 'FX3', 'FX4'] | True |
| /ch/{ch:02d}/eq/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/eq/1/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /ch/{ch:02d}/eq/1/f | f | freq | None | True |
| /ch/{ch:02d}/eq/1/g | f | eq_gain | None | True |
| /ch/{ch:02d}/eq/1/q | f | eq_q | None | True |
| /ch/{ch:02d}/eq/2/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /ch/{ch:02d}/eq/2/f | f | freq | None | True |
| /ch/{ch:02d}/eq/2/g | f | eq_gain | None | True |
| /ch/{ch:02d}/eq/2/q | f | eq_q | None | True |
| /ch/{ch:02d}/eq/3/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /ch/{ch:02d}/eq/3/f | f | freq | None | True |
| /ch/{ch:02d}/eq/3/g | f | eq_gain | None | True |
| /ch/{ch:02d}/eq/3/q | f | eq_q | None | True |
| /ch/{ch:02d}/eq/4/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /ch/{ch:02d}/eq/4/f | f | freq | None | True |
| /ch/{ch:02d}/eq/4/g | f | eq_gain | None | True |
| /ch/{ch:02d}/eq/4/q | f | eq_q | None | True |
| /ch/{ch:02d}/mix/on | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/fader | f | fader_db | None | True |
| /ch/{ch:02d}/mix/lr | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/pan | f | pan | None | True |
| /ch/{ch:02d}/mix/01/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/01/pan | f | pan | None | True |
| /ch/{ch:02d}/mix/01/grpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/01/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /ch/{ch:02d}/mix/02/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/02/grpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/02/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /ch/{ch:02d}/mix/03/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/03/pan | f | pan | None | True |
| /ch/{ch:02d}/mix/03/grpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/03/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /ch/{ch:02d}/mix/04/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/04/grpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/04/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /ch/{ch:02d}/mix/05/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/05/pan | f | pan | None | True |
| /ch/{ch:02d}/mix/05/grpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/05/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /ch/{ch:02d}/mix/06/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/06/grpon | i | None | [0, 1] | True |
| /ch/{ch:02d}/mix/06/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /ch/{ch:02d}/mix/07/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/08/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/09/level | f | fader_db | None | True |
| /ch/{ch:02d}/mix/10/level | f | fader_db | None | True |
| /ch/{ch:02d}/grp/dca | i | None | [0, 15] | True |
| /ch/{ch:02d}/grp/mute | i | None | [0, 15] | True |
| /ch/{ch:02d}/automix/group | i | None | ['OFF', 'X', 'Y'] | True |
| /ch/{ch:02d}/automix/weight | f | automix_w | None | True |
| /rtn/aux/config/name | s | None | None | True |
| /rtn/aux/config/color | i | None | ['OFF', 'RD', 'GN', 'YE', 'BL', 'MG', 'CY', 'WH', 'OFFi', 'RDi', 'GNi', 'YEi', 'BLi', 'MGi', 'CYi', 'WHi'] | True |
| /rtn/aux/preamp/invert | i | None | [0, 1] | False |
| /rtn/aux/eq/on | i | None | [0, 1] | True |
| /rtn/aux/eq/1/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/aux/eq/1/f | f | freq | None | True |
| /rtn/aux/eq/1/g | f | eq_gain | None | True |
| /rtn/aux/eq/1/q | f | eq_q | None | True |
| /rtn/aux/eq/2/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/aux/eq/2/f | f | freq | None | True |
| /rtn/aux/eq/2/g | f | eq_gain | None | True |
| /rtn/aux/eq/2/q | f | eq_q | None | True |
| /rtn/aux/eq/3/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/aux/eq/3/f | f | freq | None | True |
| /rtn/aux/eq/3/g | f | eq_gain | None | True |
| /rtn/aux/eq/3/q | f | eq_q | None | True |
| /rtn/aux/eq/4/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/aux/eq/4/f | f | freq | None | True |
| /rtn/aux/eq/4/g | f | eq_gain | None | True |
| /rtn/aux/eq/4/q | f | eq_q | None | True |
| /rtn/aux/mix/on | i | None | [0, 1] | True |
| /rtn/aux/mix/fader | f | fader_db | None | True |
| /rtn/aux/mix/lr | i | None | [0, 1] | True |
| /rtn/aux/mix/pan | f | pan | None | True |
| /rtn/aux/mix/01/level | f | fader_db | None | True |
| /rtn/aux/mix/01/pan | f | pan | None | True |
| /rtn/aux/mix/01/grpon | i | None | [0, 1] | True |
| /rtn/aux/mix/01/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/aux/mix/02/level | f | fader_db | None | True |
| /rtn/aux/mix/02/grpon | i | None | [0, 1] | True |
| /rtn/aux/mix/02/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/aux/mix/03/level | f | fader_db | None | True |
| /rtn/aux/mix/03/pan | f | pan | None | True |
| /rtn/aux/mix/03/grpon | i | None | [0, 1] | True |
| /rtn/aux/mix/03/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/aux/mix/04/level | f | fader_db | None | True |
| /rtn/aux/mix/04/grpon | i | None | [0, 1] | True |
| /rtn/aux/mix/04/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/aux/mix/05/level | f | fader_db | None | True |
| /rtn/aux/mix/05/pan | f | pan | None | True |
| /rtn/aux/mix/05/grpon | i | None | [0, 1] | True |
| /rtn/aux/mix/05/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/aux/mix/06/level | f | fader_db | None | True |
| /rtn/aux/mix/06/grpon | i | None | [0, 1] | True |
| /rtn/aux/mix/06/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/aux/mix/07/level | f | fader_db | None | True |
| /rtn/aux/mix/08/level | f | fader_db | None | True |
| /rtn/aux/mix/09/level | f | fader_db | None | True |
| /rtn/aux/mix/10/level | f | fader_db | None | True |
| /rtn/aux/grp/dca | i | None | [0, 15] | True |
| /rtn/aux/grp/mute | i | None | [0, 15] | True |
| /rtn/{fx}/config/name | s | None | None | True |
| /rtn/{fx}/config/color | i | None | ['OFF', 'RD', 'GN', 'YE', 'BL', 'MG', 'CY', 'WH', 'OFFi', 'RDi', 'GNi', 'YEi', 'BLi', 'MGi', 'CYi', 'WHi'] | True |
| /rtn/{fx}/eq/on | i | None | [0, 1] | True |
| /rtn/{fx}/eq/1/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/{fx}/eq/1/f | f | freq | None | True |
| /rtn/{fx}/eq/1/g | f | eq_gain | None | True |
| /rtn/{fx}/eq/1/q | f | eq_q | None | True |
| /rtn/{fx}/eq/2/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/{fx}/eq/2/f | f | freq | None | True |
| /rtn/{fx}/eq/2/g | f | eq_gain | None | True |
| /rtn/{fx}/eq/2/q | f | eq_q | None | True |
| /rtn/{fx}/eq/3/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/{fx}/eq/3/f | f | freq | None | True |
| /rtn/{fx}/eq/3/g | f | eq_gain | None | True |
| /rtn/{fx}/eq/3/q | f | eq_q | None | True |
| /rtn/{fx}/eq/4/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /rtn/{fx}/eq/4/f | f | freq | None | True |
| /rtn/{fx}/eq/4/g | f | eq_gain | None | True |
| /rtn/{fx}/eq/4/q | f | eq_q | None | True |
| /rtn/{fx}/mix/on | i | None | [0, 1] | True |
| /rtn/{fx}/mix/fader | f | fader_db | None | True |
| /rtn/{fx}/mix/lr | i | None | [0, 1] | True |
| /rtn/{fx}/mix/pan | f | pan | None | True |
| /rtn/{fx}/mix/01/level | f | fader_db | None | True |
| /rtn/{fx}/mix/01/pan | f | pan | None | True |
| /rtn/{fx}/mix/01/grpon | i | None | [0, 1] | True |
| /rtn/{fx}/mix/01/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/{fx}/mix/02/level | f | fader_db | None | True |
| /rtn/{fx}/mix/02/grpon | i | None | [0, 1] | True |
| /rtn/{fx}/mix/02/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/{fx}/mix/03/level | f | fader_db | None | True |
| /rtn/{fx}/mix/03/pan | f | pan | None | True |
| /rtn/{fx}/mix/03/grpon | i | None | [0, 1] | True |
| /rtn/{fx}/mix/03/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/{fx}/mix/04/level | f | fader_db | None | True |
| /rtn/{fx}/mix/04/grpon | i | None | [0, 1] | True |
| /rtn/{fx}/mix/04/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/{fx}/mix/05/level | f | fader_db | None | True |
| /rtn/{fx}/mix/05/pan | f | pan | None | True |
| /rtn/{fx}/mix/05/grpon | i | None | [0, 1] | True |
| /rtn/{fx}/mix/05/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/{fx}/mix/06/level | f | fader_db | None | True |
| /rtn/{fx}/mix/06/grpon | i | None | [0, 1] | True |
| /rtn/{fx}/mix/06/tap | i | None | ['IN', 'PREEQ', 'POSTEQ', 'PRE', 'POST', 'GRP'] | True |
| /rtn/{fx}/mix/07/level | f | fader_db | None | True |
| /rtn/{fx}/mix/08/level | f | fader_db | None | True |
| /rtn/{fx}/mix/09/level | f | fader_db | None | True |
| /rtn/{fx}/mix/10/level | f | fader_db | None | True |
| /rtn/{fx}/grp/dca | i | None | [0, 15] | True |
| /rtn/{fx}/grp/mute | i | None | [0, 15] | True |
| /bus/{bus}/config/name | s | None | None | True |
| /bus/{bus}/config/color | i | None | ['OFF', 'RD', 'GN', 'YE', 'BL', 'MG', 'CY', 'WH', 'OFFi', 'RDi', 'GNi', 'YEi', 'BLi', 'MGi', 'CYi', 'WHi'] | True |
| /bus/{bus}/dyn/on | i | None | [0, 1] | True |
| /bus/{bus}/dyn/mode | i | None | ['COMP', 'EXP'] | True |
| /bus/{bus}/dyn/det | i | None | ['PEAK', 'RMS'] | True |
| /bus/{bus}/dyn/env | i | None | ['LIN', 'LOG'] | True |
| /bus/{bus}/dyn/thr | f | dyn_thr | None | True |
| /bus/{bus}/dyn/ratio | i | None | ['1.1', '1.3', '1.5', '2.0', '2.5', '3.0', '4.0', '5.0', '7.0', '10', '20', '100'] | True |
| /bus/{bus}/dyn/knee | f | dyn_knee | None | True |
| /bus/{bus}/dyn/mgain | f | dyn_mgain | None | True |
| /bus/{bus}/dyn/attack | f | attack | None | True |
| /bus/{bus}/dyn/hold | f | hold | None | True |
| /bus/{bus}/dyn/release | f | release | None | True |
| /bus/{bus}/dyn/pos | i | None | ['PRE', 'POST'] | True |
| /bus/{bus}/dyn/keysrc | i | None | ['SELF', 'CH01', 'CH02', 'CH03', 'CH04', 'CH05', 'CH06', 'CH07', 'CH08', 'CH09', 'CH10', 'CH11', 'CH12', 'CH13', 'CH14', 'CH15', 'CH16', 'BUS1', 'BUS2', 'BUS3', 'BUS4', 'BUS5', 'BUS6'] | True |
| /bus/{bus}/dyn/mix | f | dyn_mix | None | True |
| /bus/{bus}/dyn/auto | i | None | [0, 1] | True |
| /bus/{bus}/dyn/filter/on | i | None | [0, 1] | True |
| /bus/{bus}/dyn/filter/type | i | None | [0, 8] | True |
| /bus/{bus}/dyn/filter/f | f | freq | None | True |
| /bus/{bus}/insert/on | i | None | [0, 1] | True |
| /bus/{bus}/insert/sel | i | None | ['OFF', 'FX1', 'FX2', 'FX3', 'FX4'] | True |
| /bus/{bus}/eq/on | i | None | [0, 1] | True |
| /bus/{bus}/eq/mode | i | None | [0, 2] | True |
| /bus/{bus}/eq/1/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /bus/{bus}/eq/1/f | f | freq | None | True |
| /bus/{bus}/eq/1/g | f | eq_gain | None | True |
| /bus/{bus}/eq/1/q | f | eq_q | None | True |
| /bus/{bus}/eq/2/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /bus/{bus}/eq/2/f | f | freq | None | True |
| /bus/{bus}/eq/2/g | f | eq_gain | None | True |
| /bus/{bus}/eq/2/q | f | eq_q | None | True |
| /bus/{bus}/eq/3/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /bus/{bus}/eq/3/f | f | freq | None | True |
| /bus/{bus}/eq/3/g | f | eq_gain | None | True |
| /bus/{bus}/eq/3/q | f | eq_q | None | True |
| /bus/{bus}/eq/4/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /bus/{bus}/eq/4/f | f | freq | None | True |
| /bus/{bus}/eq/4/g | f | eq_gain | None | True |
| /bus/{bus}/eq/4/q | f | eq_q | None | True |
| /bus/{bus}/eq/5/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /bus/{bus}/eq/5/f | f | freq | None | True |
| /bus/{bus}/eq/5/g | f | eq_gain | None | True |
| /bus/{bus}/eq/5/q | f | eq_q | None | True |
| /bus/{bus}/eq/6/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /bus/{bus}/eq/6/f | f | freq | None | True |
| /bus/{bus}/eq/6/g | f | eq_gain | None | True |
| /bus/{bus}/eq/6/q | f | eq_q | None | True |
| /bus/{bus}/geq/20 | f | eq_gain | None | True |
| /bus/{bus}/geq/25 | f | eq_gain | None | True |
| /bus/{bus}/geq/31.5 | f | eq_gain | None | True |
| /bus/{bus}/geq/40 | f | eq_gain | None | True |
| /bus/{bus}/geq/50 | f | eq_gain | None | True |
| /bus/{bus}/geq/63 | f | eq_gain | None | True |
| /bus/{bus}/geq/80 | f | eq_gain | None | True |
| /bus/{bus}/geq/100 | f | eq_gain | None | True |
| /bus/{bus}/geq/125 | f | eq_gain | None | True |
| /bus/{bus}/geq/160 | f | eq_gain | None | True |
| /bus/{bus}/geq/200 | f | eq_gain | None | True |
| /bus/{bus}/geq/250 | f | eq_gain | None | True |
| /bus/{bus}/geq/315 | f | eq_gain | None | True |
| /bus/{bus}/geq/400 | f | eq_gain | None | True |
| /bus/{bus}/geq/500 | f | eq_gain | None | True |
| /bus/{bus}/geq/630 | f | eq_gain | None | True |
| /bus/{bus}/geq/800 | f | eq_gain | None | True |
| /bus/{bus}/geq/1k | f | eq_gain | None | True |
| /bus/{bus}/geq/1k25 | f | eq_gain | None | True |
| /bus/{bus}/geq/1k6 | f | eq_gain | None | True |
| /bus/{bus}/geq/2k | f | eq_gain | None | True |
| /bus/{bus}/geq/2k5 | f | eq_gain | None | True |
| /bus/{bus}/geq/3k15 | f | eq_gain | None | True |
| /bus/{bus}/geq/4k | f | eq_gain | None | True |
| /bus/{bus}/geq/5k | f | eq_gain | None | True |
| /bus/{bus}/geq/6k3 | f | eq_gain | None | True |
| /bus/{bus}/geq/8k | f | eq_gain | None | True |
| /bus/{bus}/geq/10k | f | eq_gain | None | True |
| /bus/{bus}/geq/12k5 | f | eq_gain | None | True |
| /bus/{bus}/geq/16k | f | eq_gain | None | True |
| /bus/{bus}/geq/20k | f | eq_gain | None | True |
| /bus/{bus}/mix/on | i | None | [0, 1] | True |
| /bus/{bus}/mix/fader | f | fader_db | None | True |
| /bus/{bus}/mix/pan | f | pan | None | True |
| /bus/{bus}/grp/dca | i | None | [0, 15] | True |
| /bus/{bus}/grp/mute | i | None | [0, 15] | True |
| /fxsend/{fx}/config/name | s | None | None | True |
| /fxsend/{fx}/config/color | i | None | ['OFF', 'RD', 'GN', 'YE', 'BL', 'MG', 'CY', 'WH', 'OFFi', 'RDi', 'GNi', 'YEi', 'BLi', 'MGi', 'CYi', 'WHi'] | True |
| /fxsend/{fx}/mix/on | i | None | [0, 1] | True |
| /fxsend/{fx}/mix/fader | f | fader_db | None | True |
| /fxsend/{fx}/grp/dca | i | None | [0, 15] | True |
| /fxsend/{fx}/grp/mute | i | None | [0, 15] | True |
| /lr/dyn/on | i | None | [0, 1] | True |
| /lr/dyn/mode | i | None | ['COMP', 'EXP'] | True |
| /lr/dyn/det | i | None | ['PEAK', 'RMS'] | True |
| /lr/dyn/env | i | None | ['LIN', 'LOG'] | True |
| /lr/dyn/thr | f | dyn_thr | None | True |
| /lr/dyn/ratio | i | None | ['1.1', '1.3', '1.5', '2.0', '2.5', '3.0', '4.0', '5.0', '7.0', '10', '20', '100'] | True |
| /lr/dyn/knee | f | dyn_knee | None | True |
| /lr/dyn/mgain | f | dyn_mgain | None | True |
| /lr/dyn/attack | f | attack | None | True |
| /lr/dyn/hold | f | hold | None | True |
| /lr/dyn/release | f | release | None | True |
| /lr/dyn/pos | i | None | ['PRE', 'POST'] | True |
| /lr/dyn/keysrc | i | None | ['SELF', 'CH01', 'CH02', 'CH03', 'CH04', 'CH05', 'CH06', 'CH07', 'CH08', 'CH09', 'CH10', 'CH11', 'CH12', 'CH13', 'CH14', 'CH15', 'CH16', 'BUS1', 'BUS2', 'BUS3', 'BUS4', 'BUS5', 'BUS6'] | True |
| /lr/dyn/mix | f | dyn_mix | None | True |
| /lr/dyn/auto | i | None | [0, 1] | True |
| /lr/dyn/filter/on | i | None | [0, 1] | True |
| /lr/dyn/filter/type | i | None | [0, 8] | True |
| /lr/dyn/filter/f | f | freq | None | True |
| /lr/insert/on | i | None | [0, 1] | True |
| /lr/insert/sel | i | None | ['OFF', 'FX1', 'FX2', 'FX3', 'FX4'] | True |
| /lr/eq/on | i | None | [0, 1] | True |
| /lr/eq/mode | i | None | [0, 2] | True |
| /lr/eq/1/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /lr/eq/1/f | f | freq | None | True |
| /lr/eq/1/g | f | eq_gain | None | True |
| /lr/eq/1/q | f | eq_q | None | True |
| /lr/eq/2/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /lr/eq/2/f | f | freq | None | True |
| /lr/eq/2/g | f | eq_gain | None | True |
| /lr/eq/2/q | f | eq_q | None | True |
| /lr/eq/3/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /lr/eq/3/f | f | freq | None | True |
| /lr/eq/3/g | f | eq_gain | None | True |
| /lr/eq/3/q | f | eq_q | None | True |
| /lr/eq/4/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /lr/eq/4/f | f | freq | None | True |
| /lr/eq/4/g | f | eq_gain | None | True |
| /lr/eq/4/q | f | eq_q | None | True |
| /lr/eq/5/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /lr/eq/5/f | f | freq | None | True |
| /lr/eq/5/g | f | eq_gain | None | True |
| /lr/eq/5/q | f | eq_q | None | True |
| /lr/eq/6/type | i | None | ['LCut', 'LShv', 'PEQ', 'VEQ', 'HShv', 'HCut'] | True |
| /lr/eq/6/f | f | freq | None | True |
| /lr/eq/6/g | f | eq_gain | None | True |
| /lr/eq/6/q | f | eq_q | None | True |
| /lr/geq/20 | f | eq_gain | None | True |
| /lr/geq/25 | f | eq_gain | None | True |
| /lr/geq/31.5 | f | eq_gain | None | True |
| /lr/geq/40 | f | eq_gain | None | True |
| /lr/geq/50 | f | eq_gain | None | True |
| /lr/geq/63 | f | eq_gain | None | True |
| /lr/geq/80 | f | eq_gain | None | True |
| /lr/geq/100 | f | eq_gain | None | True |
| /lr/geq/125 | f | eq_gain | None | True |
| /lr/geq/160 | f | eq_gain | None | True |
| /lr/geq/200 | f | eq_gain | None | True |
| /lr/geq/250 | f | eq_gain | None | True |
| /lr/geq/315 | f | eq_gain | None | True |
| /lr/geq/400 | f | eq_gain | None | True |
| /lr/geq/500 | f | eq_gain | None | True |
| /lr/geq/630 | f | eq_gain | None | True |
| /lr/geq/800 | f | eq_gain | None | True |
| /lr/geq/1k | f | eq_gain | None | True |
| /lr/geq/1k25 | f | eq_gain | None | True |
| /lr/geq/1k6 | f | eq_gain | None | True |
| /lr/geq/2k | f | eq_gain | None | True |
| /lr/geq/2k5 | f | eq_gain | None | True |
| /lr/geq/3k15 | f | eq_gain | None | True |
| /lr/geq/4k | f | eq_gain | None | True |
| /lr/geq/5k | f | eq_gain | None | True |
| /lr/geq/6k3 | f | eq_gain | None | True |
| /lr/geq/8k | f | eq_gain | None | True |
| /lr/geq/10k | f | eq_gain | None | True |
| /lr/geq/12k5 | f | eq_gain | None | True |
| /lr/geq/16k | f | eq_gain | None | True |
| /lr/geq/20k | f | eq_gain | None | True |
| /lr/mix/on | i | None | [0, 1] | True |
| /lr/mix/fader | f | fader_db | None | True |
| /lr/mix/pan | f | pan | None | True |
| /fx/{fx}/type | i | None | ['HALL', 'AMBI', 'RPLT', 'ROOM', 'CHAM', 'PLAT', 'VREV', 'VRM', 'GATE', 'RVRS', 'DLY', '3TAP', '4TAP', 'CRS', 'FLNG', 'PHAS', 'DIMC', 'FILT', 'ROTA', 'PAN', 'SUB', 'D/RV', 'CR/R', 'FL/R', 'D/CR', 'D/FL', 'MODD', 'GEQ2', 'GEQ', 'TEQ2', 'TEQ', 'DES2', 'DES', 'P1A', 'P1A2', 'PQ5', 'PQ5S', 'WAVD', 'LIM', 'CMB', 'CMB2', 'FAC', 'FAC1M', 'FAC2', 'LEC', 'LEC2', 'ULC', 'ULC2', 'ENH2', 'ENH', 'EXC2', 'EXC', 'IMG', 'EDI', 'SON', 'AMP2', 'AMP', 'DRV2', 'DRV', 'PIT2', 'PIT'] | True |
| /fx/{fx}/par/{par:02d} | f | None | [0.0, 1.0] | True |
| /headamp/{ha:02d}/gain | f | headamp | None | True |
| /headamp/{ha:02d}/phantom | i | None | [0, 1] | True |
| /config/mute/{mg} | i | None | [0, 1] | True |
| /config/chlink/{pair} | i | None | [0, 1] | True |
| /config/buslink/{buspair} | i | None | [0, 1] | True |
| /config/linkcfg/hadly | i | None | [0, 1] | True |
| /config/linkcfg/eq | i | None | [0, 1] | True |
| /config/linkcfg/dyn | i | None | [0, 1] | True |
| /config/linkcfg/fdrmute | i | None | [0, 1] | True |
| /config/solo/level | f | fader_db | None | True |
| /config/solo/source | i | None | ['OFF', 'LR', 'LR+M', 'LR PFL', 'LR AFL', 'AUX 5/6', 'AUX 7/8'] | True |
| /config/solo/sourcetrim | f | solo_trim | None | True |
| /config/solo/chmode | i | None | [0, 1] | True |
| /config/solo/busmode | i | None | [0, 1] | True |
| /config/solo/dimatt | f | solo_dim | None | True |
| /config/solo/dim | i | None | [0, 1] | True |
| /config/solo/mono | i | None | [0, 1] | True |
| /config/solo/delay | i | None | [0, 1] | True |
| /config/solo/delaytime | f | None | None | True |
| /config/solo/exclusive | i | None | [0, 1] | True |
| /config/amixenable/X | i | None | [0, 1] | True |
| /config/amixenable/Y | i | None | [0, 1] | True |
| /dca/{dca}/on | i | None | [0, 1] | True |
| /dca/{dca}/fader | f | fader_db | None | True |
| /dca/{dca}/config/name | s | None | None | True |
| /dca/{dca}/config/color | i | None | ['OFF', 'RD', 'GN', 'YE', 'BL', 'MG', 'CY', 'WH', 'OFFi', 'RDi', 'GNi', 'YEi', 'BLi', 'MGi', 'CYi', 'WHi'] | True |
| /-snap/{snap:02d}/name | s | None | None | True |
| /-snap/save | i | None | [1, 64] | True |
| /-snap/load | i | None | [1, 64] | True |
| /-snap/index | i | None | None | False |
| /-stat/solosw/{sw:02d} | i | None | [0, 1] | False |
| /-stat/solo | i | None | None | True |
| /-prefs/lan/addr | s | None | None | False |
| /-prefs/lan/mode | i | None | None | False |
| /-prefs/name | s | None | None | False |
| /xinfo | None | None | None | True |
| /info | None | None | None | True |
| /status | None | None | None | True |
| /xremote | None | None | None | True |
| /unsubscribe | None | None | None | True |
| /renew | None | None | None | True |
| /node | s | None | None | True |
| /meters | s | None | None | True |

## ADDITIONAL_NATIVE_NODES
Global routing coverage is implemented outside the static dictionary: routing/usb/01..18, routing/aux/01..06, routing/main/01..02. Their raw source/tap tokens must be preserved. Labels `main_out_l` and `monitor_out` in the helper are implementation assumptions, not independently verified outlet semantics.
