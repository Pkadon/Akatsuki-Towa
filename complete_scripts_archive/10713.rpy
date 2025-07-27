label avg10713:

play music "ed7151.ogg"
scene avg_bg_207
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1170876)]'
c0 '[convertstrid(1170877)]'
$ update_portrait('oc002_01 3', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1170878)]'
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc008_01 1', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170879)]'
$ update_portrait('oc008_01 2', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170880)]'
hide p2
hide p8
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1170881)]'
$ update_portrait('oc008_01 5', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170882)]'
$ update_portrait('oc008_01 5', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170883)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170884)]'
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc008_01 2', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170885)]'
$ update_portrait('oc008_01 6', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170886)]'
$ update_portrait('oc008_01 6', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170887)]' with shake
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc008_01 1', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170888)]'
$ update_portrait('oc008_01 5', 'p8', [r(-5), light], 5)
c83 '[convertstrid(1170889)]'
$ update_portrait('oc008_01 5', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170890)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc008_01 6', 'p8', [r_exit(-5), light], 5)
c83 '[convertstrid(1170891)]'
hide p8
hide p2
c0 '[convertstrid(1170892)]'
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170893)]'
return