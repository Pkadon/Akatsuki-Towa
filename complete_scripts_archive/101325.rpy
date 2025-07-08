label avg101325:
stop music

scene placeholderbackground
show oc001_01 17 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1221024]]'
hide p1
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221025]]'
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc005_01 2 as p13 at l(-17), light, flip, zorder 6
c131 '[textdict[1221026]]'
hide p13
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc005_01 5 as p13 at l(-17), light, flip, zorder 6
c131 '[textdict[1221027]]'
menu:
    extend ""
    "[textdict[1221028]]":
        call avg101326
    "[textdict[1221029]]":
        call avg101327
    "[textdict[1221030]]":
        call avg101328
return