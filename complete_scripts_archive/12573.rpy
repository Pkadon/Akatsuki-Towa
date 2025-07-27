label avg12573:

play music "ED6102.ogg"
scene avg_bg_023
$ update_narrator('c12321')
window show
with fade_in
c12321 '[convertstrid(1155183)]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1155184)]'
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1155185)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c12321 '[convertstrid(1155186)]'
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1155187)]'
hide p1
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[convertstrid(1155188)]'
return