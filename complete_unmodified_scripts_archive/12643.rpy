label avg12643(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_036
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
window show
with trans
get_char('c43') '[convertstrid(1163031)]' (**arg(1, 1163031))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1163032)]' (**arg(2, 1163032))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163033)]' (**arg(3, 1163033))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1163034)]' (**arg(4, 1163034))
$ play_music("ed7511.ogg")
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1163035)]' (**arg(5, 1163035)) with shake
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1163036)]' (**arg(6, 1163036))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1163037)]' (**arg(7, 1163037))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163038)]' (**arg(8, 1163038))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1163039)]' (**arg(9, 1163039))
return "avg12643"