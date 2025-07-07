label avg10515:
stop music

play music "ED6200.ogg"
scene avg_bg_010
show oc003_01 5 as p3 at l(-6), light, zorder 6
window show
with fade_out
c31 '[textdict[1150607]]'
hide p3
show oc003_01 5 as p3 at l(-6), dark, zorder 6
show oc002_01 8 as p2 at r(-3), light, zorder 5
c23 '[textdict[1150608]]'
hide p3
hide p2
show oc002_01 8 as p2 at r(-3), dark, zorder 5
show oc004_01 4 as p4 at l(-5), light, zorder 6
c41 '[textdict[1150609]]'
hide p2
hide p4
show oc004_01 4 as p4 at l(-5), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1150610]]'
return