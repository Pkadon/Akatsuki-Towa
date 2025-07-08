label avg29026:
stop music

play music "ED6104.ogg"
scene avg_bg_027
show oc001_01 4 as p1 at mid(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1100014]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg29027
    "[textdict[1215000]]":
        call avg29025
return