label avg29034:

play music "ED6104.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1100018]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg29035
    "[textdict[1215000]]":
        call avg29025
return