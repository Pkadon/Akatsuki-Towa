label avg10306(trans=fade_in):

$ play_music("ed7126.ogg")
scene avg_bg_074
$ update_narrator('c2291')
window show
with trans
$ update_portrait('st030_01 1', 'p229', [l_entrance(-8), light, flip], 6)
play sfx2 "other_7044.ogg"
get_char('c2291') '[convertstrid(1130199)]' (**arg(1, 1130199))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130200)]' (**arg(2, 1130200))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130201)]' (**arg(3, 1130201))
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130202)]' (**arg(4, 1130202))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130203)]' (**arg(5, 1130203))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130204)]' (**arg(6, 1130204))
hide p1
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c33') '[convertstrid(1130205)]' (**arg(7, 1130205))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130206)]' (**arg(8, 1130206))
hide p3
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c43') '[convertstrid(1130207)]' (**arg(9, 1130207))
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130208)]' (**arg(10, 1130208))
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130209)]' (**arg(11, 1130209))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 5', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130210)]' (**arg(12, 1130210))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130211)]' (**arg(13, 1130211))
hide p1
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130212)]' (**arg(14, 1130212))
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1130213)]' (**arg(15, 1130213))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130214)]' (**arg(16, 1130214))
$ update_portrait('st030_01 2', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130215)]' (**arg(17, 1130215))
hide p1
$ update_portrait('st030_01 2', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1130216)]' (**arg(18, 1130216))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130217)]' (**arg(19, 1130217))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130218)]' (**arg(20, 1130218))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130219)]' (**arg(21, 1130219))
$ update_portrait('st030_01 5', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130220)]' (**arg(22, 1130220))
hide p2
$ update_portrait('st030_01 5', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130221)]' (**arg(23, 1130221))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130222)]' (**arg(24, 1130222))
return "avg10306"