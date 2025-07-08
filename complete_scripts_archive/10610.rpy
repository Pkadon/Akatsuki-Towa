label avg10610:
stop music

scene avg_bg_010
window show
with fade_out
play sfx2 "other_7060.ogg"
c0 '[textdict[1160413]]'
play music "ED6202.ogg"
show oc003_01 4 as p3 at l(-6), light, flip, zorder 6
play sfx2 "other_7060.ogg"
c31 '[textdict[1160414]]'
hide p3
show oc003_01 4 as p3 at l(-6), dark, flip, zorder 6
show oc004_01 4 as p4 at r(-5), light, zorder 5
c43 '[textdict[1160415]]'
hide p3
hide p4
show oc004_01 4 as p4 at r(-5), dark, zorder 5
show oc002_01 21 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1160416]]'
hide p4
hide p2
show oc002_01 21 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1160417]]'
play music "ed7511.ogg"
hide p1
hide p2
show oc002_01 21 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 4 as p1 at r(-2), r_shake, light, zorder 5
play sfx2 "other_7079.ogg"
c13 '[textdict[1160418]]'
hide p1
hide p2
show oc002_01 21 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 9 as p1 at r(-2), light, zorder 5
c13 '[textdict[1160419]]'
return