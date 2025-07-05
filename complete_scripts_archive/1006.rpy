label avg1006:
stop music

play music "ed7106.ogg"
scene avg_bg_023
with fade
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100084]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100085]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100086]]'
hide p56
show sc049_01 1 as p56 at l(-8), dark, zorder 6
show oc001_01 17 as p1 at r(-2), light, zorder 5
c13 '[textdict[2100087]]'
hide p56
hide p1
show oc001_01 17 as p1 at r(-2), dark, zorder 5
show sc049_01 4 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100088]]'
hide p56
hide p1
show oc001_01 17 as p1 at r(-2), dark, zorder 5
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100089]]'
menu:
    extend ""
    "[textdict[2100091]]":
        call avg1007
    "[textdict[2100092]]":
        call avg1008
    "[textdict[2100093]]":
        call avg1009
return