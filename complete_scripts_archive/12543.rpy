label avg12543:
stop music

play music "ED6103.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1152936]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1152937]]'
hide p2
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1152938]]'
hide p1
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1152939]]'
return