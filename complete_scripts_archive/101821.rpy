label avg101821:
stop music

scene placeholderbackground
show oc001_01 19 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1222215]]'
hide p1
show oc001_01 19 as p1 at r(-2), dark, zorder 5
show sc010_01 4 as p18 at l(-10), light, zorder 6
c181 '[textdict[1222216]]'
hide p18
hide p1
show oc001_01 19 as p1 at r(-2), dark, zorder 5
show sc010_01 1 as p18 at l(-10), light, zorder 6
c181 '[textdict[1222217]]'
menu:
    extend ""
    "[textdict[1222218]]":
        call avg101822
    "[textdict[1222219]]":
        call avg101823
    "[textdict[1222220]]":
        call avg101824
return