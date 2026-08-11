label avg10102(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_037
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c11') '[convertstrid(1005660)]' (**arg(1, 1005660))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1005661)]' (**arg(2, 1005661))
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1005662)]' (**arg(3, 1005662))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005663)]' (**arg(4, 1005663))
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005664)]' (**arg(5, 1005664))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1005665)]' (**arg(6, 1005665))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005666)]' (**arg(7, 1005666))
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004401)]' (**arg(8, 1004401))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005668)]' (**arg(9, 1005668))
hide p2
$ update_portrait('sc040_01 1', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('sc039_01 2', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005669)]' (**arg(10, 1005669))
hide p47
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7072.ogg"
get_char('c11') '[convertstrid(1005670)]' (**arg(11, 1005670))
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c7013') '[convertstrid(1005671)]' (**arg(12, 1005671))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005672)]' (**arg(13, 1005672))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c7013') '[convertstrid(1005673)]' (**arg(14, 1005673))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005674)]' (**arg(15, 1005674))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c7013') '[convertstrid(1005675)]' (**arg(16, 1005675))
get_char('c7013') '[convertstrid(1005676)]' (**arg(17, 1005676))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c11') '[convertstrid(1005677)]' (**arg(18, 1005677))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005678)]' (**arg(19, 1005678))
hide p1
get_char('c0') '[convertstrid(1005679)]' (**arg(20, 1005679))
return "avg10102"