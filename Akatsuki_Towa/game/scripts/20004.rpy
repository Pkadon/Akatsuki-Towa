label avg20004:

play music "ed9997.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[convertstrid(1000214)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1000215)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1000216)]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1000217)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1000218)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1000219)]'
hide p1
play sfx2 "common_remind.ogg"
c0 '[convertstrid(1000220)]'
c0 '[convertstrid(1000221)]'
c0 '[convertstrid(1000223)]'
return