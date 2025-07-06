label avg101608:
stop music

scene placeholderbackground
with fade
show sc008_01 1 as p16 at l(-18), light, zorder 6
c161 '[textdict[1221549]]'
hide p16
show sc008_01 1 as p16 at l(-18), dark, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221550]]'
hide p16
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc008_01 4 as p16 at l(-18), light, zorder 6
c161 '[textdict[1221551]]'
menu:
    extend ""
    "[textdict[1221552]]":
        call avg101609
    "[textdict[1221553]]":
        call avg101610
    "[textdict[1221554]]":
        call avg101611
return