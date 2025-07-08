label avg12377:
stop music

play music "ed9999.ogg"
scene avg_bg_058
show oc001_01 8 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1134079]]'
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show oc002_01 2 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1134080]]'
hide p1
hide p2
show oc002_01 2 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1134081]]'
return