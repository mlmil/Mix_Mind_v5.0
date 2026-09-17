# CHANNEL_STRIP_PARAMETER_MAP

## MODEL
Input strips expose config, source routing, processing, mix, sends, groups, linking and solo. Availability differs by strip type. Below is the exact representative input-strip schema; all other concrete paths and their definitions are in the JSON map. Definition ranges describe API values, not recommended operating levels.

## REPRESENTATIVE_INPUT_CH0
| Path | Definition |
| --- | --- |
| ch.0.amm.mode | {"enums":[{"name":"Off","id":0},{"name":"X","id":1},{"name":"Y","id":2}],"title":"Group","type":"enum"} |
| ch.0.amm.weight | {"tap":false,"min":-12.0,"max":12.0,"delta":0.25,"title":"Weight","type":"float"} |
| ch.0.cfg.color | {"enums":[{"name":"Black","id":0},{"name":"Red","id":1},{"name":"Green","id":2},{"name":"Yellow","id":3},{"name":"Blue","id":4},{"name":"Magenta","id":5},{"name":"Cyan","id":6},{"name":"White","id":7},{"name":"Black Inv","id":8},{"name":"Red Inv","id":9},{"name":"Green Inv","id":10},{"name":"Yellow Inv","id":11},{"name":"Blue Inv","id":12},{"name":"Magenta Inv","id":13},{"name":"Cyan Inv","id":14},{"name":"White Inv","id":15}],"title":"Color","type":"enum"} |
| ch.0.cfg.icon | {"unit":"","tap":false,"min":0.0,"max":73.0,"delta":1.0,"title":"Icon","type":"integer"} |
| ch.0.cfg.name | {"type":"string","constraints":["ASCII text","Max length 12"]} |
| ch.0.cfg.srcSel | {"enums":[{"name":"Off","id":0},{"name":"On","id":1}],"title":"On/Off","type":"enum"} |
| ch.0.dyn.attack | {"unit":" ms","tap":false,"min":0.0,"max":120.0,"delta":1.0,"title":"Attack","type":"float"} |
| ch.0.dyn.autoTime | {"type":"boolean"} |
| ch.0.dyn.detection | {"type":"boolean"} |
| ch.0.dyn.envelope | {"type":"boolean"} |
| ch.0.dyn.filter.filters.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.dyn.filter.filters.bands.0.on | {"type":"boolean"} |
| ch.0.dyn.filter.filters.bands.0.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.0.dyn.filter.filters.on | {"type":"boolean"} |
| ch.0.dyn.filter.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.dyn.filter.on | {"type":"boolean"} |
| ch.0.dyn.filter.src | {"enums":[{"name":"MATT","id":0},{"name":"MATT","id":1},{"name":"KYLE A","id":2},{"name":"ALFRED","id":3},{"name":"GUITAR","id":4},{"name":"BOH CLICK","id":5},{"name":"FULL L","id":6},{"name":"KYLE B","id":7},{"name":"MIKE","id":8},{"name":"BASS","id":9},{"name":"BOH CUES","id":10},{"name":"MIDI DRUMS","id":11},{"name":"KICK TRIG","id":12},{"name":"FULL R","id":13},{"name":"DAVE","id":14},{"name":"KICK MIC","id":15},{"name":"KEYS","id":16},{"name":"KYLE","id":17},{"name":"MIKE","id":18},{"name":"ALFRED","id":19},{"name":"MATT","id":20},{"name":"DAVE","id":21},{"name":"SUB","id":22}],"title":"Src","type":"enum"} |
| ch.0.dyn.filter.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.0.dyn.gain | {"unit":" dB","tap":false,"min":0.0,"max":24.0,"delta":0.5,"title":"Gain","type":"float"} |
| ch.0.dyn.hold | {"unit":" ms","tap":false,"min":0.020000001,"max":2000.0007,"delta":19.801987,"title":"Hold","type":"float"} |
| ch.0.dyn.knee | {"tap":false,"min":0.0,"max":5.0,"delta":1.0,"title":"Knee","type":"float"} |
| ch.0.dyn.mix | {"unit":" %","tap":false,"min":0.0,"max":100.0,"delta":5.0,"title":"Mix","type":"float"} |
| ch.0.dyn.mode | {"enums":[{"name":"Comp","id":0},{"name":"Expand","id":1}],"title":"Mode","type":"enum"} |
| ch.0.dyn.on | {"type":"boolean"} |
| ch.0.dyn.ratio | {"enums":[{"name":"1.1","id":0},{"name":"1.3","id":1},{"name":"1.5","id":2},{"name":"2.0","id":3},{"name":"2.5","id":4},{"name":"3.0","id":5},{"name":"4.0","id":6},{"name":"5.0","id":7},{"name":"7.0","id":8},{"name":"10","id":9},{"name":"20","id":10},{"name":"100","id":11}],"title":"Ratio","type":"enum"} |
| ch.0.dyn.release | {"unit":" ms","tap":false,"min":5.0,"max":4000.0007,"delta":39.603966,"title":"Release","type":"float"} |
| ch.0.dyn.thr | {"unit":" dB","tap":false,"min":-60.0,"max":0.0,"delta":0.0,"title":"Thr","type":"float"} |
| ch.0.gate.attack | {"unit":" ms","tap":false,"min":0.0,"max":120.0,"delta":1.0,"title":"Attack","type":"float"} |
| ch.0.gate.filter.filters.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.gate.filter.filters.bands.0.on | {"type":"boolean"} |
| ch.0.gate.filter.filters.bands.0.type | {"enums":[{"name":"Lo-Cut 6dB","id":7},{"name":"Lo-Cut 12dB","id":8},{"name":"Hi-Cut 6dB","id":11},{"name":"Hi-Cut 12dB","id":12},{"name":"Q 1.0","id":101},{"name":"Q 2.0","id":102},{"name":"Q 3.0","id":103},{"name":"Q 5.0","id":105},{"name":"Q 10.0","id":110}],"title":"Type","type":"enum"} |
| ch.0.gate.filter.filters.on | {"type":"boolean"} |
| ch.0.gate.filter.src | {"enums":[{"name":"MATT","id":0},{"name":"MATT","id":1},{"name":"KYLE A","id":2},{"name":"ALFRED","id":3},{"name":"GUITAR","id":4},{"name":"BOH CLICK","id":5},{"name":"FULL L","id":6},{"name":"KYLE B","id":7},{"name":"MIKE","id":8},{"name":"BASS","id":9},{"name":"BOH CUES","id":10},{"name":"MIDI DRUMS","id":11},{"name":"KICK TRIG","id":12},{"name":"FULL R","id":13},{"name":"DAVE","id":14},{"name":"KICK MIC","id":15},{"name":"KEYS","id":16},{"name":"KYLE","id":17},{"name":"MIKE","id":18},{"name":"ALFRED","id":19},{"name":"MATT","id":20},{"name":"DAVE","id":21},{"name":"SUB","id":22}],"title":"Src","type":"enum"} |
| ch.0.gate.hold | {"unit":" ms","tap":false,"min":0.020000001,"max":2000.0007,"delta":19.801987,"title":"Hold","type":"float"} |
| ch.0.gate.mode | {"enums":[{"name":"Gate","id":0},{"name":"Duck","id":1},{"name":"Exp 2","id":2},{"name":"Exp 3","id":3},{"name":"Exp 4","id":4}],"title":"Mode","type":"enum"} |
| ch.0.gate.model | {"enums":[{"name":"Gate","id":0},{"name":"Duck","id":1}],"title":"Model","type":"enum"} |
| ch.0.gate.on | {"type":"boolean"} |
| ch.0.gate.range | {"unit":" dB","tap":false,"min":3.0,"max":60.0,"delta":1.0526316,"title":"Range","type":"float"} |
| ch.0.gate.ratio | {"enums":[{"name":"Gate","id":0},{"name":"Exp 2","id":1},{"name":"Exp 3","id":2},{"name":"Exp 4","id":3}],"title":"Ratio","type":"enum"} |
| ch.0.gate.release | {"unit":" ms","tap":false,"min":5.0,"max":4000.0007,"delta":39.603966,"title":"Release","type":"float"} |
| ch.0.gate.thr | {"unit":" dB","tap":false,"min":-80.0,"max":0.0,"delta":0.0,"title":"Thr","type":"float"} |
| ch.0.grp.dca.0 | {"type":"boolean"} |
| ch.0.grp.dca.1 | {"type":"boolean"} |
| ch.0.grp.dca.2 | {"type":"boolean"} |
| ch.0.grp.dca.3 | {"type":"boolean"} |
| ch.0.grp.mute.0 | {"type":"boolean"} |
| ch.0.grp.mute.1 | {"type":"boolean"} |
| ch.0.grp.mute.2 | {"type":"boolean"} |
| ch.0.grp.mute.3 | {"type":"boolean"} |
| ch.0.headamp.gain | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| ch.0.info.isActive | {"type":"boolean"} |
| ch.0.info.isStereo | {"type":"boolean"} |
| ch.0.insX.0.on | {"type":"boolean"} |
| ch.0.levelData.-1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.-1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.-1.on | {"type":"boolean"} |
| ch.0.levelData.-1.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.0.levelData.-2.level | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| ch.0.levelData.-2.lvl | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| ch.0.levelData.0.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.1.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.2.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.2.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.3.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.3.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.4.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.4.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.5.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.5.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.6.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.6.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.7.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.7.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.8.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.8.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.9.level | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.levelData.9.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.link.linked | {"type":"boolean"} |
| ch.0.mix.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.on | {"type":"boolean"} |
| ch.0.mix.pan | {"unit":"","tap":false,"min":-100.0,"max":100.0,"delta":0.5,"title":"Pan","type":"float"} |
| ch.0.mix.rawOn | {"type":"boolean"} |
| ch.0.mix.sends.0.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.0.on | {"type":"boolean"} |
| ch.0.mix.sends.0.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.1.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.1.on | {"type":"boolean"} |
| ch.0.mix.sends.1.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.2.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.2.on | {"type":"boolean"} |
| ch.0.mix.sends.2.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.3.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.3.on | {"type":"boolean"} |
| ch.0.mix.sends.3.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.4.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.4.on | {"type":"boolean"} |
| ch.0.mix.sends.4.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.5.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.5.on | {"type":"boolean"} |
| ch.0.mix.sends.5.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5},{"name":"Group","id":6}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.6.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.6.on | {"type":"boolean"} |
| ch.0.mix.sends.6.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.7.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.7.on | {"type":"boolean"} |
| ch.0.mix.sends.7.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.8.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.8.on | {"type":"boolean"} |
| ch.0.mix.sends.8.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.0.mix.sends.9.lvl | {"unit":" dB","tap":false,"min":-90.0,"max":10.0,"delta":0.0050000004,"title":"Level","type":"float"} |
| ch.0.mix.sends.9.on | {"type":"boolean"} |
| ch.0.mix.sends.9.tap | {"enums":[{"name":"IN","id":0},{"name":"Pre EQ","id":2},{"name":"Post EQ","id":3},{"name":"Pre Fader","id":4},{"name":"Post Fader","id":5}],"title":"Tap","type":"enum"} |
| ch.0.mix.stOn | {"type":"boolean"} |
| ch.0.peq.bands.0.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.peq.bands.0.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.0.peq.bands.0.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.0.peq.bands.0.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.0.peq.bands.1.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.peq.bands.1.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.0.peq.bands.1.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.0.peq.bands.1.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.0.peq.bands.2.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.peq.bands.2.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.0.peq.bands.2.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.0.peq.bands.2.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.0.peq.bands.3.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.peq.bands.3.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.0.peq.bands.3.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.0.peq.bands.3.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.0.peq.on | {"type":"boolean"} |
| ch.0.peq.selBand.freq | {"unit":" Hz","tap":false,"min":20.000002,"max":20000.008,"delta":100.00004,"title":"Freq","type":"float"} |
| ch.0.peq.selBand.gain | {"unit":" dB","tap":false,"min":-15.0,"max":15.0,"delta":0.125,"title":"Gain","type":"float"} |
| ch.0.peq.selBand.q | {"tap":false,"min":0.3,"max":10.0,"delta":0.1388889,"title":"Q","type":"float"} |
| ch.0.peq.selBand.type | {"enums":[{"name":"Hi-Cut","id":2},{"name":"Hi-Shelf","id":5},{"name":"VEQ","id":1},{"name":"PEQ","id":0},{"name":"Lo-Shelf","id":4},{"name":"Lo-Cut","id":3}],"title":"Type","type":"enum"} |
| ch.0.preamp.filter.0.freq | {"tap":false,"min":20.0,"max":400.0,"delta":3.960396,"title":"Lowcut","type":"float"} |
| ch.0.preamp.filter.0.on | {"type":"boolean"} |
| ch.0.preamp.inv | {"type":"boolean"} |
| ch.0.preamp.retOn | {"type":"boolean"} |
| ch.0.preamp.retTrim | {"unit":" dB","tap":false,"min":-18.0,"max":18.0,"delta":0.125,"title":"Trim","type":"float"} |
| ch.0.rawEq.model | {"enums":[{"name":"PEQ","id":0}],"title":"","type":"enum"} |
| ch.0.routing.srcCfg.0 | {"enums":[{"name":"None - None","id":0},{"name":"In 1-8 - In 1","id":1},{"name":"In 1-8 - In 2","id":2},{"name":"In 1-8 - In 3","id":3},{"name":"In 1-8 - In 4","id":4},{"name":"In 1-8 - In 5","id":5},{"name":"In 1-8 - In 6","id":6},{"name":"In 1-8 - In 7","id":7},{"name":"In 1-8 - In 8","id":8},{"name":"In 9-16 - In 9","id":9},{"name":"In 9-16 - In 10","id":10},{"name":"In 9-16 - In 11","id":11},{"name":"In 9-16 - In 12","id":12},{"name":"In 9-16 - In 13","id":13},{"name":"In 9-16 - In 14","id":14},{"name":"In 9-16 - In 15","id":15},{"name":"In 9-16 - In 16","id":16},{"name":"Aux - Aux L","id":17},{"name":"Aux - Aux R","id":18}],"title":"Signal sources","type":"enum"} |
| ch.0.routing.srcCfg.1 | {"enums":[{"name":"USB - U 1","id":0},{"name":"USB - U 2","id":1},{"name":"USB - U 3","id":2},{"name":"USB - U 4","id":3},{"name":"USB - U 5","id":4},{"name":"USB - U 6","id":5},{"name":"USB - U 7","id":6},{"name":"USB - U 8","id":7},{"name":"USB - U 9","id":8},{"name":"USB - U 10","id":9},{"name":"USB - U 11","id":10},{"name":"USB - U 12","id":11},{"name":"USB - U 13","id":12},{"name":"USB - U 14","id":13},{"name":"USB - U 15","id":14},{"name":"USB - U 16","id":15},{"name":"USB - U 17","id":16},{"name":"USB - U 18","id":17}],"title":"Signal sources","type":"enum"} |
| ch.0.solo | {"type":"boolean"} |

## NATIVE_PROCESSING
Native groups include config/preamp/gate/dyn/insert/eq/mix/grp/automix. EQ band counts differ by strip. Native send slots 01..06 target buses; 07..10 target FX sends. `mix/on` uses 1=unmuted. Headamp ownership follows the physical analog source, not necessarily the strip number. The channel-detail tool currently reads headamp using the strip number; treat that association as unverified when sources are remapped. Parameter definitions do not prove processing order or tap behavior.
