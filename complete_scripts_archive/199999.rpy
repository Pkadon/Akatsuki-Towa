label avg199999:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na19.ogg"
c13 '[convertstrid(1218313)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1218314)]'
return