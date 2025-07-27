label avg12548:

play music "ED6556.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1152970)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1152971)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152972)]'
return