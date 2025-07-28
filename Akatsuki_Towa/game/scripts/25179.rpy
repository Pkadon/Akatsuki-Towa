label avg25179:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210577)]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1210578)]'
hide p2
play sfx2 "other_7080.ogg"
c0 '[convertstrid(1210579)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210580)]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[convertstrid(1210581)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1210582)]'
return