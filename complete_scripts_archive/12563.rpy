label avg12563:

play music "ED6200.ogg"
scene avg_bg_080
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1153214)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1153215)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1153216)]'
hide p3
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1153217)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153218)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1153219)]'
play music "ed7450.ogg"
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1153220)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1153221)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153222)]'
return