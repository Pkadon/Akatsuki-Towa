label avg12826:
stop music

play music "ed7102.ogg"
scene avg_bg_036
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1184608]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1184609]]'
hide p4
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1184610]]'
hide p4
hide p1
c0 '[textdict[1184611]]'
c25641 '[textdict[1184612]]'
c25651 '[textdict[1184613]]'
c25661 '[textdict[1184614]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1184615]]'
play music "ed7511.ogg"
hide p2
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1184616]]' with shake
hide p2
hide p1304
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 5)
c23 '[textdict[1184617]]'
hide p2
hide p1304
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1184618]]'
hide p1304
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1184619]]'
hide p1
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 5)
c43 '[textdict[1184620]]'
return