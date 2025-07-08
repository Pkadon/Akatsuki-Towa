label avg12373:
stop music

play music "ed9999.ogg"
scene avg_bg_058
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
play sfx2 "other_7021.ogg"
c21 '[textdict[1134058]]'
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1134059]]'
hide p2
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1134060]]'
hide p1
hide p2
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1134062]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134063]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134064]]'
hide p1
hide p2
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
c13 '[textdict[1134065]]'
hide p2
hide p1
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134066]]'
hide p2
hide p1
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1134067]]'
hide p1
hide p2
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfx2 "other_7079.ogg"
c13 '[textdict[1134068]]'
hide p1
hide p2
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1134069]]'
return