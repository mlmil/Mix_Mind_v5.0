# BUSES_RETURNS_FX_AND_MONITOR_MAP

## ARCHITECTURE
| Object | MS representation | Native representation |
| --- | --- | --- |
| Buses 1..6 | ch.21..26 | /bus/1..6 |
| FX returns 1..4 | ch.17..20 stereo | /rtn/1..4 |
| FX sends 1..4 | ch.27..30 | /fxsend/1..4 |
| LR | ch.31 stereo | /lr |
| Aux | ch.16 stereo | /rtn/aux |
| FX processors | fx.rack.0..3; fx.cfg.0..3 | /fx/1..4 |
| Monitor | monitor subtree | /config/solo/* plus routing nodes |
| DCA | ch.32..35; idca separate app objects | /dca/1..4 source map; hardware support not established |

## TARGETS
`GET /console/mixTargets` describes available sinks; captured raw in evidence. Input/Aux/FX-return channel types advertise six buses and four FX-send targets. DCA is a control grouping, not an audio bus. A source/tap label must be preserved alongside the target ID.

## REPRESENTATIVE_PATH_DEFINITIONS
| Path | Definition |
| --- | --- |
| ch.16.cfg.color | {"enums":[{"name":"Black","id":0},{"name":"Red","id":1},{"name":"Green","id":2},{"name":"Yellow","id":3},{"name":"Blue","id":4},{"name":"Magenta","id":5},{"name":"Cyan","id":6},{"name":"White","id":7},{"name":"Black Inv","id":8},{"name":"Red Inv","id":9},{"name":"Green Inv","id":10},{"name":"Yellow Inv","id":11},{"name":"Blue Inv","id":12},{"name":"Magenta Inv","id":13},{"name":"Cyan Inv","id":14},{"name":"White Inv","id":15}],"title":"Color","type":"enum"} |
| ch.16.cfg.icon | {"unit":"","tap":false,"min":0.0,"max":73.0,"delta":1.0,"title":"Icon","type":"integer"} |
| ch.16.cfg.name | {"type":"string","constraints":["ASCII text","Max length 12"]} |
| ch.16.cfg.srcSel | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"On/Off","type":"enum"} |
| ch.16.grp.dca.0 | {"type":"boolean"} |
| ch.16.grp.dca.1 | {"type":"boolean"} |
| ch.16.grp.dca.2 | {"type":"boolean"} |
| ch.16.grp.dca.3 | {"type":"boolean"} |
| ch.16.grp.mute.0 | {"type":"boolean"} |
| ch.16.grp.mute.1 | {"type":"boolean"} |
| ch.16.grp.mute.2 | {"type":"boolean"} |
| ch.16.grp.mute.3 | {"type":"boolean"} |
| ch.16.headamp.gain | {"tap":false,"min":-12.0,"max":20.0,"delta":0.3125,"title":"Gain","type":"float"} |
| ch.16.info.isActive | {"type":"boolean"} |
| ch.16.info.isStereo | {"type":"boolean"} |
| ch.16.levelData.-1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.-1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.-1.on | {"type":"boolean"} |
| ch.16.levelData.-1.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.16.levelData.-2.level | {"tap":false,"min":-12.0,"max":20.0,"delta":0.3125,"title":"Gain","type":"float"} |
| ch.16.levelData.-2.lvl | {"tap":false,"min":-12.0,"max":20.0,"delta":0.3125,"title":"Gain","type":"float"} |
| ch.16.levelData.0.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.2.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.2.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.3.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.3.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.4.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.4.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.5.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.5.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.6.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.6.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.7.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.7.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.8.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.8.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.9.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.levelData.9.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.on | {"type":"boolean"} |
| ch.16.mix.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.16.mix.rawOn | {"type":"boolean"} |
| ch.16.mix.sends.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.0.on | {"type":"boolean"} |
| ch.16.mix.sends.0.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.1.on | {"type":"boolean"} |
| ch.16.mix.sends.1.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.2.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.2.on | {"type":"boolean"} |
| ch.16.mix.sends.2.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.3.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.3.on | {"type":"boolean"} |
| ch.16.mix.sends.3.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.4.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.4.on | {"type":"boolean"} |
| ch.16.mix.sends.4.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.5.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.5.on | {"type":"boolean"} |
| ch.16.mix.sends.5.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.6.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.6.on | {"type":"boolean"} |
| ch.16.mix.sends.6.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.7.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.7.on | {"type":"boolean"} |
| ch.16.mix.sends.7.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.8.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.8.on | {"type":"boolean"} |
| ch.16.mix.sends.8.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.16.mix.sends.9.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.16.mix.sends.9.on | {"type":"boolean"} |
| ch.16.mix.sends.9.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.16.mix.stOn | {"type":"boolean"} |
| ch.16.peq.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.16.peq.bands.0.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.16.peq.bands.0.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.16.peq.bands.0.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.16.peq.bands.1.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.16.peq.bands.1.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.16.peq.bands.1.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.16.peq.bands.1.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.16.peq.bands.2.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.16.peq.bands.2.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.16.peq.bands.2.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.16.peq.bands.2.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.16.peq.bands.3.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.16.peq.bands.3.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.16.peq.bands.3.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.16.peq.bands.3.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.16.peq.on | {"type":"boolean"} |
| ch.16.peq.selBand.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.16.peq.selBand.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.16.peq.selBand.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.16.peq.selBand.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.16.preamp.retOn | {"type":"boolean"} |
| ch.16.preamp.retTrim | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| ch.16.rawEq.model | {"enums":[{"name":"PEQ","id":0}],"title":"","type":"enum"} |
| ch.16.routing.srcCfg.0 | {"enums":[{"name":"USB - U 1/2","id":0},{"name":"USB - U 3/4","id":1},{"name":"USB - U 5/6","id":2},{"name":"USB - U 7/8","id":3},{"name":"USB - U 9/10","id":4},{"name":"USB - U 11/12","id":5},{"name":"USB - U 13/14","id":6},{"name":"USB - U 15/16","id":7},{"name":"USB - U 17/18","id":8}],"title":"Signal sources","type":"enum"} |
| ch.16.solo | {"type":"boolean"} |
| ch.17.cfg.color | {"enums":[{"name":"Black","id":0},{"name":"Red","id":1},{"name":"Green","id":2},{"name":"Yellow","id":3},{"name":"Blue","id":4},{"name":"Magenta","id":5},{"name":"Cyan","id":6},{"name":"White","id":7},{"name":"Black Inv","id":8},{"name":"Red Inv","id":9},{"name":"Green Inv","id":10},{"name":"Yellow Inv","id":11},{"name":"Blue Inv","id":12},{"name":"Magenta Inv","id":13},{"name":"Cyan Inv","id":14},{"name":"White Inv","id":15}],"title":"Color","type":"enum"} |
| ch.17.cfg.icon | {"unit":"","tap":false,"min":0.0,"max":73.0,"delta":1.0,"title":"Icon","type":"integer"} |
| ch.17.cfg.name | {"type":"string","constraints":["ASCII text","Max length 12"]} |
| ch.17.cfg.srcSel | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"On/Off","type":"enum"} |
| ch.17.grp.dca.0 | {"type":"boolean"} |
| ch.17.grp.dca.1 | {"type":"boolean"} |
| ch.17.grp.dca.2 | {"type":"boolean"} |
| ch.17.grp.dca.3 | {"type":"boolean"} |
| ch.17.grp.mute.0 | {"type":"boolean"} |
| ch.17.grp.mute.1 | {"type":"boolean"} |
| ch.17.grp.mute.2 | {"type":"boolean"} |
| ch.17.grp.mute.3 | {"type":"boolean"} |
| ch.17.info.isActive | {"type":"boolean"} |
| ch.17.info.isStereo | {"type":"boolean"} |
| ch.17.levelData.-1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.-1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.-1.on | {"type":"boolean"} |
| ch.17.levelData.-1.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.17.levelData.0.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.2.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.2.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.3.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.3.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.4.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.4.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.5.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.5.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.6.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.6.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.7.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.7.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.8.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.8.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.9.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.levelData.9.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.on | {"type":"boolean"} |
| ch.17.mix.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.17.mix.rawOn | {"type":"boolean"} |
| ch.17.mix.sends.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.0.on | {"type":"boolean"} |
| ch.17.mix.sends.0.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.1.on | {"type":"boolean"} |
| ch.17.mix.sends.1.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.2.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.2.on | {"type":"boolean"} |
| ch.17.mix.sends.2.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.3.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.3.on | {"type":"boolean"} |
| ch.17.mix.sends.3.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.4.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.4.on | {"type":"boolean"} |
| ch.17.mix.sends.4.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.5.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.5.on | {"type":"boolean"} |
| ch.17.mix.sends.5.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.6.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.6.on | {"type":"boolean"} |
| ch.17.mix.sends.6.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.7.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.7.on | {"type":"boolean"} |
| ch.17.mix.sends.7.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.8.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.8.on | {"type":"boolean"} |
| ch.17.mix.sends.8.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.17.mix.sends.9.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.17.mix.sends.9.on | {"type":"boolean"} |
| ch.17.mix.sends.9.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.17.mix.stOn | {"type":"boolean"} |
| ch.17.peq.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.17.peq.bands.0.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.17.peq.bands.0.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.17.peq.bands.0.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.17.peq.bands.1.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.17.peq.bands.1.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.17.peq.bands.1.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.17.peq.bands.1.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.17.peq.bands.2.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.17.peq.bands.2.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.17.peq.bands.2.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.17.peq.bands.2.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.17.peq.bands.3.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.17.peq.bands.3.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.17.peq.bands.3.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.17.peq.bands.3.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.17.peq.on | {"type":"boolean"} |
| ch.17.peq.selBand.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.17.peq.selBand.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.17.peq.selBand.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.17.peq.selBand.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.17.preamp.retOn | {"type":"boolean"} |
| ch.17.preamp.retTrim | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| ch.17.rawEq.model | {"enums":[{"name":"PEQ","id":0}],"title":"","type":"enum"} |
| ch.17.routing.srcCfg.0 | {"enums":[{"name":"USB - U 1/2","id":0},{"name":"USB - U 3/4","id":1},{"name":"USB - U 5/6","id":2},{"name":"USB - U 7/8","id":3},{"name":"USB - U 9/10","id":4},{"name":"USB - U 11/12","id":5},{"name":"USB - U 13/14","id":6},{"name":"USB - U 15/16","id":7},{"name":"USB - U 17/18","id":8}],"title":"Signal sources","type":"enum"} |
| ch.17.solo | {"type":"boolean"} |
| ch.21.cfg.color | {"enums":[{"name":"Black","id":0},{"name":"Red","id":1},{"name":"Green","id":2},{"name":"Yellow","id":3},{"name":"Blue","id":4},{"name":"Magenta","id":5},{"name":"Cyan","id":6},{"name":"White","id":7},{"name":"Black Inv","id":8},{"name":"Red Inv","id":9},{"name":"Green Inv","id":10},{"name":"Yellow Inv","id":11},{"name":"Blue Inv","id":12},{"name":"Magenta Inv","id":13},{"name":"Cyan Inv","id":14},{"name":"White Inv","id":15}],"title":"Color","type":"enum"} |
| ch.21.cfg.icon | {"unit":"","tap":false,"min":0.0,"max":73.0,"delta":1.0,"title":"Icon","type":"integer"} |
| ch.21.cfg.name | {"type":"string","constraints":["ASCII text","Max length 12"]} |
| ch.21.dyn.attack | {"unit":" ms","tap":false,"min":0.0,"max":120.0,"delta":1.0,"title":"Attack","type":"float"} |
| ch.21.dyn.autoTime | {"type":"boolean"} |
| ch.21.dyn.detection | {"type":"boolean"} |
| ch.21.dyn.envelope | {"type":"boolean"} |
| ch.21.dyn.filter.filters.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.dyn.filter.filters.bands.0.on | {"type":"boolean"} |
| ch.21.dyn.filter.filters.bands.0.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.21.dyn.filter.filters.on | {"type":"boolean"} |
| ch.21.dyn.filter.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.dyn.filter.on | {"type":"boolean"} |
| ch.21.dyn.filter.src | {"enums":[{"name":"KYLE","id":0},{"name":"MATT","id":1},{"name":"KYLE A","id":2},{"name":"ALFRED","id":3},{"name":"GUITAR","id":4},{"name":"BOH CLICK","id":5},{"name":"FULL L","id":6},{"name":"KYLE B","id":7},{"name":"MIKE","id":8},{"name":"BASS","id":9},{"name":"BOH CUES","id":10},{"name":"MIDI DRUMS","id":11},{"name":"KICK TRIG","id":12},{"name":"FULL R","id":13},{"name":"DAVE","id":14},{"name":"KICK MIC","id":15},{"name":"KEYS","id":16},{"name":"KYLE","id":17},{"name":"MIKE","id":18},{"name":"ALFRED","id":19},{"name":"MATT","id":20},{"name":"DAVE","id":21},{"name":"SUB","id":22}],"title":"Src","type":"enum"} |
| ch.21.dyn.filter.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.21.dyn.gain | {"unit":" dB","tap":false,"min":0.0,"max":24.0,"delta":0.5,"title":"Gain","type":"float"} |
| ch.21.dyn.hold | {"unit":" ms","tap":false,"min":0.020000001,"max":2000.0007,"delta":19.801987,"title":"Hold","type":"float"} |
| ch.21.dyn.knee | {"tap":false,"min":0.0,"max":5.0,"delta":1.0,"title":"Knee","type":"float"} |
| ch.21.dyn.mix | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":5.0,"title":"Mix","type":"float"} |
| ch.21.dyn.mode | {"enums":[{"name":"Comp","id":0},{"name":"Expand","id":1}],"title":"Mode","type":"enum"} |
| ch.21.dyn.on | {"type":"boolean"} |
| ch.21.dyn.ratio | {"enums":[{"name":"1.1","id":0},{"name":"1.3","id":1},{"name":"1.5","id":2},{"name":"2.0","id":3},{"name":"2.5","id":4},{"name":"3.0","id":5},{"name":"4.0","id":6},{"name":"5.0","id":7},{"name":"7.0","id":8},{"name":"10","id":9},{"name":"20","id":10},{"name":"100","id":11}],"title":"Ratio","type":"enum"} |
| ch.21.dyn.release | {"unit":" ms","tap":false,"min":5.0,"max":4000.0007,"delta":39.603966,"title":"Release","type":"float"} |
| ch.21.dyn.thr | {"unit":" dB","tap":false,"min":-60.0,"max":0.0,"delta":0.0,"title":"Thr","type":"float"} |
| ch.21.grp.dca.0 | {"type":"boolean"} |
| ch.21.grp.dca.1 | {"type":"boolean"} |
| ch.21.grp.dca.2 | {"type":"boolean"} |
| ch.21.grp.dca.3 | {"type":"boolean"} |
| ch.21.grp.mute.0 | {"type":"boolean"} |
| ch.21.grp.mute.1 | {"type":"boolean"} |
| ch.21.grp.mute.2 | {"type":"boolean"} |
| ch.21.grp.mute.3 | {"type":"boolean"} |
| ch.21.info.isActive | {"type":"boolean"} |
| ch.21.info.isStereo | {"type":"boolean"} |
| ch.21.insX.0.on | {"type":"boolean"} |
| ch.21.levelData.-1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.21.levelData.-1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.21.levelData.-1.on | {"type":"boolean"} |
| ch.21.levelData.-1.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.21.link.linked | {"type":"boolean"} |
| ch.21.mix.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.21.mix.on | {"type":"boolean"} |
| ch.21.mix.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.21.mix.rawOn | {"type":"boolean"} |
| ch.21.mix.stOn | {"type":"boolean"} |
| ch.21.peq.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.bands.0.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.bands.0.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.bands.0.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.peq.bands.1.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.bands.1.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.bands.1.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.bands.1.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.peq.bands.2.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.bands.2.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.bands.2.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.bands.2.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.peq.bands.3.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.bands.3.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.bands.3.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.bands.3.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.peq.bands.4.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.bands.4.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.bands.4.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.bands.4.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.peq.bands.5.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.bands.5.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.bands.5.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.bands.5.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.peq.on | {"type":"boolean"} |
| ch.21.peq.selBand.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.21.peq.selBand.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.21.peq.selBand.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.21.peq.selBand.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.21.rawEq.model | {"enums":[{"name":"PEQ","id":0},{"name":"GEQ","id":1},{"name":"TEQ","id":2}],"title":"Model","type":"enum"} |
| ch.21.solo | {"type":"boolean"} |
| ch.27.cfg.color | {"enums":[{"name":"Black","id":0},{"name":"Red","id":1},{"name":"Green","id":2},{"name":"Yellow","id":3},{"name":"Blue","id":4},{"name":"Magenta","id":5},{"name":"Cyan","id":6},{"name":"White","id":7},{"name":"Black Inv","id":8},{"name":"Red Inv","id":9},{"name":"Green Inv","id":10},{"name":"Yellow Inv","id":11},{"name":"Blue Inv","id":12},{"name":"Magenta Inv","id":13},{"name":"Cyan Inv","id":14},{"name":"White Inv","id":15}],"title":"Color","type":"enum"} |
| ch.27.cfg.icon | {"unit":"","tap":false,"min":0.0,"max":73.0,"delta":1.0,"title":"Icon","type":"integer"} |
| ch.27.cfg.name | {"type":"string","constraints":["ASCII text","Max length 12"]} |
| ch.27.grp.dca.0 | {"type":"boolean"} |
| ch.27.grp.dca.1 | {"type":"boolean"} |
| ch.27.grp.dca.2 | {"type":"boolean"} |
| ch.27.grp.dca.3 | {"type":"boolean"} |
| ch.27.grp.mute.0 | {"type":"boolean"} |
| ch.27.grp.mute.1 | {"type":"boolean"} |
| ch.27.grp.mute.2 | {"type":"boolean"} |
| ch.27.grp.mute.3 | {"type":"boolean"} |
| ch.27.info.isActive | {"type":"boolean"} |
| ch.27.info.isStereo | {"type":"boolean"} |
| ch.27.levelData.-1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.27.levelData.-1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.27.levelData.-1.on | {"type":"boolean"} |
| ch.27.mix.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.27.mix.on | {"type":"boolean"} |
| ch.27.mix.rawOn | {"type":"boolean"} |
| ch.27.solo | {"type":"boolean"} |
| ch.31.cfg.color | {"enums":[{"name":"Black","id":0},{"name":"Red","id":1},{"name":"Green","id":2},{"name":"Yellow","id":3},{"name":"Blue","id":4},{"name":"Magenta","id":5},{"name":"Cyan","id":6},{"name":"White","id":7},{"name":"Black Inv","id":8},{"name":"Red Inv","id":9},{"name":"Green Inv","id":10},{"name":"Yellow Inv","id":11},{"name":"Blue Inv","id":12},{"name":"Magenta Inv","id":13},{"name":"Cyan Inv","id":14},{"name":"White Inv","id":15}],"title":"Color","type":"enum"} |
| ch.31.cfg.icon | {"unit":"","tap":false,"min":0.0,"max":73.0,"delta":1.0,"title":"Icon","type":"integer"} |
| ch.31.cfg.name | {"type":"string","constraints":["ASCII text","Max length 12"]} |
| ch.31.dyn.attack | {"unit":" ms","tap":false,"min":0.0,"max":120.0,"delta":1.0,"title":"Attack","type":"float"} |
| ch.31.dyn.autoTime | {"type":"boolean"} |
| ch.31.dyn.detection | {"type":"boolean"} |
| ch.31.dyn.envelope | {"type":"boolean"} |
| ch.31.dyn.filter.filters.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.31.dyn.filter.filters.bands.0.on | {"type":"boolean"} |
| ch.31.dyn.filter.filters.bands.0.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.31.dyn.filter.filters.on | {"type":"boolean"} |
| ch.31.dyn.filter.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.31.dyn.filter.on | {"type":"boolean"} |
| ch.31.dyn.filter.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.31.dyn.gain | {"unit":" dB","tap":false,"min":0.0,"max":24.0,"delta":0.5,"title":"Gain","type":"float"} |
| ch.31.dyn.hold | {"unit":" ms","tap":false,"min":0.020000001,"max":2000.0007,"delta":19.801987,"title":"Hold","type":"float"} |
| ch.31.dyn.knee | {"tap":false,"min":0.0,"max":5.0,"delta":1.0,"title":"Knee","type":"float"} |
| ch.31.dyn.mix | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":5.0,"title":"Mix","type":"float"} |
| ch.31.dyn.mode | {"enums":[{"name":"Comp","id":0},{"name":"Expand","id":1}],"title":"Mode","type":"enum"} |
| ch.31.dyn.on | {"type":"boolean"} |
| ch.31.dyn.ratio | {"enums":[{"name":"1.1","id":0},{"name":"1.3","id":1},{"name":"1.5","id":2},{"name":"2.0","id":3},{"name":"2.5","id":4},{"name":"3.0","id":5},{"name":"4.0","id":6},{"name":"5.0","id":7},{"name":"7.0","id":8},{"name":"10","id":9},{"name":"20","id":10},{"name":"100","id":11}],"title":"Ratio","type":"enum"} |
| ch.31.dyn.release | {"unit":" ms","tap":false,"min":5.0,"max":4000.0007,"delta":39.603966,"title":"Release","type":"float"} |
| ch.31.dyn.thr | {"unit":" dB","tap":false,"min":-60.0,"max":0.0,"delta":0.0,"title":"Thr","type":"float"} |
| ch.31.info.isActive | {"type":"boolean"} |
| ch.31.info.isStereo | {"type":"boolean"} |
| ch.31.insX.0.on | {"type":"boolean"} |
| ch.31.levelData.-1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.31.levelData.-1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.31.levelData.-1.on | {"type":"boolean"} |
| ch.31.levelData.-1.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.31.mix.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.31.mix.on | {"type":"boolean"} |
| ch.31.mix.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.31.mix.rawOn | {"type":"boolean"} |
| ch.31.peq.levels.0 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.1 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.10 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.11 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.12 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.13 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.14 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.15 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.16 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.17 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.18 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.19 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.2 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.20 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.21 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.22 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.23 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.24 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.25 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.26 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.27 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.28 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.29 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.3 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.30 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.4 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.5 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.6 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.7 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.8 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.levels.9 | {"tap":false,"min":-15.0,"max":15.0,"delta":0.25,"title":"Gain","type":"float"} |
| ch.31.peq.on | {"type":"boolean"} |
| ch.31.rawEq.model | {"enums":[{"name":"PEQ","id":0},{"name":"GEQ","id":1},{"name":"TEQ","id":2}],"title":"Model","type":"enum"} |
| ch.31.solo | {"type":"boolean"} |
| fx.cfg.0.ins | {"type":"boolean"} |
| fx.cfg.1.ins | {"type":"boolean"} |
| fx.cfg.2.ins | {"type":"boolean"} |
| fx.cfg.3.ins | {"type":"boolean"} |
| fx.rack.0.crossfeed | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"CrossFeed","type":"enum"} |
| fx.rack.0.dry | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"Dry","type":"enum"} |
| fx.rack.0.factorA | {"enums":[{"name":"1/4","id":0},{"name":"3/8","id":1},{"name":"1/2","id":2},{"name":"2/3","id":3},{"name":"1","id":4},{"name":"4/3","id":5},{"name":"3/2","id":6},{"name":"2","id":7},{"name":"3","id":8}],"title":"Factor A","type":"enum"} |
| fx.rack.0.factorB | {"enums":[{"name":"1/4","id":0},{"name":"3/8","id":1},{"name":"1/2","id":2},{"name":"2/3","id":3},{"name":"1","id":4},{"name":"4/3","id":5},{"name":"3/2","id":6},{"name":"2","id":7},{"name":"3","id":8}],"title":"Factor B","type":"enum"} |
| fx.rack.0.factorC | {"enums":[{"name":"1/4","id":0},{"name":"3/8","id":1},{"name":"1/2","id":2},{"name":"2/3","id":3},{"name":"1","id":4},{"name":"4/3","id":5},{"name":"3/2","id":6},{"name":"2","id":7},{"name":"3","id":8}],"title":"Factor C","type":"enum"} |
| fx.rack.0.fbk | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Feedback","type":"float"} |
| fx.rack.0.gainA | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain A","type":"float"} |
| fx.rack.0.gainB | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain B","type":"float"} |
| fx.rack.0.gainBase | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain Base","type":"float"} |
| fx.rack.0.gainC | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain C","type":"float"} |
| fx.rack.0.hi | {"unit":" Hz","tap":false,"min":199.99997,"max":20000.008,"delta":400.00015,"title":"Hi-Cut","type":"float"} |
| fx.rack.0.lc | {"unit":" Hz","tap":false,"min":10.0,"max":499.99982,"delta":9.999996,"title":"Lo Cut","type":"float"} |
| fx.rack.0.mono | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"Mono","type":"enum"} |
| fx.rack.0.spread | {"unit":"","tap":false,"min":0.0,"max":6.0,"delta":1.0,"title":"Spread","type":"float"} |
| fx.rack.0.t | {"unit":" ms","tap":true,"min":1.0,"max":3000.0,"delta":1.0003334,"title":"Time","type":"float"} |
| fx.rack.1.decay | {"unit":" s","tap":true,"min":0.1,"max":19.999996,"delta":0.39999992,"title":"Decay","type":"float"} |
| fx.rack.1.dens | {"unit":"","tap":false,"min":1.0,"max":30.0,"delta":1.0344827,"title":"Density","type":"float"} |
| fx.rack.1.erLeft | {"unit":" ms","tap":true,"min":0.0,"max":200.0,"delta":2.0,"title":"ER Left","type":"float"} |
| fx.rack.1.erLevel | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"ER Level","type":"float"} |
| fx.rack.1.erRight | {"unit":" ms","tap":true,"min":0.0,"max":200.0,"delta":2.0,"title":"ER Right","type":"float"} |
| fx.rack.1.freeze | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"Freeze","type":"enum"} |
| fx.rack.1.hi | {"unit":" Hz","tap":false,"min":199.99997,"max":20000.008,"delta":400.00015,"title":"Hi-Cut","type":"float"} |
| fx.rack.1.hiMulti | {"unit":"","tap":false,"min":0.1,"max":10.0,"delta":0.19999999,"title":"Hi Multi","type":"float"} |
| fx.rack.1.lc | {"unit":" Hz","tap":false,"min":10.0,"max":499.99982,"delta":9.999996,"title":"Lo Cut","type":"float"} |
| fx.rack.1.loMulti | {"unit":"","tap":false,"min":0.1,"max":10.0,"delta":0.19999999,"title":"Lo Multi","type":"float"} |
| fx.rack.1.lvl | {"unit":" dB","tap":false,"min":-12.0,"max":12.0,"delta":0.25,"title":"Level","type":"float"} |
| fx.rack.1.revDelay | {"unit":" ms","tap":true,"min":0.0,"max":200.0,"delta":2.0,"title":"Rev Delay","type":"float"} |
| fx.rack.1.size | {"unit":"","tap":false,"min":2.0,"max":100.0,"delta":2.0408163,"title":"Size","type":"float"} |
| fx.rack.2.crossFeed | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"Cross Feed","type":"enum"} |
| fx.rack.2.dry | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"Dry","type":"enum"} |
| fx.rack.2.factorA | {"enums":[{"name":"1/4","id":0},{"name":"3/8","id":1},{"name":"1/2","id":2},{"name":"2/3","id":3},{"name":"1","id":4},{"name":"4/3","id":5},{"name":"3/2","id":6},{"name":"2","id":7},{"name":"3","id":8}],"title":"Factor A","type":"enum"} |
| fx.rack.2.factorB | {"enums":[{"name":"1/4","id":0},{"name":"3/8","id":1},{"name":"1/2","id":2},{"name":"2/3","id":3},{"name":"1","id":4},{"name":"4/3","id":5},{"name":"3/2","id":6},{"name":"2","id":7},{"name":"3","id":8}],"title":"Factor B","type":"enum"} |
| fx.rack.2.fbk | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Feedback","type":"float"} |
| fx.rack.2.gBase | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain Base","type":"float"} |
| fx.rack.2.gainA | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain A","type":"float"} |
| fx.rack.2.gainB | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Gain B","type":"float"} |
| fx.rack.2.hi | {"unit":" Hz","tap":false,"min":199.99997,"max":20000.008,"delta":400.00015,"title":"Hi-Cut","type":"float"} |
| fx.rack.2.lc | {"unit":" Hz","tap":false,"min":10.0,"max":499.99982,"delta":9.999996,"title":"Lo Cut","type":"float"} |
| fx.rack.2.mono | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"Mono","type":"enum"} |
| fx.rack.2.pBase | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Pan Base","type":"float"} |
| fx.rack.2.panA | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan A","type":"float"} |
| fx.rack.2.panB | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan B","type":"float"} |
| fx.rack.2.t | {"unit":" ms","tap":true,"min":1.0,"max":3000.0,"delta":10.003335,"title":"Time","type":"float"} |
| fx.rack.3.attack | {"unit":" ms","tap":false,"min":10.0,"max":1000.0,"delta":20.0,"title":"Attack","type":"float"} |
| fx.rack.3.base | {"unit":"","tap":false,"min":0.0,"max":50.0,"delta":2.0,"title":"Base","type":"float"} |
| fx.rack.3.depth | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Depth","type":"float"} |
| fx.rack.3.envMod | {"unit":" %","tap":false,"min":-100.0,"max":100.0,"delta":2.5,"title":"Env Mod","type":"float"} |
| fx.rack.3.hold | {"unit":" ms","tap":false,"min":1.0,"max":1999.9996,"delta":39.999992,"title":"Hold","type":"float"} |
| fx.rack.3.mix | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Mix","type":"float"} |
| fx.rack.3.phase | {"unit":"","tap":false,"min":0.0,"max":180.0,"delta":5.0,"title":"Phase","type":"float"} |
| fx.rack.3.release | {"unit":" ms","tap":false,"min":10.0,"max":1000.0,"delta":20.0,"title":"Release","type":"float"} |
| fx.rack.3.reso | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":2.0,"title":"Reso","type":"float"} |
| fx.rack.3.speed | {"unit":" Hz","tap":true,"min":0.049999993,"max":4.9999995,"delta":0.09999999,"title":"Speed","type":"float"} |
| fx.rack.3.stages | {"unit":"","tap":false,"min":2.0,"max":12.0,"delta":1.2,"title":"Stages","type":"float"} |
| fx.rack.3.wave | {"unit":"","tap":false,"min":-50.0,"max":50.0,"delta":2.5,"title":"Wave","type":"float"} |
| monitor.busAfl | {"type":"boolean"} |
| monitor.ch.0.dim.lvl | {"tap":false,"min":-40.0,"max":0.0,"delta":0.0,"title":"Dim","type":"float"} |
| monitor.ch.0.dim.on | {"type":"boolean"} |
| monitor.ch.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| monitor.ch.0.mute | {"type":"boolean"} |
| monitor.ch.0.src.src | {"enums":[{"name":"Off","id":0},{"name":"LR","id":1},{"name":"LR PFL","id":2},{"name":"LR AFL","id":3},{"name":"Aux","id":4},{"name":"USB 17/18","id":5},{"name":"Bus 1","id":6},{"name":"Bus 2","id":7},{"name":"Bus 3","id":8},{"name":"Bus 4","id":9},{"name":"Bus 5","id":10},{"name":"Bus 6","id":11},{"name":"Bus 1/2","id":12},{"name":"Bus 3/4","id":13},{"name":"Bus 5/6","id":14}],"title":"Source","type":"enum"} |
| monitor.ch.0.src.trim | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| monitor.chAfl | {"type":"boolean"} |
| monitor.dimPfl | {"type":"boolean"} |
| monitor.mono | {"type":"boolean"} |

## METERING_AND_STATUS
Native meters use int32 little-endian count followed by int16 little-endian /256 dB values in the current decoder. Meter bank 1 has 40 tentative labels; other banks remain index-only. No meters sampled. The implementation deduplicates identical frames and does not enforce freshness, so its mean is not a time-weighted mean. MS metering format is a separate protocol: see subscription schemas; legacy binary data is base64, big-endian int16 /100. Do not reuse native decoding for MS payloads. App state and console identity are control metadata, not audio evidence.
