label avg12680:
stop music

play music "ed7203.ogg"
scene avg_bg_070
show oc003_01 4 as p3 at l(-6), light, flip, zorder 6
window show
with fade_in
c31 '[textdict[1166980]]'
hide p3
show oc003_01 4 as p3 at l(-6), dark, flip, zorder 6
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1166981]]'
hide p3
hide p4
show oc004_01 4 as p4 at r(-5), dark, zorder 5
show oc002_01 8 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1166982]]'
hide p4
hide p2
show oc002_01 8 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 7 as p1 at r(-2), light, zorder 5
c13 '[textdict[1166983]]'
hide p2
hide p1
show oc001_01 7 as p1 at r(-2), dark, zorder 5
show oc004_01 8 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1166984]]'
hide p4
hide p1
show oc001_01 7 as p1 at r(-2), dark, zorder 5
show oc003_01 4 as p3 at l(-6), light, flip, zorder 6
play sfx2 "other_7080.ogg"
c31 '[textdict[1166985]]'
hide p1
hide p3
show oc003_01 4 as p3 at l(-6), dark, flip, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
play sfx2 "fight_6024.ogg"
c13 '[textdict[1166986]]'
return