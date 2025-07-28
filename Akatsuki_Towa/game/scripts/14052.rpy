label avg14052:

play music "ED6100.ogg"
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1203033)]'
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7047.ogg"
c23 '[convertstrid(1203034)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c12021 '[convertstrid(1203035)]'
c12021 '[convertstrid(1203036)]'
c12021 '[convertstrid(1203037)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1203038)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c12021 '[convertstrid(1203039)]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1203040)]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
c12021 '[convertstrid(1203041)]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1203042)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1203043)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c12021 '[convertstrid(1203044)]'
c12021 '[convertstrid(1203045)]'
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1203046)]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
c12021 '[convertstrid(1203047)]'
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
c0 '[convertstrid(1203048)]'
play music "ed7124.ogg"
scene avg_bg_059
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7047.ogg"
c23 '[convertstrid(1203049)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
c12561 '[convertstrid(1203050)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1203051)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
c12561 '[convertstrid(1203052)]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1203053)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
c12561 '[convertstrid(1203054)]'
c12561 '[convertstrid(1203055)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1203056)]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1203057)]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
c12561 '[convertstrid(1203058)]'
c12561 '[convertstrid(1203059)]'
return