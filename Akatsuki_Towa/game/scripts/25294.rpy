label avg25294:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1211120)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1211121)]'
hide p1
c20153 '[convertstrid(1211122)]'
c20153 '[convertstrid(1211123)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7085.ogg"
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[convertstrid(1211124)]'
return