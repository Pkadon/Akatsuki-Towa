label avg12177:

play music "ED6104.ogg"
scene avg_bg_038
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1120544)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120545)]'
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1120546)]'
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1120547)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120548)]'
hide p3
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120549)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120550)]'
hide p1
hide p2
play sfx2 "common_remind.ogg"
c0 '[convertstrid(1120551)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120552)]'
return