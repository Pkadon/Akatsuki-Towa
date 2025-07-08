label avg12842:
stop music

play music "ed7302.ogg"
scene avg_bg_074
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1186256]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1186257]]'
hide p2
hide p1
play sfx2 "other_7085.ogg"
c0 '[textdict[1186258]]'
c15281 '[textdict[1186259]]' with shake
c15291 '[textdict[1186260]]'
c15291 '[textdict[1186261]]'
c15301 '[textdict[1186262]]'
c15301 '[textdict[1186263]]'
c15291 '[textdict[1186264]]'
c15301 '[textdict[1186265]]'
c15301 '[textdict[1186266]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1186267]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1186268]]'
hide p1
hide p4
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1186269]]'
hide p4
hide p3
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1186270]]'
scene avg_bg_070
with fade
c0 '[textdict[1186271]]'
c0 '[textdict[1186272]]'
c0 '[textdict[1186273]]'
return