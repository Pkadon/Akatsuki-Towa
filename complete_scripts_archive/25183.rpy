label avg25183:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[convertstrid(1210597)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1210598)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[convertstrid(1210599)]'
hide p2
c6123 '[convertstrid(1210600)]'
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na08.ogg"
c13 '[convertstrid(1210601)]'
return