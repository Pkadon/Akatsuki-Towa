label avg12522:

play music "ED6100.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1151301)]'
hide p1
$ update_portrait('sc005_01 1', 'p13', [r_entrance(-17), light], 6)
c133 '[convertstrid(1151302)]'
$ update_portrait('sc005_01 1', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151303)]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), r_shake, light], 6)
c133 '[convertstrid(1151304)]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151305)]'
c12021 '[convertstrid(1151306)]'
c12021 '[convertstrid(1151307)]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), r_shake, light], 6)
c133 '[convertstrid(1151308)]'
$ update_portrait('sc005_01 2', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151309)]'
$ update_portrait('sc005_01 4', 'p13', [r(-17), light], 6)
c133 '[convertstrid(1151310)]'
$ update_portrait('sc005_01 4', 'p13', [r(-17), dark], 5)
c12021 '[convertstrid(1151311)]'
c12021 '[convertstrid(1151312)]'
hide p13
$ update_portrait('oc002_01 21', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1151313)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1151314)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151315)]'
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151316)]'
hide p3
$ update_portrait('sc005_01 4', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1151317)]'
return