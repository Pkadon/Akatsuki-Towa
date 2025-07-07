label avg101621:
stop music

scene placeholderbackground
show sc008_01 3 as p16 at l(-18), light, zorder 6
window show
with fade_out
c161 '[textdict[1221586]]'
hide p16
show sc008_01 3 as p16 at l(-18), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221587]]'
hide p16
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc008_01 1 as p16 at l(-18), light, zorder 6
c161 '[textdict[1221588]]'
menu:
    extend ""
    "[textdict[1221589]]":
        call avg101622
    "[textdict[1221590]]":
        call avg101623
    "[textdict[1221591]]":
        call avg101624
return