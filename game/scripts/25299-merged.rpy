label avg25299:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20250 '[textdict[str(1211156)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25300
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7088.ogg"
c20260 '[textdict[str(1211161)]]'
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211162)]]'
hide c2portrait
c20260 '[textdict[str(1211163)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6024.ogg"
c20270 '[textdict[str(1211164)]]'
play sfxvoice "avg_vocal_ch05.ogg"
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211165)]]'
hide c2portrait
c20270 '[textdict[str(1211166)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
c20280 '[textdict[str(1211167)]]'
play sfxvoice "avg_vocal_ch17.ogg"
show oc002_01 10 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211168)]]'
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na06.ogg"
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211169)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211170)]]'
hide c2portrait
c20250 '[textdict[str(1211171)]]'
play sfxvoice "avg_vocal_na10.ogg"
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211172)]]'
play sfx2 "common_36rewardsp.ogg"
hide c1portrait
c20250 '[textdict[str(1211173)]]'
return