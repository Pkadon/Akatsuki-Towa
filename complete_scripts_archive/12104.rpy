label avg12104:

play music "ed7111.ogg"
scene avg_bg_047
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
play sfx2 "common_select.ogg"
c11 '[textdict[1128019]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc005_01 5', 'p5', [r(-6), light], 5)
play sfxvoice "avg_vocal_ji11.ogg"
c53 '[textdict[1128020]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 5)
c53 '[textdict[1128021]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc005_01 10', 'p5', [r(-6), light], 5)
c53 '[textdict[1128022]]'
$ update_portrait('oc005_01 10', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1128023]]'
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 5)
play sfx2 "common_quest.ogg"
c53 '[textdict[1128024]]'
return