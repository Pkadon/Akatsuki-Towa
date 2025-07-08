label avg102125:
stop music

scene placeholderbackground
show sc013_01 3 as p21 at l(-12), light, flip, zorder 6
window show
with fade_out
c211 '[textdict[1218879]]'
hide p21
show sc013_01 3 as p21 at l(-12), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218880]]'
hide p21
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc013_01 1 as p21 at l(-12), light, flip, zorder 6
c211 '[textdict[1218881]]'
menu:
    extend ""
    "[textdict[1218882]]":
        call avg102126
    "[textdict[1218883]]":
        call avg102127
    "[textdict[1218884]]":
        call avg102128
return