label avg12554:

play music "ED6523.ogg"
scene avg_bg_081
$ update_narrator('c12411')
window show
with fade_in
c12411 '[convertstrid(1153047)]'
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 5)
c13 '[convertstrid(1153048)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1153049)]'
hide p3
c12411 '[convertstrid(1153050)]'
hide p1
c12463 '[convertstrid(1153051)]'
c12471 '[convertstrid(1153052)]'
c12483 '[convertstrid(1153053)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro04.ogg"
c33 '[convertstrid(1153054)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
c12491 '[convertstrid(1153055)]'
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch24.ogg"
c23 '[convertstrid(1153056)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1153057)]'
return