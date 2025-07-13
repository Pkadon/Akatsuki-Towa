label avg12752:

play music "ed7544.ogg"
scene avg_bg_036
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1174312]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1174313]]'
hide p1
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1174314]]'
hide p1304
hide p3
play sfx2 "other_7080.ogg"
c0 '[textdict[1174315]]' with shake
c14661 '[textdict[1174316]]'
c14581 '[textdict[1174317]]'
c14581 '[textdict[1174318]]'
c14601 '[textdict[1174319]]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1174320]]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1174321]]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1174322]]'
return