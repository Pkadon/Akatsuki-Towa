label avg10764:
stop music

play music "ed6323.ogg"
scene avg_bg_206
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1175153]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175154]]'
hide p1304
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175155]]'
hide p1
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1175156]]'
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175157]]'
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1175158]]'
play music "ed7511.ogg"
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1175159]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1175160]]'
hide p3
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1175161]]'
hide p2
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1175162]]'
hide p4
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
c13 '[textdict[1175163]]'
return