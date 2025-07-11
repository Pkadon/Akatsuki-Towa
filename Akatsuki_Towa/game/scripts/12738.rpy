label avg12738:

play music "ED6200.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[1172861]]'
play sfx2 "other_7014.ogg"
c0 '[textdict[1172862]]'
c14401 '[textdict[1172863]]'
c14401 '[textdict[1172864]]'
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1172865]]'
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
c13 '[textdict[1172866]]'
hide p1304
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
c14401 '[textdict[1172867]]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172868]]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1172869]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c14401 '[textdict[1172870]]'
hide p1
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1172871]]'
return