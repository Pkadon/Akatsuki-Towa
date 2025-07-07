label avg1002:
stop music

play music "ed7106.ogg"
scene avg_bg_023
window show
with fade_out
c0 '[textdict[2100030]]'
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100031]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100032]]'
hide p56
show sc049_01 1 as p56 at l(-8), light, zorder 6
c561 '[textdict[2100033]]'
menu:
    extend ""
    "[textdict[2100034]]":
        call avg1003
    "[textdict[2100035]]":
        call avg1004
    "[textdict[2100036]]":
        call avg1005
return