label avg12554:
stop music

play music "ED6523.ogg"
scene avg_bg_081
window show
with fade_in
c12411 '[textdict[1153047]]'
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1153048]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1153049]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c12411 '[textdict[1153050]]'
hide p1
c12463 '[textdict[1153051]]'
c12471 '[textdict[1153052]]'
c12483 '[textdict[1153053]]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro04.ogg"
c33 '[textdict[1153054]]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
c12491 '[textdict[1153055]]'
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch24.ogg"
c23 '[textdict[1153056]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1153057]]'
return