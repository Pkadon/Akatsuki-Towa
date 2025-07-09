label avg12361:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
play sfx2 "other_7021.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[textdict[1133702]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133703]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1133704]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7004.ogg"
c21 '[textdict[1133705]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1133706]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfx2 "common_quest.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[textdict[1133707]]'
return