label avg102704:
stop music

scene placeholderbackground
show oc001_01 2 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1219451]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc019_01 3 as p27 at l(-18), light, zorder 6
c271 '[textdict[1219452]]'
hide p27
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc019_01 1 as p27 at l(-18), light, zorder 6
c271 '[textdict[1219453]]'
menu:
    extend ""
    "[textdict[1219454]]":
        call avg102705
    "[textdict[1219455]]":
        call avg102706
    "[textdict[1219456]]":
        call avg102707
return