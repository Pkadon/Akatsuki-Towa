label avg12034(trans=fade_in):

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c7171')
window show
with trans
get_char('c7171') '[convertstrid(1120197)]' (**arg(1, 1120197))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120198)]' (**arg(2, 1120198))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
get_char('c7171') '[convertstrid(1120199)]' (**arg(3, 1120199))
$ update_portrait('st033_01 3', 'p232', [r(-7), r_shake, light], 6)
get_char('c2323') '[convertstrid(1120200)]' (**arg(4, 1120200))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c21') '[convertstrid(1120201)]' (**arg(5, 1120201))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120202)]' (**arg(6, 1120202))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120203)]' (**arg(7, 1120203))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st033_01 2', 'p232', [r(-7), r_shake, light], 6)
get_char('c2323') '[convertstrid(1120204)]' (**arg(8, 1120204))
$ update_portrait('st033_01 2', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1120205)]' (**arg(9, 1120205))
hide p232
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
get_char('c7173') '[convertstrid(1120206)]' (**arg(10, 1120206))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1120207)]' (**arg(11, 1120207))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c7173') '[convertstrid(1120208)]' (**arg(12, 1120208))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1120209)]' (**arg(13, 1120209))
hide p1
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_c03_01.ogg"
get_char('c21') '[convertstrid(1120210)]' (**arg(14, 1120210))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121550)]' (**arg(15, 1121550))
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120211)]' (**arg(16, 1120211))
hide p232
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
get_char('c7173') '[convertstrid(1120212)]' (**arg(17, 1120212))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1120213)]' (**arg(18, 1120213))
return "avg12034"