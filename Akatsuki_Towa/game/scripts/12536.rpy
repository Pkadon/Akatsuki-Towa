label avg12536:

play music "ED6301.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1151765]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151766]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1151767]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1151768]]'
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1151769]]'
return