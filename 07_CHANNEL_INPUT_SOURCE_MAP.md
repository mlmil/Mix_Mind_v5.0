# CHANNEL_INPUT_SOURCE_MAP

## CRITICAL_FIELDS
| MS field on ch.N | Meaning | Valid raw IDs | Exact enum labels | Native field |
| --- | --- | --- | --- | --- |
| cfg.srcSel | Active A/D versus USB selection | 0,1 | 0=Off; 1=On | /ch/NN/preamp/rtnsw |
| routing.srcCfg.0 | Analog source choice retained even in USB mode | 0..18 | 0=None - None; 1..8=In 1-8 - In N; 9..16=In 9-16 - In N; 17=Aux - Aux L; 18=Aux - Aux R | /ch/NN/config/insrc |
| routing.srcCfg.1 | USB return choice retained even in A/D mode | 0..17 | USB - U 1 through USB - U 18 | /ch/NN/config/rtnsrc |

## SELECTOR_SEMANTICS
MS enum labels are literally Off/On, not A/D/USB. The source implementation associates selector 0 with A/D and 1 with USB; native preamp/rtnsw agrees at value 1 on both sampled strips. Thus USB mode at 1 is corroborated by live reads. The 0 branch is source-defined and was not exercised by toggling or observed in this sample. UI-facing semantic labels are A/D and USB; direct UI rendering was not inspected. Invalid values must decode UNKNOWN, not A/D.

## NUMBERING
MS `ch.1` is channel strip 2; native `/ch/02` is channel strip 2. Analog MS ID 1 and native insrc 0 both represent In01 in the captured native node. USB MS ID 16 and native rtnsrc 16 both represent U17. Analog MS IDs 1..18 → native 0..17 is inferred beyond the observed Input 1 example and supported by source map range. MS analog None ID 0 has no proven native value; never subtract one blindly for None.

## VERIFIED_READ_EXAMPLES
| Strip | MS name | MS selector | MS analog ID / label | MS USB ID / label | Native config tuple | Native node source |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | KYLE A | 1 / On → USB | 1 / In 1-8 - In 1 | 16 / USB - U 17 | [KYLE A_45,7,0,16] | In01 U17 |
| 7 | KYLE B | 1 / On → USB | 1 / In 1-8 - In 1 | 17 / USB - U 18 | [KYLE B_46,7,0,17] | In01 U18 |

The name difference is recorded, with cause UNKNOWN. The analog numeric difference is resolved by the native text; it is a numbering difference, not a route mismatch. These reads do not prove physical cabling or Ableton audio flow.

## INTENDED_NEON_BLONDE_EXAMPLE
Physical Input 1 → channel strips 2 and 7 → USB returns 17 and 18 → stereo left/right.
This is the user's reference association, not a complete serial signal graph: USB returns enter strip source selection from the host. It associates analog Input 1, two strips, and USB return roles. It does not establish the USB send, Ableton input, Ableton output, panning, or native stereo-link mechanism. Nonadjacent strip labels alone do not prove a hardware link.

## COMPLETE_ENUM_LABELS

### ch.1.cfg.srcSel
| Raw ID | Label |
| --- | --- |
| 0 | Off |
| 1 | On |

### ch.1.routing.srcCfg.0
| Raw ID | Label |
| --- | --- |
| 0 | None - None |
| 1 | In 1-8 - In 1 |
| 2 | In 1-8 - In 2 |
| 3 | In 1-8 - In 3 |
| 4 | In 1-8 - In 4 |
| 5 | In 1-8 - In 5 |
| 6 | In 1-8 - In 6 |
| 7 | In 1-8 - In 7 |
| 8 | In 1-8 - In 8 |
| 9 | In 9-16 - In 9 |
| 10 | In 9-16 - In 10 |
| 11 | In 9-16 - In 11 |
| 12 | In 9-16 - In 12 |
| 13 | In 9-16 - In 13 |
| 14 | In 9-16 - In 14 |
| 15 | In 9-16 - In 15 |
| 16 | In 9-16 - In 16 |
| 17 | Aux - Aux L |
| 18 | Aux - Aux R |

### ch.1.routing.srcCfg.1
| Raw ID | Label |
| --- | --- |
| 0 | USB - U 1 |
| 1 | USB - U 2 |
| 2 | USB - U 3 |
| 3 | USB - U 4 |
| 4 | USB - U 5 |
| 5 | USB - U 6 |
| 6 | USB - U 7 |
| 7 | USB - U 8 |
| 8 | USB - U 9 |
| 9 | USB - U 10 |
| 10 | USB - U 11 |
| 11 | USB - U 12 |
| 12 | USB - U 13 |
| 13 | USB - U 14 |
| 14 | USB - U 15 |
| 15 | USB - U 16 |
| 16 | USB - U 17 |
| 17 | USB - U 18 |
