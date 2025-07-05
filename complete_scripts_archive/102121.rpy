label avg102121:
stop music

stop music
scene placeholderbackground
with fade
show sc013_01 3 as p21 at l(-12), light, zorder 6
c211 '[textdict[1218869]]'
stop music
hide p21
show sc013_01 3 as p21 at l(-12), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218870]]'
stop music
hide p21
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc013_01 3 as p21 at l(-12), light, zorder 6
c211 '[textdict[1218871]]'
menu:
    extend ""
    "[textdict[1218872]]":
        call avg102122
    "[textdict[1218873]]":
        call avg102123
    "[textdict[1218874]]":
        call avg102124
return