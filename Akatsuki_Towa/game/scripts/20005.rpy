label avg20005:

play music "ed9997.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1000224)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1000225)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1000226)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1000227)]'
hide p1
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[convertstrid(1000228)]'
hide p2
play sfx2 "common_remind.ogg"
c0 '[convertstrid(1000229)]'
c0 '[convertstrid(1000230)]'
return