label avg12522:

play music "ED6100.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1151301]]'
hide p1
$ update_portrait('sc005_01 1', 'p13', [r_entrance(-17), light], 5)
c133 '[textdict[1151302]]'
$ update_portrait('sc005_01 1', 'p13', [r(-17), dark], 5)
c12021 '[textdict[1151303]]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), r_shake, light], 5)
c133 '[textdict[1151304]]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), dark], 5)
c12021 '[textdict[1151305]]'
c12021 '[textdict[1151306]]'
c12021 '[textdict[1151307]]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), r_shake, light], 5)
c133 '[textdict[1151308]]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), dark], 5)
c12021 '[textdict[1151309]]'
$ update_portrait('sc005_01 4', 'p13', [r(-17), light], 5)
c133 '[textdict[1151310]]'
$ update_portrait('sc005_01 4', 'p13', [r(-17), dark], 5)
c12021 '[textdict[1151311]]'
c12021 '[textdict[1151312]]'
hide p13
$ update_portrait('oc002_01 21', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1151313]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1151314]]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1151315]]'
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1151316]]'
hide p3
$ update_portrait('sc005_01 4', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1151317]]'
return