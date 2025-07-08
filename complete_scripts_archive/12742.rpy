label avg12742:
stop music

play music "ed7105.ogg"
scene avg_bg_203
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1172916]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172917]]'
hide p1
hide p3
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1172918]]'
play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[1172919]]'
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172920]]'
hide p3
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172921]]'
hide p3
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172922]]'
hide p1
hide p3
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1172923]]'
hide p1
hide p3
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1172924]]'
hide p3
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[textdict[1172925]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1172926]]'
return