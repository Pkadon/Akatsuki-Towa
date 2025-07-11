label avg20069:

play music "ed7150.ogg"
scene avg_bg_015
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
c11 '[textdict[1003881]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1003882]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1003883]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na06.ogg"
c11 '[textdict[1003884]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1003885]]'
return