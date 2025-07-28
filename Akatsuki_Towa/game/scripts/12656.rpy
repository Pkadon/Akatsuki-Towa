label avg12656:

play music "ED6300.ogg"
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
c33 '[convertstrid(1166374)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166375)]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166376)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166377)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166378)]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 6)
c43 '[convertstrid(1166379)]'
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166380)]'
hide p4
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1166381)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1166382)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1166383)]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1166384)]'
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1166385)]'
return