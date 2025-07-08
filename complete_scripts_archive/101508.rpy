label avg101508:
stop music

scene placeholderbackground
show sc007_01 1 as p15 at l(-17), light, flip, zorder 6
window show
with fade_out
c151 '[textdict[1221281]]'
hide p15
show sc007_01 1 as p15 at l(-17), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221282]]'
hide p15
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc007_01 5 as p15 at l(-17), light, flip, zorder 6
c151 '[textdict[1221283]]'
hide p1
hide p15
show sc007_01 5 as p15 at l(-17), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221284]]'
menu:
    extend ""
    "[textdict[1221285]]":
        call avg101509
    "[textdict[1221286]]":
        call avg101510
    "[textdict[1221287]]":
        call avg101511
return