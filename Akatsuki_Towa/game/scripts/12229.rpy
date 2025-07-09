label avg12229:
stop music

play music "ED6103.ogg"
scene avg_bg_072
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
c11 '[textdict[1121093]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c6873 '[textdict[1121094]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121095]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
c43 '[textdict[1121096]]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121097]]'
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1121098]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1121099]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 5)
c463 '[textdict[1121100]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 5)
c463 '[textdict[1121581]]'
hide p2
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121101]]'
return