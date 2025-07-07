label avg12551:
stop music

play music "ED6103.ogg"
scene avg_bg_023
window show
with fade_out
c0 '[textdict[1153001]]'
c0 '[textdict[1153002]]'
show oc002_01 2 as p2 at l(-3), light, zorder 6
c21 '[textdict[1153003]]'
hide p2
show oc002_01 2 as p2 at l(-3), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1153004]]'
hide p2
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show oc002_01 8 as p2 at l(-3), light, zorder 6
c21 '[textdict[1153005]]'
hide p2
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show oc003_01 5 as p3 at l(-6), light, zorder 6
play sfxvoice "avg_vocal_ro05.ogg"
c31 '[textdict[1153006]]'
hide p1
hide p3
show oc003_01 5 as p3 at l(-6), dark, zorder 6
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1153007]]'
hide p4
hide p3
show oc003_01 5 as p3 at l(-6), dark, zorder 6
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1153008]]'
hide p3
hide p4
c0 '[textdict[1153009]]'
return