label avg10308:

play music "ed7124.ogg"
scene avg_bg_059
$ update_narrator('c10063')
window show
with fade_in
play sfx2 "other_7021.ogg"
c10063 '[convertstrid(1130265)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1130266)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
c10063 '[convertstrid(1130267)]'
c10063 '[convertstrid(1130268)]'
c10063 '[convertstrid(1130269)]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130270)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
c10063 '[convertstrid(1130271)]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1130272)]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
c10063 '[convertstrid(1130273)]'
c10063 '[convertstrid(1130274)]'
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[convertstrid(1130275)]'
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130276)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1130277)]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro08.ogg"
c33 '[convertstrid(1130278)]'
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[convertstrid(1130279)]'
hide p3
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
c10063 '[convertstrid(1130280)]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
c41 '[convertstrid(1130281)]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1130282)]'
menu:
    extend ""
    "[textdict[1130283]]":
        call avg10309
    "[textdict[1130284]]":
        call avg10310
return