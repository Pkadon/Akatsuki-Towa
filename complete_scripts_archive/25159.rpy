label avg25159:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[convertstrid(1210506)]'
hide p2
play sfx2 "other_7057.ogg"
c0 '[convertstrid(1210507)]'
c6123 '[convertstrid(1210508)]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1210509)]'
hide p1
c20153 '[convertstrid(1210510)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210511)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210512)]'
hide p1
c20153 '[convertstrid(1210513)]'
play sfx2 "other_7085.ogg"
c0 '[convertstrid(1210514)]'
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1210515)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210516)]'
return