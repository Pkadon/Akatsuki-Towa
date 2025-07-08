label avg10763:
stop music

play music "ed6323.ogg"
scene avg_bg_206
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1175146]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1175147]]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1175148]]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1175149]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1175150]]'
hide p4
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1175151]]'
return