label avg12313:
stop music

play music "ed7305.ogg"
scene avg_bg_051
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
window show
with fade_in
c41 '[textdict[1133256]]'
hide p4
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1133257]]'
hide p4
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133258]]'
hide p1
hide p2
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[textdict[1133259]]'
hide p3
hide p2
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
c43 '[textdict[1133260]]'
hide p2
hide p4
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l_exit(-32), light, flip], 6)
c581 '[textdict[1133261]]'
hide p58
hide p4
$ update_portrait('oc002_01 12', 'p2', [r_midback(-3), light], 5)
c23 '[textdict[1133262]]'
return