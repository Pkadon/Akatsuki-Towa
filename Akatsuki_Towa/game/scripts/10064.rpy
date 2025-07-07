label avg10064:
stop music

play music "ED6103.ogg"
scene avg_bg_038
show oc001_01 1 as p1 at l(-2), light, zorder 6
window show
with fade_out
play sfx2 "common_menu.ogg"
c11 '[textdict[1005000]]'
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show sc007_01 1 as p15 at r(-17), light, zorder 5
c153 '[textdict[1005001]]'
hide p15
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1005002]]'
hide p1
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
show oc001_01 7 as p1 at l(-2), light, zorder 6
c11 '[textdict[1005003]]'
hide p2
hide p1
show oc001_01 7 as p1 at l(-2), dark, zorder 6
show oc004_01 7 as p4 at r(-5), light, zorder 5
c43 '[textdict[1005004]]'
hide p4
hide p1
show oc001_01 7 as p1 at l(-2), dark, zorder 6
show sc039_01 5 as p46 at r(-13), light, zorder 5
c463 '[textdict[1005005]]'
hide p1
hide p46
show sc039_01 5 as p46 at r(-13), dark, zorder 5
show oc001_01 10 as p1 at l(-2), light, zorder 6
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1005006]]'
hide p46
hide p1
show oc001_01 10 as p1 at l(-2), dark, zorder 6
show oc002_01 8 as p2 at r(-3), light, zorder 5
c23 '[textdict[1005007]]'
return