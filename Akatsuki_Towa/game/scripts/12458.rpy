label avg12458:
stop music

play music "ed7102.ogg"
scene avg_bg_022
window show
with fade_in
c0 '[textdict[1143729]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1143730]]'
hide p2
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1143731]]'
hide p2
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1143732]]'
hide p2
play sfx2 "other_7047.ogg"
c0 '[textdict[1143733]]'
return