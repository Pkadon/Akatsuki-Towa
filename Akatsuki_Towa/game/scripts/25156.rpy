label avg25156:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "elc_5002.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[convertstrid(1210496)]'
hide p1
c6123 '[convertstrid(1210497)]'
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[convertstrid(1210498)]'
return