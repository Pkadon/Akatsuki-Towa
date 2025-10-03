label avg12826:

$ play_music("ed7102.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1184608)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1184609)]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1184610)]'
hide p4
hide p1
c0 '[convertstrid(1184611)]'
c25641 '[convertstrid(1184612)]'
c25651 '[convertstrid(1184613)]'
c25661 '[convertstrid(1184614)]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1184615)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1184616)]' with shake
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1184617)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1184618)]'
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1184619)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1184620)]'
return