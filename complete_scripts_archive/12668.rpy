label avg12668:
stop music

play music "ed7150.ogg"
scene avg_bg_015
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1166661]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166662]]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
c13661 '[textdict[1166663]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1166664]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l_entrance(-32), light, flip], 6)
c581 '[textdict[1166665]]'
hide p1
$ update_portrait('sc051_01 4', 'p58', [l(-32), dark, flip], 6)
$ update_portrait('sc053_01 4', 'p60', [r_entrance(-32), light], 5)
c603 '[textdict[1166666]]'
hide p58
hide p60
play sfx2 "other_7085.ogg"
c0 '[textdict[1166667]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1166668]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166669]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1166670]]'
return