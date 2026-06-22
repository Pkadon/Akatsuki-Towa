label avg25155:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
get_char('c6123') '[convertstrid(1210491)]' (**arg(1, 1210491))
get_char('c6123') '[convertstrid(1210492)]' (**arg(2, 1210492))
play sfx2 "other_7034.ogg"
get_char('c0') '[convertstrid(1210493)]' (**arg(3, 1210493))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c23') '[convertstrid(1210494)]' (**arg(4, 1210494))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210495)]' (**arg(5, 1210495))
return