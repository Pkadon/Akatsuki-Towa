label avg12560:
stop music

play music "ED6102.ogg"
scene avg_bg_023
window show
with fade_in
c12321 '[textdict[1153117]]'
c12321 '[textdict[1153118]]'
c12321 '[textdict[1153119]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1153120]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
c21 '[textdict[1153121]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1153122]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1153123]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1153124]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1153125]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1153126]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1153127]]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1153128]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1153129]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1153130]]'
return