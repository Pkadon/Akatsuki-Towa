label avg127103:

play music "ed6323.ogg"
scene avg_bg_214
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(1178414)]'
$ update_portrait('oc002_01 23', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1178415)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1178416)]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1178417)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1178418)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1178419)]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1178420)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1178421)]'
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l_entrance(-2), light, flip], 6)
c13041 '[convertstrid(1178422)]'
hide p3
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1178423)]'
hide p1304
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st064_01 1', 'p1469', [l(-2), light, flip], 6)
c14691 '[convertstrid(1178424)]'
hide p1469
hide p1
c0 '[convertstrid(1178425)]'
return