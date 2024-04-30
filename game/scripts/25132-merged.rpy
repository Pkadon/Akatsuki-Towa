label avg25132:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20130 '[textdict[str(1210399)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25133
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na18.ogg"
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210405)]]'
play sfxvoice "avg_vocal_ch08.ogg"
hide c1portrait
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210406)]]'
play sfx2 "other_7088.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210407)]]'
play sfxvoice "avg_vocal_ch06.ogg"
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210408)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc001_01 21 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210409)]]'
hide c1portrait
c20130 '[textdict[str(1210410)]]'
play sfxvoice "avg_vocal_ch10.ogg"
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210411)]]'
hide c2portrait
c20130 '[textdict[str(1210412)]]'
play sfxvoice "avg_vocal_ch05.ogg"
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210413)]]'
play sfx2 "other_7039.ogg"
hide c2portrait
c20130 '[textdict[str(1210414)]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na17.ogg"
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210415)]]'
return