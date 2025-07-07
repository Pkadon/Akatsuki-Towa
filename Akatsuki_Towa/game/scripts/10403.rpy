label avg10403:
stop music

play music "ED6518.ogg"
scene avg_bg_001
show oc001_01 4 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1140280]]'
hide p1
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1140282]]'
menu:
    extend ""
    "[textdict[1140283]]":
        call avg10404
    "[textdict[1140284]]":
        call avg10405
return