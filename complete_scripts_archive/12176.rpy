label avg12176:

play music "ed7111.ogg"
scene avg_bg_003
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
window show
with fade_in
c51 '[textdict[1120530]]'
$ update_portrait('oc005_01 2', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 5)
c13 '[textdict[1120531]]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
c51 '[textdict[1120532]]'
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
c51 '[textdict[1120533]]'
$ update_portrait('oc005_01 14', 'p5', [l(-6), light, flip], 6)
c51 '[textdict[1120534]]'
hide p1
$ update_portrait('oc005_01 14', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1120535]]'
hide p5
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120536]]'
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120537]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
c33 '[textdict[1120538]]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
c51 '[textdict[1120539]]'
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
c51 '[textdict[1120540]]'
$ update_portrait('oc005_01 8', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1120541]]'
hide p5
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120542]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1007705]]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007706]]'
return