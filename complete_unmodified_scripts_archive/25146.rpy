label avg25146:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 3', 'p2014', [mid(6), light], 6)
$ update_narrator('c20143')
window show
with fade_in
c20143 '[convertstrid(1210463)]'
hide p2014
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210464)]'
hide p1
$ update_portrait('uc001_02 3', 'p2014', [mid(6), light], 6)
c20143 '[convertstrid(1210465)]'
hide p2014
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[convertstrid(1210466)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1210467)]'
return