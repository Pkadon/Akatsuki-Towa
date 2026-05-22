label avg12806:

$ play_music("ed7516.ogg")
scene avg_bg_023
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
c13 '[convertstrid(1181735)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1181736)]'
hide p1
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1181737)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1181738)]'
hide p2
$ update_portrait('st040_01 4', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1181739)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1181740)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1181741)]'
$ update_portrait('st040_01 4', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1181742)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st040_01 3', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1181743)]'
hide p3
$ update_portrait('st040_01 3', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1181744)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1181745)]'
$ update_portrait('st040_01 4', 'p239', [l(-19), light, flip], 6)
c2391 '[convertstrid(1181746)]'
$ update_portrait('st040_01 4', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1181747)]'
scene avg_bg_010
$ update_narrator('c0')
with fade
c0 '[convertstrid(1181748)]'
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1181749)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1181750)]'
$ play_music("ed7511.ogg")
scene avg_bg_036
$ update_narrator('c0')
with fade
play sfx2 "other_7013.ogg"
c0 '[convertstrid(1181751)]'
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1181752)]'
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1181753)]'
hide p2
$ update_portrait('oc003_01 21', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1181754)]'
hide p3
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
c14401 '[convertstrid(1181755)]' with shake
hide p1304
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1181756)]'
hide p1
c0 '[convertstrid(1181757)]'
return