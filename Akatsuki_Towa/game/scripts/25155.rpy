label avg25155:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[convertstrid(1210491)]'
c6123 '[convertstrid(1210492)]'
play sfx2 "other_7034.ogg"
c0 '[convertstrid(1210493)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_win_02.ogg"
c23 '[convertstrid(1210494)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210495)]'
return