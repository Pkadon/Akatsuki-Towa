label avg12638:
stop music

play music "ed7203.ogg"
scene avg_bg_070
show oc002_01 3 as p2 at r(-3), light, zorder 5
window show
with fade_in
play sfx2 "fight_6019.ogg"
c23 '[textdict[1162984]]'
hide p2
show oc002_01 3 as p2 at r(-3), dark, zorder 5
show oc004_01 4 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1162985]]'
hide p2
hide p4
show oc004_01 4 as p4 at l(-5), dark, flip, zorder 6
show oc003_01 4 as p3 at r(-6), light, zorder 5
c33 '[textdict[1162986]]'
hide p4
hide p3
show oc003_01 4 as p3 at r(-6), dark, zorder 5
c13251 '[textdict[1162987]]'
return