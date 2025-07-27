label avg10711:

play music "ed7151.ogg"
scene avg_bg_061
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1170322)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1170323)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1170324)]'
scene avg_bg_040
$ update_portrait('oc008_01 1', 'p8', [r(-5), light], 5)
$ update_narrator('c83')
with fade
c83 '[convertstrid(1170325)]'
$ update_portrait('oc008_01 1', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170326)]'
hide p2
hide p8
play sfx2 "other_7044.ogg"
c0 '[convertstrid(1170327)]'
$ update_portrait('oc008_01 3', 'p8', [r_exit(-5), light], 5)
c83 '[convertstrid(1170328)]'
hide p8
$ update_portrait('st061_01 5', 'p1304', [r_entrance(-2), light], 5)
c13043 '[convertstrid(1170329)]'
hide p1304
c0 '[convertstrid(1170330)]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[convertstrid(1170331)]'
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170332)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 3', 'p1304', [r(-2), light], 5)
c13043 '[convertstrid(1170333)]'
hide p2
hide p1304
play sfx2 "other_7057.ogg"
c0 '[convertstrid(1170334)]' with shake
c0 '[convertstrid(1170335)]'
c0 '[convertstrid(1170336)]'
$ update_portrait('oc008_01 1', 'p8', [r_exit(-5), light], 5)
c83 '[convertstrid(1170337)]'
hide p8
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170338)]'
$ update_portrait('oc002_01 15', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1170339)]'
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r_entrance(-2), light], 5)
c13043 '[convertstrid(1170340)]'
$ update_portrait('st061_01 3', 'p1304', [r(-2), light], 5)
c13043 '[convertstrid(1170341)]'
$ update_portrait('st061_01 3', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170342)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1170343)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 5)
c13043 '[convertstrid(1170344)]'
return