label avg25287:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20230 '[textdict[str(1211098)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25288
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6019.ogg"
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211102)]]'
play sfxvoice "bcv_oc002_c02_01.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211103)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211104)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211105)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 3 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211106)]]'
play sfxvoice "avg_vocal_ch22.ogg"
hide c1portrait
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211107)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211108)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211109)]]'
hide c1portrait
c20230 '[textdict[str(1211110)]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211111)]]'
hide c2portrait
c20230 '[textdict[str(1211112)]]'
play sfx2 "fight_6018.ogg"
c00 '[textdict[str(1211113)]]'
play sfxvoice "avg_vocal_ch17.ogg"
show oc002_01 11 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211114)]]'
play sfx2 "common_36rewardsp.ogg"
hide c2portrait
c20230 '[textdict[str(1211115)]]'
return