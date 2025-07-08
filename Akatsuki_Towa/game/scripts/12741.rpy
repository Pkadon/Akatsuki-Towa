label avg12741:
stop music

play music "ed7105.ogg"
scene avg_bg_203
window show
with fade_in
c0 '[textdict[1172905]]'
c0 '[textdict[1172906]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1172907]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172908]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172909]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1172910]]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172911]]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172912]]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1172913]]' with shake
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[textdict[1172914]]'
return