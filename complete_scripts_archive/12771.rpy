label avg12771:
stop music

play music "ED6202.ogg"
scene avg_bg_010
show oc003_01 1 as p3 at r(-6), light, zorder 5
window show
with fade_out
c33 '[textdict[1175632]]'
hide p3
show oc003_01 1 as p3 at r(-6), dark, zorder 5
show oc002_01 5 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1175633]]'
hide p3
hide p2
show oc002_01 5 as p2 at l(-3), dark, flip, zorder 6
show st061_01 5 as p1304 at r(-2), light, zorder 5
c13043 '[textdict[1175634]]'
hide p2
hide p1304
show st061_01 5 as p1304 at r(-2), dark, zorder 5
show oc004_01 1 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1175635]]'
hide p1304
hide p4
show oc004_01 1 as p4 at l(-5), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1175636]]'
return