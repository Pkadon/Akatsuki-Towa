label avg25809:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1211274)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1211275)]'
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "elc_5001.ogg"
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1211276)]'
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1211277)]'
return