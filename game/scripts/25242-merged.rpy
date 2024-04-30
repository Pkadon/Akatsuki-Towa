label avg25242:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20240 '[textdict[str(1210880)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25243
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6025.ogg"
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210885)]]'
play sfxvoice "avg_vocal_ch08.ogg"
hide c1portrait
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210886)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210887)]]'
play sfx2 "fight_6025.ogg"
hide c1portrait
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210888)]]'
play sfxvoice "avg_vocal_na17.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210889)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na16.ogg"
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210890)]]'
hide c1portrait
c20240 '[textdict[str(1210891)]]'
play sfxvoice "avg_vocal_ch29.ogg"
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210892)]]'
hide c2portrait
c20240 '[textdict[str(1210893)]]'
play sfx2 "common_36rewardsp.ogg"
show oc001_01 21 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210894)]]'
return