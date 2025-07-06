label avg101804:
stop music

scene placeholderbackground
with fade
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222166]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc010_01 1 as p18 at l(-10), light, zorder 6
c181 '[textdict[1222167]]'
hide p18
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc010_01 4 as p18 at l(-10), light, zorder 6
c181 '[textdict[1222168]]'
menu:
    extend ""
    "[textdict[1222169]]":
        call avg101805
    "[textdict[1222170]]":
        call avg101806
    "[textdict[1222171]]":
        call avg101807
return