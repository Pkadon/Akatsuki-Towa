label avg20005:

play music "ed9997.ogg"
scene avg_bg_071
$ update_narrator('c13')
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
window show
with fade_in
$ update_portrait('oc001_01 19', 'p1', [r(-2), l_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1000224)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1000225)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1000226)]'
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1000227)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 20', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c21 '[convertstrid(1000228)]'
hide p2
hide p1
play sfx2 "common_remind.ogg"
c0 '[convertstrid(1000229)]'
c0 '[convertstrid(1000230)]'
return