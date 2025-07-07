label avg101604:
stop music

scene placeholderbackground
show sc008_01 2 as p16 at l(-18), light, zorder 6
window show
with fade_out
c161 '[textdict[1221539]]'
hide p16
show sc008_01 2 as p16 at l(-18), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221540]]'
hide p16
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc008_01 4 as p16 at l(-18), light, zorder 6
c161 '[textdict[1221541]]'
menu:
    extend ""
    "[textdict[1221542]]":
        call avg101605
    "[textdict[1221543]]":
        call avg101606
    "[textdict[1221547]]":
        call avg101607
return