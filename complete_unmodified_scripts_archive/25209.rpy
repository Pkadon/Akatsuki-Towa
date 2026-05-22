label avg25209:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch28.ogg"
c23 '[convertstrid(1210721)]'
hide p2
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfx2 "other_7043.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1210722)]'
hide p1
$ update_portrait('oc002_01 16', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6020.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[convertstrid(1210723)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1210724)]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfx2 "elc_5002.ogg"
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[convertstrid(1210725)]'
return