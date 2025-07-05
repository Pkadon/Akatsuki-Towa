label avg101125:
stop music

stop music
scene placeholderbackground
with fade
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220456]]'
stop music
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc003_01 2 as p11 at l(-4), light, zorder 6
c111 '[textdict[1220457]]'
stop music
hide p1
hide p11
show sc003_01 2 as p11 at l(-4), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220458]]'
menu:
    extend ""
    "[textdict[1220459]]":
        call avg101126
    "[textdict[1220460]]":
        call avg101127
    "[textdict[1220461]]":
        call avg101128
return