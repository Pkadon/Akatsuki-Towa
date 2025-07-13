label avg12771:

play music "ED6202.ogg"
scene avg_bg_010
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
$ update_narrator('c33')
window show
with fade_in
c33 '[textdict[1175632]]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1175633]]'
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1175634]]'
hide p2
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1175635]]'
hide p1304
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1175636]]'
return