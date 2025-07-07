label avg29028:
stop music

play music "ED6104.ogg"
scene avg_bg_027
show oc001_01 18 as p1 at mid(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1100015]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg29029
    "[textdict[1215000]]":
        call avg29025
return