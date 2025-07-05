label avg20112:
stop music

play music "ed7150.ogg"
scene avg_bg_038
with fade
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1005447]]'
hide p2
show oc002_01 2 as p2 at r(-3), dark, zorder 5
show oc001_01 8 as p1 at l(-2), light, zorder 6
c11 '[textdict[1001032]]'
menu:
    extend ""
    "[textdict[1005449]]":
        call avg10092
    "[textdict[1005450]]":
        call avg10094
return