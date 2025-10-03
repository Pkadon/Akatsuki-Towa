label avg12752:

$ play_music("ed7544.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1174312)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1174313)]'
hide p1
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1174314)]'
hide p1304
hide p3
play sfx2 "other_7080.ogg"
c0 '[convertstrid(1174315)]' with shake
c14661 '[convertstrid(1174316)]'
c14581 '[convertstrid(1174317)]'
c14581 '[convertstrid(1174318)]'
c14601 '[convertstrid(1174319)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1174320)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1174321)]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1174322)]'
return