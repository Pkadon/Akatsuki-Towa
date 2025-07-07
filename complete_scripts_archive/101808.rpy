label avg101808:
stop music

scene placeholderbackground
show sc010_01 1 as p18 at l(-10), light, zorder 6
window show
with fade_out
c181 '[textdict[1222176]]'
hide p18
show sc010_01 1 as p18 at l(-10), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1222177]]'
hide p18
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc010_01 4 as p18 at l(-10), light, zorder 6
c181 '[textdict[1222178]]'
menu:
    extend ""
    "[textdict[1222179]]":
        call avg101809
    "[textdict[1222180]]":
        call avg101810
    "[textdict[1222181]]":
        call avg101811
return