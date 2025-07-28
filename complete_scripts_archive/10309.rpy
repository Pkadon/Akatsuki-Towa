label avg10309:

play music "ed7124.ogg"
scene avg_bg_059
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[convertstrid(1130285)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130286)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130287)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130288)]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
c10063 '[convertstrid(1130289)]'
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130290)]'
return