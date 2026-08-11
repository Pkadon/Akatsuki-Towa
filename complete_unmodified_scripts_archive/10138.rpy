label avg10138(trans=fade_in):

$ play_music("ED6505.ogg")
scene avg_bg_028
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7033.ogg"
get_char('c0') '[convertstrid(1007688)]' (**arg(1, 1007688))
get_char('c5691') '[convertstrid(1002313)]' (**arg(2, 1002313))
get_char('c5691') '[convertstrid(1002314)]' (**arg(3, 1002314))
get_char('c5691') '[convertstrid(1002315)]' (**arg(4, 1002315))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1002316)]' (**arg(5, 1002316))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1002317)]' (**arg(6, 1002317))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfx2 "other_7021.ogg"
get_char('c13') '[convertstrid(1007413)]' (**arg(7, 1007413))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007414)]' (**arg(8, 1007414))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007415)]' (**arg(9, 1007415))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007416)]' (**arg(10, 1007416))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1007417)]' (**arg(11, 1007417))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007418)]' (**arg(12, 1007418))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007419)]' (**arg(13, 1007419))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007420)]' (**arg(14, 1007420))
return "avg10138"