label avg20125:
stop music

play music "ed7110.ogg"
scene avg_bg_030
window show
with fade_in
$ update_portrait('sc038_01 1', 'p45', [l_entrance(-1), light, flip], 6)
play sfx2 "other_7047.ogg"
c451 '[textdict[1006453]]'
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1006454]]'
hide p45
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
c451 '[textdict[1006455]]'
hide p1
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1006456]]'
hide p1
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1006457]]'
hide p45
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 5', 'p45', [l(-1), light, flip], 6)
c451 '[textdict[1006458]]'
hide p45
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
c451 '[textdict[1006459]]'
hide p45
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
c451 '[textdict[1006460]]'
hide p45
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 5', 'p45', [l(-1), light, flip], 6)
c451 '[textdict[1006461]]'
hide p1
$ update_portrait('sc038_01 5', 'p45', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1006462]]'
hide p1
$ update_portrait('sc038_01 5', 'p45', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1006463]]'
hide p45
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1006464]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1006465]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1006466]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r_exit(-2), light], 5)
c13 '[textdict[1006467]]'
hide p1
hide p2
$ update_portrait('sc041_01 5', 'p48', [l(-9), light, flip], 6)
with fade
c481 '[textdict[1006468]]'
$ update_portrait('sc041_01 5', 'p48', [l(-9), dark, flip], 6)
$ update_portrait('sc040_01 2', 'p47', [r_entrance(-9), light], 5)
c473 '[textdict[1006469]]'
return