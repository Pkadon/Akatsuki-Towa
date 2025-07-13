label avg12227:

play music "ed7569.ogg"
scene avg_bg_036
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7018.ogg"
c21 '[textdict[1121050]]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('uc004_02 1', 'p991', [r(-6), light], 5)
c9913 '[textdict[1121051]]'
hide p2
hide p991
c0 '[textdict[1121052]]'
$ update_portrait('uc004_02 2', 'p991', [r(-6), light], 5)
play sfx2 "other_7088.ogg"
c9913 '[textdict[1121053]]'
$ update_portrait('uc004_02 2', 'p991', [r(-6), dark], 5)
$ update_portrait('oc001_01 17', 'p1', [l_midback(-2), light, flip], 6)
play sfx2 "other_7002.ogg"
c11 '[textdict[1121054]]'
hide p991
$ update_portrait('oc001_01 17', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[textdict[1121055]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1121056]]'
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1121057]]'
hide p46
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1121058]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[textdict[1121059]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1121060]]'
return