label avg10854:

$ play_music("ed7510.ogg")
scene avg_bg_218
$ update_portrait('oc003_01 20', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
play sfx2 "other_7057.ogg"
get_char('c33') '[convertstrid(1189627)]' (**arg(1, 1189627))
$ update_portrait('oc003_01 20', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1189628)]' (**arg(2, 1189628))
hide p3
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1189629)]' (**arg(3, 1189629))
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1189630)]' (**arg(4, 1189630))
hide p2
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('oc007_02 1', 'p2623', [l(-24), light, flip], 6)
get_char('c26231') '[convertstrid(1189631)]' (**arg(5, 1189631))
hide p2623
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1189632)]' (**arg(6, 1189632))
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1189633)]' (**arg(7, 1189633))
hide p1
$ update_portrait('oc008_01 2', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1189634)]' (**arg(8, 1189634))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1189635)]' (**arg(9, 1189635))
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1189636)]' (**arg(10, 1189636))
hide p8
$ update_portrait('oc007_02 1', 'p2623', [l(-24), light, flip], 6)
get_char('c26231') '[convertstrid(1189637)]' (**arg(11, 1189637))
stop music
$ update_portrait('oc007_02 3', 'p2623', [l(-24), l_shake, light, flip], 6)
get_char('c26231') '[convertstrid(1189638)]' (**arg(12, 1189638))
hide p2623
$ update_portrait('oc008_01 3', 'p8', [l(-5), l_shake, light, flip], 6)
get_char('c81') '[convertstrid(1189639)]' (**arg(13, 1189639))
hide p8
$ update_portrait('oc007_02 3', 'p2623', [l(-24), light, flip], 6)
get_char('c26231') '[convertstrid(1189640)]' (**arg(14, 1189640))
hide p2623
$ update_portrait('oc008_01 3', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1189641)]' (**arg(15, 1189641)) with shake
hide p4
$ update_portrait('oc008_01 3', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('st063_01 2', 'p1346', [r(-16), light], 6)
get_char('c13463') '[convertstrid(1189642)]' (**arg(16, 1189642))
return