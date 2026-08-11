label avg12666(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1166617)]' (**arg(1, 1166617))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166618)]' (**arg(2, 1166618))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c13671') '[convertstrid(1166619)]' (**arg(3, 1166619))
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1166620)]' (**arg(4, 1166620))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1166621)]' (**arg(5, 1166621)) with shake
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
play sfx2 "other_7081.ogg"
get_char('c13691') '[convertstrid(1166622)]' (**arg(6, 1166622))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166623)]' (**arg(7, 1166623))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166624)]' (**arg(8, 1166624))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
get_char('c13661') '[convertstrid(1166625)]' (**arg(9, 1166625))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166626)]' (**arg(10, 1166626))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166627)]' (**arg(11, 1166627))
hide p4
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166628)]' (**arg(12, 1166628))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166629)]' (**arg(13, 1166629))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166630)]' (**arg(14, 1166630))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166631)]' (**arg(15, 1166631))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166632)]' (**arg(16, 1166632))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c13663') '[convertstrid(1166633)]' (**arg(17, 1166633))
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1166634)]' (**arg(18, 1166634))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166635)]' (**arg(19, 1166635))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c13671') '[convertstrid(1166636)]' (**arg(20, 1166636))
hide p4
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166637)]' (**arg(21, 1166637))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1166638)]' (**arg(22, 1166638))
hide p1
get_char('c13671') '[convertstrid(1166639)]' (**arg(23, 1166639))
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166640)]' (**arg(24, 1166640))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c13671') '[convertstrid(1166641)]' (**arg(25, 1166641))
hide p4
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166642)]' (**arg(26, 1166642))
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
get_char('c13671') '[convertstrid(1166643)]' (**arg(27, 1166643))
return "avg12666"