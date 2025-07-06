label avg102004:
stop music

scene placeholderbackground
with fade
show sc012_01 2 as p20 at l(-16), light, zorder 6
c201 '[textdict[1218639]]'
hide p20
show sc012_01 2 as p20 at l(-16), dark, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218640]]'
hide p20
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc012_01 4 as p20 at l(-16), light, zorder 6
c201 '[textdict[1218641]]'
menu:
    extend ""
    "[textdict[1218642]]":
        call avg102005
    "[textdict[1218643]]":
        call avg102006
    "[textdict[1218644]]":
        call avg102007
return