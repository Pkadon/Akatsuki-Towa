label avg12225:
stop music

play music "ED6103.ogg"
scene avg_bg_037
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1121028]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1121029]]'
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1121030]]'
hide p46
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1121491]]'
hide p2
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1121032]]'
hide p2
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1121033]]'
hide p46
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121034]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 5)
c463 '[textdict[1121035]]'
hide p1
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1121036]]'
hide p46
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1121575]]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121576]]'
return