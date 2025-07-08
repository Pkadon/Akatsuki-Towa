label avg10762:
stop music

play music "ed6323.ogg"
scene avg_bg_206
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 5)
window show
with fade_in
c43 '[textdict[1175136]]'
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1175137]]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1175138]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175139]]'
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1175140]]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1175141]]'
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175142]]'
hide p1304
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175143]]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1175144]]'
return