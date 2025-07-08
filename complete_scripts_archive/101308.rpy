label avg101308:
stop music

scene placeholderbackground
show oc001_01 22 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1220970]]'
hide p1
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220971]]'
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc005_01 1 as p13 at l(-17), light, flip, zorder 6
c131 '[textdict[1220972]]'
hide p1
hide p13
show sc005_01 1 as p13 at l(-17), dark, flip, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220973]]'
menu:
    extend ""
    "[textdict[1220974]]":
        call avg101309
    "[textdict[1220975]]":
        call avg101310
    "[textdict[1220976]]":
        call avg101311
return