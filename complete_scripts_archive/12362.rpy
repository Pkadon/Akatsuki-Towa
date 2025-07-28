label avg12362:

play music "ed7150.ogg"
scene avg_bg_014
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7021.ogg"
c0 '[convertstrid(1133709)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133710)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133711)]'
hide p2
play sfx2 "other_7097.ogg"
c10701 '[convertstrid(1133712)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1133713)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[convertstrid(1133714)]'
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133715)]'
return