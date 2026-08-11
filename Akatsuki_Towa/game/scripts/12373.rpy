label avg12373(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_058
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfx2 "other_7021.ogg"
get_char('c21') '[convertstrid(1134058)]' (**arg(1, 1134058))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1134059)]' (**arg(2, 1134059))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1134060)]' (**arg(3, 1134060))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1134062)]' (**arg(4, 1134062))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134063)]' (**arg(5, 1134063))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134064)]' (**arg(6, 1134064))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1134065)]' (**arg(7, 1134065))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134066)]' (**arg(8, 1134066))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134067)]' (**arg(9, 1134067))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfx2 "other_7079.ogg"
get_char('c13') '[convertstrid(1134068)]' (**arg(10, 1134068))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1134069)]' (**arg(11, 1134069))
return "avg12373"