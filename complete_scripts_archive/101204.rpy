label avg101204:
stop music

scene placeholderbackground
show oc001_01 8 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1220670]]'
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show sc004_01 2 as p12 at l(-12), light, zorder 6
c121 '[textdict[1220671]]'
hide p1
hide p12
show sc004_01 2 as p12 at l(-12), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220672]]'
menu:
    extend ""
    "[textdict[1220673]]":
        call avg101205
    "[textdict[1220674]]":
        call avg101206
    "[textdict[1220675]]":
        call avg101207
return