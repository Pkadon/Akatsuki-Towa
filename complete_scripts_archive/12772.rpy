label avg12772:
stop music

play music "ED6202.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1175638]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1175639]]'
hide p1
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1175640]]'
hide p4
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1175641]]'
hide p1304
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1175642]]'
hide p3
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1175643]]'
hide p1304
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1175644]]'
return