label avg25133:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[convertstrid(1210400)]'
hide p1
c20133 '[convertstrid(1210401)]'
c20133 '[convertstrid(1210402)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1210403)]'
hide p2
c20133 '[convertstrid(1210404)]'
return