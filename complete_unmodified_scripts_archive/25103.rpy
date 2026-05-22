label avg25103:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[convertstrid(1210290)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1210291)]'
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210292)]'
hide p1
c20073 '[convertstrid(1210293)]'
return