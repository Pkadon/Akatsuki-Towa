label avg25192:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7041.ogg"
c20130 '[textdict[str(1210646)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25193
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
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210652)]]'
play sfxvoice "avg_vocal_ch05.ogg"
hide c1portrait
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210653)]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210654)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210655)]]'
play sfx2 "other_7039.ogg"
hide c1portrait
c20130 '[textdict[str(1210656)]]'
play sfx2 "other_7092.ogg"
c00 '[textdict[str(1210657)]]'
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210658)]]'
hide c2portrait
show oc001_01 10 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210659)]]'
hide c1portrait
c20130 '[textdict[str(1210660)]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na16.ogg"
show oc001_01 21 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210661)]]'
return