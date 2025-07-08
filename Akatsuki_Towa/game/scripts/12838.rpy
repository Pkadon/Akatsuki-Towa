label avg12838:
stop music

play music "ED6301.ogg"
scene avg_bg_218
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1186131]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1186132]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1186133]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1186134]]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1186135]]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1186136]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1186137]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1186138]]'
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1186139]]'
return