label avg12507:
stop music

play music "ed7113.ogg"
scene avg_bg_021
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1150909]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1150910]]'
return