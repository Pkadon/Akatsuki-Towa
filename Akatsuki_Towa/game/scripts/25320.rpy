label avg25320:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[convertstrid(1211236)]'
hide p1
c20243 '[convertstrid(1211237)]'
c20243 '[convertstrid(1211238)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1211239)]'
hide p2
c20243 '[convertstrid(1211240)]'
return