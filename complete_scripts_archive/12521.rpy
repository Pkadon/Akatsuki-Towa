label avg12521:
stop music

play music "ED6100.ogg"
scene avg_bg_104
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
$ update_portrait('oc002_01 14', 'p2', [l(-3), r_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[textdict[1151258]]'
hide p2
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151259]]'
hide p2
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1151260]]'
hide p13
hide p1
with fade
$ update_portrait('st041_01 1', 'p1218', [l_entrance(-1), light, flip], 6)
c12181 '[textdict[1151261]]'
hide p1218
$ update_portrait('st041_01 1', 'p1218', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1151262]]'
hide p1
hide p1218
$ update_portrait('st041_01 1', 'p1218', [l(-1), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch19.ogg"
c23 '[textdict[1151263]]'
hide p1218
hide p2
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st041_01 1', 'p1218', [l(-1), light, flip], 6)
c12181 '[textdict[1151264]]'
hide p1218
hide p2
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
c2401 '[textdict[1151265]]'
hide p240
hide p2
with fade
$ update_portrait('st050_01 5', 'p1219', [l_entrance(-11), light, flip], 6)
c12191 '[textdict[1151266]]'
hide p1219
$ update_portrait('st050_01 5', 'p1219', [l(-11), light, flip], 6)
c12191 '[textdict[1151267]]'
hide p1219
$ update_portrait('st050_01 5', 'p1219', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1151268]]'
hide p1
hide p1219
$ update_portrait('st050_01 5', 'p1219', [l(-11), dark, flip], 6)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1151270]]'
hide p2
hide p1219
$ update_portrait('st050_01 5', 'p1219', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[textdict[1151276]]'
hide p1219
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 5)
with fade
c33 '[textdict[1151277]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151283]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1151284]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1151285]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1151289]]'
hide p2
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1151295]]'
return