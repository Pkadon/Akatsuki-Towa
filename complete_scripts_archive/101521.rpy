label avg101521:
stop music

scene placeholderbackground
show sc007_01 3 as p15 at l(-17), light, flip, zorder 6
window show
with fade_in
c151 '[textdict[1221319]]'
hide p15
show sc007_01 3 as p15 at l(-17), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221320]]'
hide p15
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc007_01 2 as p15 at l(-17), light, flip, zorder 6
c151 '[textdict[1221321]]'
hide p15
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc007_01 3 as p15 at l(-17), light, flip, zorder 6
c151 '[textdict[1221322]]'
hide p1
hide p15
show sc007_01 3 as p15 at l(-17), dark, flip, zorder 6
show oc001_01 7 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221323]]'
menu:
    extend ""
    "[textdict[1221324]]":
        call avg101522
    "[textdict[1221325]]":
        call avg101523
    "[textdict[1221326]]":
        call avg101524
return