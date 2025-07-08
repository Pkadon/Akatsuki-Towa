label avg1010:
stop music

play music "ed7106.ogg"
scene avg_bg_023
show sc049_01 1 as p56 at l(-8), light, flip, zorder 6
window show
with fade_in
c561 '[textdict[2100125]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, flip, zorder 6
c561 '[textdict[2100126]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, flip, zorder 6
c561 '[textdict[2100127]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, flip, zorder 6
c561 '[textdict[2100128]]'
menu:
    extend ""
    "[textdict[2100129]]":
        call avg1011
    "[textdict[2100130]]":
        call avg1012
    "[textdict[2100131]]":
        call avg1013
return