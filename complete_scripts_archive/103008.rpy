label avg103008:
stop music

stop music
scene placeholderbackground
with fade
show sc022_01 1 as p30 at l(-9), light, zorder 5
c301 '[textdict[1222432]]'
stop music
hide p30
show sc022_01 1 as p30 at l(-9), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222433]]'
stop music
hide p30
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc022_01 1 as p30 at l(-9), light, zorder 5
c301 '[textdict[1222434]]'
stop music
hide p1
hide p30
show sc022_01 1 as p30 at l(-9), dark, zorder 6
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222435]]'
menu:
    extend ""
    "[textdict[1222436]]":
        call avg103009
    "[textdict[1222437]]":
        call avg103010
    "[textdict[1222438]]":
        call avg103011
return