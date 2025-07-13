label avg12221:

play music "ED6103.ogg"
scene avg_bg_072
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7047.ogg"
c0 '[textdict[1120960]]'
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
c11 '[textdict[1120961]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c6873 '[textdict[1120962]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120963]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120964]]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
c6873 '[textdict[1120965]]'
c6873 '[textdict[1120966]]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1120967]]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
c6873 '[textdict[1120968]]'
c6873 '[textdict[1121573]]'
return