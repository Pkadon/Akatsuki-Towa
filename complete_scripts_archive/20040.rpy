label avg20040:

play music "ed7151.ogg"
scene placeholderbackground
$ update_narrator('c353')
$ update_portrait('sc027_01 1', 'p35', [r(-10), light], 6)
window show
with fade_in
$ update_portrait('sc027_01 1', 'p35', [r_exit(-10), light], 6)
play sfx2 "other_7085.ogg"
c353 '[convertstrid(1002424)]'
hide p35
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1002425)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1002426)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1002427)]'
return