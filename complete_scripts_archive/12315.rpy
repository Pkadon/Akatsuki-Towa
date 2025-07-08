label avg12315:
stop music

play music "ed7305.ogg"
scene avg_bg_052
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
window show
with fade_in
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
play sfx2 "other_7051.ogg"
c23 '[textdict[1133288]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133289]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1133290]]'
hide p1
hide p4
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 5)
c33 '[textdict[1133291]]'
hide p3
hide p4
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1133292]]'
hide p4
hide p3
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1133293]]'
hide p3
hide p4
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133294]]'
hide p4
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133295]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1133296]]'
hide p4
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1133297]]'
hide p1
hide p4
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1133298]]'
return