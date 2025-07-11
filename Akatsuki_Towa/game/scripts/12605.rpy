label avg12605:

play music "ED6102.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1161236]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1161237]]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1161238]]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1161239]]'
hide p2
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 5)
c33 '[textdict[1161240]]'
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161241]]'
hide p3
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1161242]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161243]]'
hide p4
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1161244]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1161245]]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1161246]]'
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1161247]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1161248]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161249]]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1161250]]'
return