label avg12657:

play music "ED6300.ogg"
scene avg_bg_070
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1166387)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1166388)]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1166389)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1166390)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1166391)]'
$ update_portrait('oc004_01 22', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1166392)]'
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[convertstrid(1166393)]'
hide p1
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1166394)]'
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7087.ogg"
c41 '[convertstrid(1166395)]' with shake
return