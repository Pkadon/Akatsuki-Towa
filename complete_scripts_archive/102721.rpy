label avg102721:
stop music

scene placeholderbackground
show sc019_01 2 as p27 at l(-18), light, zorder 6
window show
with fade_out
c271 '[textdict[1219497]]'
hide p27
show sc019_01 2 as p27 at l(-18), dark, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219498]]'
hide p27
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc019_01 1 as p27 at l(-18), light, zorder 6
c271 '[textdict[1219499]]'
menu:
    extend ""
    "[textdict[1219500]]":
        call avg102722
    "[textdict[1219501]]":
        call avg102723
    "[textdict[1219502]]":
        call avg102724
return