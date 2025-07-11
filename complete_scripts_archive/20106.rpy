label avg20106:

play music "ED6103.ogg"
scene avg_bg_072
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
c11 '[textdict[1005213]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c6873 '[textdict[1005214]]'
hide p1
c0 '[textdict[1005215]]'
c6873 '[textdict[1005216]]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005217]]'
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1005218]]'
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1005219]]'
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 6)
c6873 '[textdict[1005220]]'
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005221]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
c6873 '[textdict[1005222]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
c6873 '[textdict[1005223]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
with fade
play sfxvoice "avg_vocal_ch19.ogg"
c21 '[textdict[1005224]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1005225]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 5)
c13 '[textdict[1005226]]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1005227]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc040_01 5', 'p47', [l(-9), light, flip], 6)
c471 '[textdict[1005228]]'
hide p1
$ update_portrait('sc040_01 5', 'p47', [l(-9), dark, flip], 6)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 5)
c463 '[textdict[1005230]]'
hide p47
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005231]]'
return