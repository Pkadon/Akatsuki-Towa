label avg12582:
stop music

play music "ed7151.ogg"
scene avg_bg_080
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1155411]]'
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1155412]]'
hide p3
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155413]]'
hide p4
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155414]]'
hide p1
hide p4
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1155415]]'
hide p1
hide p4
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1155416]]'
hide p1
hide p4
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155417]]'
hide p4
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1155418]]'
hide p1
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155419]]'
hide p2
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155420]]'
hide p4
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[textdict[1155421]]'
hide p1
hide p3
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 5)
c43 '[textdict[1155422]]'
hide p4
hide p3
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1155423]]'
hide p4
hide p3
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1155424]]'
hide p2
hide p3
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1155425]]'
return