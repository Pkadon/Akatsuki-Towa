label avg12578:

play music "ED6523.ogg"
scene avg_bg_080
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1155359]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1155360]]'
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155361]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155362]]'
hide p3
hide p1
with fade
c12611 '[textdict[1155363]]'
$ update_portrait('sc021_01 1', 'p29', [r(-17), light], 5)
c293 '[textdict[1155364]]'
$ update_portrait('sc021_01 1', 'p29', [r(-17), dark], 5)
c12611 '[textdict[1155365]]'
c12611 '[textdict[1155366]]'
hide p29
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155367]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c12611 '[textdict[1155368]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1155369]]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
c12611 '[textdict[1155370]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
with fade
c13 '[textdict[1155371]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1155372]]'
hide p4
hide p1
with fade
c12611 '[textdict[1155373]]'
return