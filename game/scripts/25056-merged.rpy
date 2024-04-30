label avg25056:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na15.ogg"
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210163)]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210164)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210165)]]'
menu:
    "[textdict[str(1214997)]]":
        call avg25057
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210167)]]'
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210168)]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210169)]]'
play sfxvoice "avg_vocal_ch24.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210170)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210171)]]'
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210172)]]'
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210173)]]'
menu:
    "[textdict[str(1214998)]]":
        call avg25080
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch22.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210174)]]'
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210175)]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210176)]]'
return