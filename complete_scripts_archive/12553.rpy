label avg12553:
stop music

play music "ED6523.ogg"
scene avg_bg_081
window show
with fade_out
c12411 '[textdict[1153036]]'
c12423 '[textdict[1153037]]'
c12431 '[textdict[1153038]]'
c12443 '[textdict[1153039]]'
c12451 '[textdict[1153040]]'
show oc001_01 4 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1153041]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc003_01 5 as p3 at l(-6), light, flip, zorder 6
c31 '[textdict[1153042]]'
hide p1
hide p3
show oc003_01 5 as p3 at l(-6), dark, flip, zorder 6
show oc004_01 7 as p4 at r(-5), light, zorder 5
c43 '[textdict[1153043]]'
hide p4
hide p3
show oc003_01 5 as p3 at l(-6), dark, flip, zorder 6
show oc002_01 8 as p2 at r(-3), r_shake, light, zorder 5
c23 '[textdict[1153044]]'
hide p3
hide p2
with fade
c12411 '[textdict[1153045]]'
return