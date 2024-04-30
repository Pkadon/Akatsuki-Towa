label avg25319:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20240 '[textdict[str(1211235)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25320
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_na10.ogg"
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211241)]]'
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
hide c1portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211242)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211243)]]'
play sfxvoice "avg_vocal_ch08.ogg"
hide c1portrait
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211244)]]'
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_na18.ogg"
hide c2portrait
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211245)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211246)]]'
hide c1portrait
c20240 '[textdict[str(1211247)]]'
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211248)]]'
hide c2portrait
c20240 '[textdict[str(1211249)]]'
play sfxvoice "avg_vocal_na21.ogg"
show oc001_01 12 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211250)]]'
hide c1portrait
c20240 '[textdict[str(1211251)]]'
c20240 '[textdict[str(1211252)]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211253)]]'
return