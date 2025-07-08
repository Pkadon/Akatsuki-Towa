label avg102108:
stop music

scene placeholderbackground
show sc013_01 5 as p21 at l(-12), light, flip, zorder 6
window show
with fade_in
c211 '[textdict[1218830]]'
hide p21
show sc013_01 5 as p21 at l(-12), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218831]]'
hide p21
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc013_01 1 as p21 at l(-12), light, flip, zorder 6
c211 '[textdict[1218832]]'
menu:
    extend ""
    "[textdict[1218833]]":
        call avg102109
    "[textdict[1218834]]":
        call avg102110
    "[textdict[1218835]]":
        call avg102111
return