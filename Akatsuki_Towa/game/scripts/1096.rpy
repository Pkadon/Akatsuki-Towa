label avg1096:

$ play_music("ed7200.ogg")
scene avg_bg_010
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
$ update_narrator('c571')
window show
with fade_in
get_char('c571') '[convertstrid(2102201)]' (**arg(1, 2102201))
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102202)]' (**arg(2, 2102202))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102203)]' (**arg(3, 2102203))
hide p57
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
get_char('c10931') '[convertstrid(2102204)]' (**arg(4, 2102204))
get_char('c10931') '[convertstrid(2102205)]' (**arg(5, 2102205)) with shake
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(2102206)]' (**arg(6, 2102206))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
get_char('c10931') '[convertstrid(2102207)]' (**arg(7, 2102207))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102208)]' (**arg(8, 2102208))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102209)]' (**arg(9, 2102209))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(2102210)]' (**arg(10, 2102210))
hide p57
get_char('c10931') '[convertstrid(2102211)]' (**arg(11, 2102211))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(2102212)]' (**arg(12, 2102212))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c10931') '[convertstrid(2102213)]' (**arg(13, 2102213))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(2102214)]' (**arg(14, 2102214))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c10931') '[convertstrid(2102215)]' (**arg(15, 2102215))
hide p1
play sfx2 "other_7013.ogg"
get_char('c0') '[convertstrid(2102216)]' (**arg(16, 2102216))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102217)]' (**arg(17, 2102217))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(2102218)]' (**arg(18, 2102218))
$ update_portrait('sc050_01 5', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(2102219)]' (**arg(19, 2102219))
$ update_portrait('sc050_01 5', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102220)]' (**arg(20, 2102220))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102221)]' (**arg(21, 2102221))
return