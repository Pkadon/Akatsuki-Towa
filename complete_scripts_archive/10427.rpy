label avg10427:

play music "ed7511.ogg"
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1141272)]'
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1141273)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), l_shake, light], 6)
play sfxvoice "avg_vocal_na07.ogg"
c13 '[convertstrid(1141274)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
c11091 '[convertstrid(1141275)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1141276)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1141277)]'
hide p2
$ update_portrait('oc004_01 12', 'p4', [l_entrance(-5), light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
c41 '[convertstrid(1141278)]'
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1141279)]'
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[convertstrid(1141280)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1141281)]'
hide p3
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
play sfx2 "other_7007.ogg"
c11091 '[convertstrid(1141282)]' with shake
return