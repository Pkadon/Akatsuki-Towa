label avg25225:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210790)]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210791)]'
hide p1
c20193 '[convertstrid(1210792)]'
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[convertstrid(1210793)]'
return