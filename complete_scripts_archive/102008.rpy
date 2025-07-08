label avg102008:
stop music

scene placeholderbackground
show sc012_01 4 as p20 at l(-16), light, flip, zorder 6
window show
with fade_out
c201 '[textdict[1218649]]'
hide p20
show sc012_01 4 as p20 at l(-16), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218650]]'
hide p20
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc012_01 1 as p20 at l(-16), light, flip, zorder 6
c201 '[textdict[1218651]]'
menu:
    extend ""
    "[textdict[1218652]]":
        call avg102009
    "[textdict[1218653]]":
        call avg102010
    "[textdict[1218654]]":
        call avg102011
return