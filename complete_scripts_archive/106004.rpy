label avg106004:
stop music

stop music
scene placeholderbackground
with fade
show sc053_01 2 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219056]]'
stop music
hide p60
show sc053_01 2 as p60 at l(-32), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219057]]'
stop music
hide p60
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc053_01 1 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219058]]'
stop music
hide p60
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc053_01 4 as p60 at l(-32), light, zorder 6
c601 '[textdict[1219059]]'
menu:
    extend ""
    "[textdict[1219060]]":
        call avg106005
    "[textdict[1219061]]":
        call avg106006
    "[textdict[1219062]]":
        call avg106007
return