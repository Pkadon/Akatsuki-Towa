label avg10552(trans=fade_in):

$ play_music("ED6102.ogg")
scene avg_bg_105
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
$ update_narrator('c2401')
window show
with trans
play sfx2 "other_7061.ogg"
get_char('c2401') '[convertstrid(1153652)]' (**arg(1, 1153652))
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
play sfx2 "other_7061.ogg"
get_char('c2401') '[convertstrid(1153653)]' (**arg(2, 1153653))
$ update_portrait('st041_01 1', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('st050_01 5', 'p257', [r(-11), r_shake, light], 6)
get_char('c2573') '[convertstrid(1153654)]' (**arg(3, 1153654))
$ update_portrait('st050_01 1', 'p257', [r(-11), light], 6)
get_char('c2573') '[convertstrid(1153655)]' (**arg(4, 1153655))
$ update_portrait('st050_01 5', 'p257', [r(-11), light], 6)
get_char('c2573') '[convertstrid(1153656)]' (**arg(5, 1153656))
$ update_portrait('st050_01 5', 'p257', [r(-11), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153657)]' (**arg(6, 1153657))
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153658)]' (**arg(7, 1153658))
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153659)]' (**arg(8, 1153659))
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153660)]' (**arg(9, 1153660))
$ update_portrait('st041_01 1', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('st050_01 5', 'p257', [r(-11), light], 6)
get_char('c2573') '[convertstrid(1153661)]' (**arg(10, 1153661))
$ update_portrait('st050_01 5', 'p257', [r(-11), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153662)]' (**arg(11, 1153662))
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153663)]' (**arg(12, 1153663))
$ update_portrait('st041_01 4', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('st050_01 1', 'p257', [r(-11), light], 6)
get_char('c2573') '[convertstrid(1153664)]' (**arg(13, 1153664))
$ update_portrait('st050_01 1', 'p257', [r(-11), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1153665)]' (**arg(14, 1153665))
hide p240
hide p257
get_char('c0') '[convertstrid(1153666)]' (**arg(15, 1153666))
return "avg10552"