label avg12548:
stop music

play music "ED6556.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1152970]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1152971]]'
hide p2
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1152972]]'
return