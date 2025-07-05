label avg12603:
stop music

play music "ED6200.ogg"
scene avg_bg_080
with fade
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1161143]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc003_01 4 as p3 at l(-6), light, zorder 6
c31 '[textdict[1161144]]'
hide p1
hide p3
show oc003_01 4 as p3 at l(-6), dark, zorder 6
show oc002_01 4 as p2 at r(-3), r_shake, light, zorder 5
c23 '[textdict[1161145]]'
hide p3
hide p2
show oc002_01 4 as p2 at r(-3), dark, zorder 5
show oc003_01 1 as p3 at l(-6), light, zorder 6
c31 '[textdict[1161146]]'
hide p2
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show oc004_01 1 as p4 at r(-5), light, zorder 5
c43 '[textdict[1161147]]'
return