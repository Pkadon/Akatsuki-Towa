label avg12601:
stop music

play music "ED6102.ogg"
scene avg_bg_023
show oc001_01 1 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1161118]]'
hide p1
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1161119]]'
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
c12321 '[textdict[1161120]]'
hide p2
show oc002_01 12 as p2 at r(-3), r_shake, light, zorder 5
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1161121]]'
hide p2
show oc003_01 4 as p3 at r(-6), light, zorder 5
c33 '[textdict[1161122]]'
hide p3
show oc003_01 4 as p3 at r(-6), dark, zorder 5
c12321 '[textdict[1161123]]'
hide p3
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1161124]]'
hide p4
show oc004_01 4 as p4 at r(-5), dark, zorder 5
c12321 '[textdict[1161125]]'
hide p4
show oc004_01 4 as p4 at r(-5), dark, zorder 5
c12321 '[textdict[1161126]]'
hide p4
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1161127]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc003_01 4 as p3 at l(-6), light, zorder 6
c31 '[textdict[1161128]]'
hide p3
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
c12321 '[textdict[1161129]]'
hide p1
show oc002_01 9 as p2 at r(-3), r_shake, light, zorder 5
c23 '[textdict[1161130]]'
return