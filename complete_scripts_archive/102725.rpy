label avg102725:
stop music

scene placeholderbackground
show oc001_01 2 as p1 at r(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1219507]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc019_01 1 as p27 at l(-18), light, flip, zorder 6
c271 '[textdict[1219508]]'
hide p27
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc019_01 4 as p27 at l(-18), light, flip, zorder 6
c271 '[textdict[1219509]]'
menu:
    extend ""
    "[textdict[1219510]]":
        call avg102726
    "[textdict[1219511]]":
        call avg102727
    "[textdict[1219512]]":
        call avg102728
return