label avg102025:
stop music

scene placeholderbackground
show sc012_01 4 as p20 at l(-16), light, zorder 6
with fade
c201 '[textdict[1218695]]'
hide p20
show sc012_01 4 as p20 at l(-16), dark, zorder 6
show oc001_01 7 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218696]]'
hide p20
hide p1
show oc001_01 7 as p1 at r(-2), dark, zorder 5
show sc012_01 1 as p20 at l(-16), light, zorder 6
c201 '[textdict[1218697]]'
menu:
    extend ""
    "[textdict[1218698]]":
        call avg102026
    "[textdict[1218699]]":
        call avg102027
    "[textdict[1218700]]":
        call avg102028
return