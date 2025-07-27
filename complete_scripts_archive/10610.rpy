label avg10610:

stop music
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7060.ogg"
c0 '[convertstrid(1160413)]'
play music "ED6202.ogg"
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7060.ogg"
c31 '[convertstrid(1160414)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[convertstrid(1160415)]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1160416)]'
hide p4
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1160417)]'
play music "ed7511.ogg"
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 5)
play sfx2 "other_7079.ogg"
c13 '[convertstrid(1160418)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1160419)]'
return