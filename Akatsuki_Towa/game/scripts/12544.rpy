label avg12544(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_039
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1152942)]' (**arg(1, 1152942))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st026_01 1', 'p225', [l_entrance(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1152943)]' (**arg(2, 1152943))
$ update_portrait('st026_01 2', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1152944)]' (**arg(3, 1152944))
hide p1
$ update_portrait('st026_01 2', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1152945)]' (**arg(4, 1152945))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152946)]' (**arg(5, 1152946))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st026_01 4', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1152947)]' (**arg(6, 1152947))
hide p4
$ update_portrait('st026_01 4', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1152948)]' (**arg(7, 1152948))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152949)]' (**arg(8, 1152949))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152950)]' (**arg(9, 1152950))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st026_01 1', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1152951)]' (**arg(10, 1152951))
return "avg12544"