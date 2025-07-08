label avg12642:
stop music

play music "ED6202.ogg"
scene avg_bg_036
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 5)
play sfx2 "other_7060.ogg"
c13 '[textdict[1163021]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1163022]]'
hide p4
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1163023]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1163024]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1163025]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1163026]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1163027]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1163028]]'
hide p3
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1163029]]'
return