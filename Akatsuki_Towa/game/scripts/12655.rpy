label avg12655:
stop music

play music "ED6300.ogg"
scene avg_bg_070
show oc001_01 4 as p1 at r(-2), light, zorder 5
with fade
c13 '[textdict[1166365]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc002_01 2 as p2 at l(-3), light, zorder 6
c21 '[textdict[1166366]]'
hide p1
hide p2
show oc002_01 2 as p2 at l(-3), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
play sfx2 "other_7043.ogg"
c13 '[textdict[1166367]]'
hide p1
hide p2
show oc002_01 2 as p2 at l(-3), dark, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1166368]]'
hide p2
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc003_01 5 as p3 at l(-6), light, zorder 6
c31 '[textdict[1166369]]'
hide p3
hide p1
play sfx2 "other_7045.ogg"
c0 '[textdict[1166370]]'
show oc003_01 1 as p3 at l(-6), light, zorder 6
c31 '[textdict[1166371]]'
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1166372]]'
return