label avg12539:

play music "ED6105.ogg"
scene avg_bg_077
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 5)
play sfx2 "other_7047.ogg"
c13 '[convertstrid(1152901)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c471 '[convertstrid(1152902)]'
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1152903)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[convertstrid(1152904)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c471 '[convertstrid(1152905)]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [r_entrance(-6), light], 5)
c33 '[convertstrid(1152906)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c471 '[convertstrid(1152907)]'
c471 '[convertstrid(1152908)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1152909)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c471 '[convertstrid(1152910)]'
return