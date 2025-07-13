label avg12601:

play music "ED6102.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1161118]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1161119]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1161120]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1161121]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1161122]]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c12321 '[textdict[1161123]]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1161124]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12321 '[textdict[1161125]]'
c12321 '[textdict[1161126]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1161127]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1161128]]'
hide p3
c12321 '[textdict[1161129]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1161130]]'
return