label avg25107:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "other_7092.ogg"
get_char('c6123') '[convertstrid(1210311)]' (**arg(1, 1210311))
get_char('c6123') '[convertstrid(1210312)]' (**arg(2, 1210312))
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1210313)]' (**arg(3, 1210313))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210314)]' (**arg(4, 1210314))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1210315)]' (**arg(5, 1210315))
return