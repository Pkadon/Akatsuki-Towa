label avg12570:

play music "ED6200.ogg"
scene avg_bg_010
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[convertstrid(1155146)]'
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155147)]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155148)]'
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1155149)]'
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1155150)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7080.ogg"
c31 '[convertstrid(1155151)]' with shake
return