label avg25206:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210703)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[convertstrid(1210704)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210705)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[convertstrid(1210706)]'
return