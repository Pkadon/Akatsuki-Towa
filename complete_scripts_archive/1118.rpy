label avg1118:

play music "ed7124.ogg"
scene avg_bg_059
window show
with fade_in
c0 '[textdict[2102908]]'
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[2102909]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c21 '[textdict[2102910]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[2102911]]'
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c10061 '[textdict[2102912]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2102913]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
c31 '[textdict[2102914]]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2102915]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[2102916]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
c13 '[textdict[2102917]]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2102918]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
c43 '[textdict[2102919]]'
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2102920]]'
scene avg_bg_070
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[2102921]]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[2102922]]'
return