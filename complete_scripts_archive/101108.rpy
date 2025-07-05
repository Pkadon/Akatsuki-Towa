label avg101108:
stop music

stop music
scene placeholderbackground
with fade
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220409]]'
stop music
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc003_01 1 as p11 at l(-4), light, zorder 6
c111 '[textdict[1220410]]'
stop music
hide p1
hide p11
show sc003_01 1 as p11 at l(-4), dark, zorder 6
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220411]]'
menu:
    extend ""
    "[textdict[1220412]]":
        call avg101109
    "[textdict[1220413]]":
        call avg101110
    "[textdict[1220414]]":
        call avg101111
return