label avg103021:
stop music

scene placeholderbackground
show sc022_01 4 as p30 at l(-9), light, zorder 6
with fade
c301 '[textdict[1222471]]'
hide p30
show sc022_01 4 as p30 at l(-9), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222472]]'
hide p30
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc022_01 1 as p30 at l(-9), light, zorder 6
c301 '[textdict[1222473]]'
hide p1
hide p30
show sc022_01 1 as p30 at l(-9), dark, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222474]]'
hide p30
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc022_01 5 as p30 at l(-9), light, zorder 6
c301 '[textdict[1222475]]'
hide p30
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc022_01 1 as p30 at l(-9), light, zorder 6
c301 '[textdict[1222476]]'
menu:
    extend ""
    "[textdict[1222477]]":
        call avg103022
    "[textdict[1222478]]":
        call avg103023
    "[textdict[1222479]]":
        call avg103024
return