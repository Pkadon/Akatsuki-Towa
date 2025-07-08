label avg102808:
stop music

scene placeholderbackground
show oc001_01 10 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1219734]]'
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc020_01 5 as p28 at l(-10), light, flip, zorder 6
c281 '[textdict[1219735]]'
hide p1
hide p28
show sc020_01 5 as p28 at l(-10), dark, flip, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219736]]'
menu:
    extend ""
    "[textdict[1219737]]":
        call avg102809
    "[textdict[1219738]]":
        call avg102810
    "[textdict[1219739]]":
        call avg102811
return