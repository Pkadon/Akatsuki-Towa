label avg12546:
stop music

play music "ED6105.ogg"
scene avg_bg_010
with fade
show oc001_01 17 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1152959]]'
hide p1
show oc001_01 17 as p1 at r(-2), dark, zorder 5
show oc002_01 10 as p2 at l(-3), light, zorder 6
c21 '[textdict[1152960]]'
hide p2
hide p1
show oc001_01 17 as p1 at r(-2), dark, zorder 5
show oc003_01 17 as p3 at l(-6), light, zorder 6
c31 '[textdict[1152961]]'
hide p1
hide p3
show oc003_01 17 as p3 at l(-6), dark, zorder 6
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1152962]]'
return