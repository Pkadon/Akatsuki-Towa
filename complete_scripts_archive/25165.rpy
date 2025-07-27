label avg25165:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210539)]'
hide p1
play sfx2 "other_7082.ogg"
c20173 '[convertstrid(1210540)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210541)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210542)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1210543)]'
return