label avg12508:

$ play_music("ed7150.ogg")
scene avg_bg_008
$ update_narrator('c12141')
window show
with fade_in
get_char('c12141') '[convertstrid(1150912)]' (**arg(1, 1150912))
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150913)]' (**arg(2, 1150913))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
get_char('c12141') '[convertstrid(1150914)]' (**arg(3, 1150914))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1150915)]' (**arg(4, 1150915))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12141') '[convertstrid(1150916)]' (**arg(5, 1150916))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150917)]' (**arg(6, 1150917))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c12141') '[convertstrid(1150918)]' (**arg(7, 1150918))
get_char('c12141') '[convertstrid(1150919)]' (**arg(8, 1150919))
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150920)]' (**arg(9, 1150920))
hide p3
get_char('c0') '[convertstrid(1150921)]' (**arg(10, 1150921))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150922)]' (**arg(11, 1150922))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150923)]' (**arg(12, 1150923))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150924)]' (**arg(13, 1150924))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150925)]' (**arg(14, 1150925))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150926)]' (**arg(15, 1150926))
hide p2
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150927)]' (**arg(16, 1150927))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150928)]' (**arg(17, 1150928))
return