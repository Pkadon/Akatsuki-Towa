label avg12243:

play music "ed7101.ogg"
scene avg_bg_020
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1121265)]'
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1121266)]'
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1121267)]'
hide p2
$ update_portrait('oc004_01 22', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121268)]'
hide p1
hide p4
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
$ update_narrator('c2323')
with fade
c2323 '[convertstrid(1121269)]'
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1121270)]'
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), r_shake, light], 6)
c2323 '[convertstrid(1121271)]'
hide p4
hide p232
c0 '[convertstrid(1121272)]'
$ update_portrait('st033_01 1', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1121273)]'
$ update_portrait('st033_01 1', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1121274)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1121523)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121275)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st033_01 2', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1121590)]'
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121591)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1121592)]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
c2323 '[convertstrid(1121593)]'
return