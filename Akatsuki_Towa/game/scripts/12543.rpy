label avg12543:

play music "ED6103.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1152936)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1152937)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152938)]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1152939)]'
return