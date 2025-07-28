label avg12248:

play music "ed7105.ogg"
scene avg_bg_010
$ update_narrator('c33')
window show
with fade_in
$ update_portrait('oc003_01 1', 'p3', [r_entrance(-6), light], 6)
c33 '[convertstrid(1121340)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1121341)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121342)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfx2 "other_7072.ogg"
c33 '[convertstrid(1121343)]'
hide p3
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1121344)]'
hide p1
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1121345)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1121346)]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121347)]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1121348)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1121526)]'
return