label avg12318:

play music "ed7302.ogg"
scene avg_bg_052
$ update_portrait('oc002_01 3', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1133325]]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
c13 '[textdict[1133326]]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 4', 'p57', [l(-19), light, flip], 6)
c571 '[textdict[1133327]]'
hide p57
hide p1
play sfx2 "other_7085.ogg"
c0 '[textdict[1133328]]'
return