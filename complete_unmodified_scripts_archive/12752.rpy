label avg12752(trans=fade_in):

$ play_music("ed7544.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1174312)]' (**arg(1, 1174312))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1174313)]' (**arg(2, 1174313))
hide p1
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1174314)]' (**arg(3, 1174314))
hide p1304
hide p3
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1174315)]' (**arg(4, 1174315)) with shake
get_char('c14661') '[convertstrid(1174316)]' (**arg(5, 1174316))
get_char('c14581') '[convertstrid(1174317)]' (**arg(6, 1174317))
get_char('c14581') '[convertstrid(1174318)]' (**arg(7, 1174318))
get_char('c14601') '[convertstrid(1174319)]' (**arg(8, 1174319))
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1174320)]' (**arg(9, 1174320))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174321)]' (**arg(10, 1174321))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174322)]' (**arg(11, 1174322))
return "avg12752"