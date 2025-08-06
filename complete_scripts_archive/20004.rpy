label avg20004:

play music "ed9997.ogg"
scene avg_bg_071
$ update_narrator('c13')
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
window show
with fade_in
$ update_portrait('oc001_01 19', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[convertstrid(1000214)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1000215)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000216)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000217)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1000218)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1000219)]'
hide p2
hide p1
play sfx2 "common_remind.ogg"
c0 '[convertstrid(1000220)]'
c0 '[convertstrid(1000221)]'
c0 '[convertstrid(1000223)]'
return