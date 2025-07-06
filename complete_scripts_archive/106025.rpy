label avg106025:
stop music

scene placeholderbackground
with fade
show sc053_01 1 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219120]]'
hide p60
show sc053_01 5 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219121]]'
hide p60
show sc053_01 5 as p60 at l(-32), dark, zorder 6
show oc001_01 22 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219122]]'
hide p60
hide p1
show oc001_01 22 as p1 at r(-2), dark, zorder 5
show sc053_01 2 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219123]]'
menu:
    extend ""
    "[textdict[1219124]]":
        call avg106026
    "[textdict[1219125]]":
        call avg106027
    "[textdict[1219126]]":
        call avg106028
return