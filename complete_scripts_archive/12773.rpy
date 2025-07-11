label avg12773:

play music "ED6202.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1175646]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1175647]]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 5)
c33 '[textdict[1175648]]'
hide p3
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
c23 '[textdict[1175649]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1175650]]'
hide p4
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175651]]'
hide p2
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1175652]]'
hide p1304
hide p1
c0 '[textdict[1175653]]'
return