label avg12540:
stop music

play music "ED6105.ogg"
scene avg_bg_010
window show
with fade_out
c0 '[textdict[1152912]]'
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1152913]]'
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show oc004_01 4 as p4 at l(-5), light, zorder 6
c41 '[textdict[1152914]]'
hide p1
hide p4
show oc004_01 4 as p4 at l(-5), dark, zorder 6
show oc002_01 10 as p2 at r(-3), light, zorder 5
c23 '[textdict[1152915]]'
hide p2
hide p4
show oc004_01 4 as p4 at l(-5), dark, zorder 6
show oc002_01 8 as p2 at r(-3), r_shake, light, zorder 5
c23 '[textdict[1152916]]'
hide p2
hide p4
show oc004_01 4 as p4 at l(-5), dark, zorder 6
show oc001_01 8 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1152917]]'
return