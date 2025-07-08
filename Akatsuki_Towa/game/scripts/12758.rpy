label avg12758:
stop music

play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1174455]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1174456]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1174457]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1174458]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1174459]]'
hide p3
hide p1
play sfx2 "other_7088.ogg"
c0 '[textdict[1174460]]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1174461]]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[textdict[1174462]]'
return