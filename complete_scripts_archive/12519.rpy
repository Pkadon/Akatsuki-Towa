label avg12519:

play music "ED6301.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1151238)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1151239)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro12.ogg"
c31 '[convertstrid(1151240)]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1151241)]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1151242)]'
hide p4
$ update_portrait('sc005_01 1', 'p13', [l_entrance(-17), light, flip], 6)
c131 '[convertstrid(1151243)]'
hide p2
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1151244)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1151245)]'
hide p3
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1151246)]'
hide p13
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1151247)]'
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1151248)]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1151249)]'
hide p4
$ update_portrait('sc005_01 1', 'p13', [l_entrance(-17), light, flip], 6)
c131 '[convertstrid(1151250)]'
return