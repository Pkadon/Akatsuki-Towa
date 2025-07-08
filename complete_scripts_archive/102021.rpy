label avg102021:
stop music

scene placeholderbackground
show sc012_01 4 as p20 at l(-16), light, flip, zorder 6
window show
with fade_in
c201 '[textdict[1218685]]'
hide p20
show sc012_01 4 as p20 at l(-16), dark, flip, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218686]]'
hide p20
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc012_01 1 as p20 at l(-16), light, flip, zorder 6
c201 '[textdict[1218687]]'
menu:
    extend ""
    "[textdict[1218688]]":
        call avg102022
    "[textdict[1218689]]":
        call avg102023
    "[textdict[1218690]]":
        call avg102024
return