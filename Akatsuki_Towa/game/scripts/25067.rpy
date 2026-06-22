label avg25067:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1210202)]' (**arg(1, 1210202))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1210203)]' (**arg(2, 1210203))
hide p1
play sfx2 "fight_6028.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
get_char('c0') '[convertstrid(1210204)]' (**arg(3, 1210204))
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210205)]' (**arg(4, 1210205))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210206)]' (**arg(5, 1210206))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c23') '[convertstrid(1210207)]' (**arg(6, 1210207))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1210208)]' (**arg(7, 1210208))
return