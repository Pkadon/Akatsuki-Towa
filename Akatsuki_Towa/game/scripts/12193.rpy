label avg12193(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_039
$ update_narrator('c9853')
window show
with trans
get_char('c9853') '[convertstrid(1120754)]' (**arg(1, 1120754))
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c21') '[convertstrid(1120755)]' (**arg(2, 1120755))
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
get_char('c9853') '[convertstrid(1120756)]' (**arg(3, 1120756))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120757)]' (**arg(4, 1120757))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c9853') '[convertstrid(1120758)]' (**arg(5, 1120758))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120759)]' (**arg(6, 1120759))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c9853') '[convertstrid(1120760)]' (**arg(7, 1120760))
get_char('c9853') '[convertstrid(1120761)]' (**arg(8, 1120761))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1120762)]' (**arg(9, 1120762))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
get_char('c9853') '[convertstrid(1120763)]' (**arg(10, 1120763))
get_char('c9853') '[convertstrid(1120764)]' (**arg(11, 1120764))
get_char('c9853') '[convertstrid(1120765)]' (**arg(12, 1120765))
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120766)]' (**arg(13, 1120766))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120767)]' (**arg(14, 1120767))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c9853') '[convertstrid(1120768)]' (**arg(15, 1120768))
return "avg12193"