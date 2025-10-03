label avg127107:

$ play_music("ed6323.ogg")
scene avg_bg_214
$ update_narrator('c14741')
window show
with fade_in
c14741 '[convertstrid(1178620)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1178621)]'
hide p4
c0 '[convertstrid(1178622)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1178623)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1178624)]'
hide p1
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('st064_01 2', 'p1469', [l(-2), light, flip], 6)
c14691 '[convertstrid(1178625)]'
hide p1304
$ update_portrait('st064_01 2', 'p1469', [l(-2), dark, flip], 5)
c14743 '[convertstrid(1178626)]'
c14753 '[convertstrid(1178627)]'
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1178628)]'
hide p1469
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
c14751 '[convertstrid(1178629)]'
hide p1304
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfx2 "other_7080.ogg"
c33 '[convertstrid(1178630)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), r_shake, light, flip], 6)
c41 '[convertstrid(1178631)]'
hide p3
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1178632)]'
return