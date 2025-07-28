label avg12603:

play music "ED6200.ogg"
scene avg_bg_080
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1161143)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161144)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1161145)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161146)]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1161147)]'
return