label avg12177:
stop music

play music "ED6104.ogg"
scene avg_bg_038
with fade
c0 '[textdict[1120544]]'
show oc001_01 8 as p1 at l(-2), light, zorder 6
c11 '[textdict[1120545]]'
hide p1
show oc001_01 8 as p1 at l(-2), dark, zorder 6
show oc003_01 7 as p3 at r(-6), light, zorder 5
c33 '[textdict[1120546]]'
hide p1
hide p3
show oc003_01 7 as p3 at r(-6), dark, zorder 5
show oc002_01 14 as p2 at l(-3), l_shake, light, zorder 6
c21 '[textdict[1120547]]'
hide p2
hide p3
show oc003_01 7 as p3 at r(-6), dark, zorder 5
show oc001_01 1 as p1 at l(-2), light, zorder 6
c11 '[textdict[1120548]]'
hide p3
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show oc002_01 10 as p2 at r(-3), light, zorder 5
c23 '[textdict[1120549]]'
hide p1
hide p2
show oc002_01 10 as p2 at r(-3), dark, zorder 5
show oc001_01 10 as p1 at l(-2), light, zorder 6
c11 '[textdict[1120550]]'
play sfx2 "common_remind.ogg"
hide p1
hide p2
c0 '[textdict[1120551]]'
show oc002_01 8 as p2 at r(-3), light, zorder 5
c23 '[textdict[1120552]]'
return