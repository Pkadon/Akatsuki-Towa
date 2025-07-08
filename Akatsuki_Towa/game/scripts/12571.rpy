label avg12571:
stop music

play music "ED6200.ogg"
scene avg_bg_010
show oc001_01 4 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1155153]]'
hide p1
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1155154]]'
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show oc004_01 24 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1155155]]'
return