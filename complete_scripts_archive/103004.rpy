label avg103004:
stop music

scene placeholderbackground
show sc022_01 1 as p30 at l(-9), light, zorder 6
window show
with fade_out
c301 '[textdict[1222419]]'
hide p30
show sc022_01 1 as p30 at l(-9), dark, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222420]]'
hide p30
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc022_01 4 as p30 at l(-9), light, zorder 6
c301 '[textdict[1222421]]'
hide p1
hide p30
show sc022_01 4 as p30 at l(-9), dark, zorder 6
show oc001_01 7 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222422]]'
hide p1
hide p30
show sc022_01 4 as p30 at l(-9), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222423]]'
hide p30
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc022_01 5 as p30 at l(-9), light, zorder 6
c301 '[textdict[1222424]]'
menu:
    extend ""
    "[textdict[1222425]]":
        call avg103005
    "[textdict[1222426]]":
        call avg103006
    "[textdict[1222427]]":
        call avg103007
return