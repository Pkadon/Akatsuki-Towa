label avg101825:
stop music

scene placeholderbackground
show oc001_01 4 as p1 at r(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1222226]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc010_01 4 as p18 at l(-10), light, flip, zorder 6
c181 '[textdict[1222227]]'
hide p18
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show sc010_01 4 as p18 at l(-10), light, flip, zorder 6
c181 '[textdict[1222228]]'
menu:
    extend ""
    "[textdict[1222229]]":
        call avg101826
    "[textdict[1222230]]":
        call avg101827
    "[textdict[1222231]]":
        call avg101828
return