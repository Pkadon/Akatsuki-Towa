label avg102925:
stop music

scene placeholderbackground
show oc001_01 1 as p1 at r(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1219964]]'
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc021_01 4 as p29 at l(-17), light, flip, zorder 6
c291 '[textdict[1219965]]'
hide p29
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc021_01 3 as p29 at l(-17), light, flip, zorder 6
c291 '[textdict[1219966]]'
menu:
    extend ""
    "[textdict[1219967]]":
        call avg102926
    "[textdict[1219968]]":
        call avg102927
    "[textdict[1219969]]":
        call avg102928
return