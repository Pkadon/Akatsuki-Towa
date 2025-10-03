label avg12762:

stop music
scene avg_bg_201
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7060.ogg"
c0 '[convertstrid(1174603)]'
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1174604)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c14521 '[convertstrid(1174605)]' with shake
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1174606)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1174607)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1174608)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
play sfx2 "fight_6002.ogg"
c13043 '[convertstrid(1174609)]'
hide p2
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[convertstrid(1174610)]'
hide p1304
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1174611)]'
hide p3
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1174612)]'
return