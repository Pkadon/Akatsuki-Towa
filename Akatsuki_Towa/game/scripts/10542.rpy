label avg10542:

play music "ed7151.ogg"
scene avg_bg_078
window show
with fade_in
c0 '[textdict[1152695]]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 5)
c23 '[textdict[1152696]]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1152697]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
c43 '[textdict[1152698]]'
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1152699]]'
hide p3
hide p1
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
with fade
c2391 '[textdict[1152700]]'
$ update_portrait('st040_01 5', 'p239', [l(-19), dark, flip], 6)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li03.ogg"
c43 '[textdict[1152701]]'
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1152702]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1152703]]'
return