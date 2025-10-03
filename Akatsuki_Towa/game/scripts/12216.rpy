label avg12216:

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7042.ogg"
c11 '[convertstrid(1120901)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
c9893 '[convertstrid(1120902)]'
c9883 '[convertstrid(1121477)]'
hide p1
c9881 '[convertstrid(1121478)]'
c9893 '[convertstrid(1120903)]'
c9881 '[convertstrid(1120904)]'
c9893 '[convertstrid(1120905)]'
c9893 '[convertstrid(1120906)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120907)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
c9883 '[convertstrid(1120908)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120909)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1120910)]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120911)]'
return