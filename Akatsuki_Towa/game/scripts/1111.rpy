label avg1111:
stop music

play music "ed7201.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[2102762]]'
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[2102763]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc004_01 1 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[2102764]]'
hide p1
hide p4
show oc004_01 1 as p4 at l(-5), dark, flip, zorder 6
show st004_01 5 as p204 at r(4), light, zorder 5
c2043 '[textdict[2102765]]'
hide p204
hide p4
show oc004_01 1 as p4 at l(-5), dark, flip, zorder 6
c9773 '[textdict[2102766]]'
hide p4
show oc004_01 1 as p4 at l(-5), light, flip, zorder 6
play sfx2 "other_7013.ogg"
c41 '[textdict[2102767]]'
return