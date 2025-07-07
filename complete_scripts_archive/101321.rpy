label avg101321:
stop music

scene placeholderbackground
show oc001_01 4 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1221012]]'
hide p1
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221013]]'
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc005_01 1 as p13 at l(-17), light, zorder 6
c131 '[textdict[1221014]]'
hide p13
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc005_01 2 as p13 at l(-17), light, zorder 6
c131 '[textdict[1221015]]'
hide p1
hide p13
show sc005_01 2 as p13 at l(-17), dark, zorder 6
show oc001_01 18 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221016]]'
menu:
    extend ""
    "[textdict[1221017]]":
        call avg101322
    "[textdict[1221018]]":
        call avg101323
    "[textdict[1221019]]":
        call avg101324
return