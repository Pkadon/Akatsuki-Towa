label avg10541:

$ play_music("ed7151.ogg")
scene avg_bg_078
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1152681)]' (**arg(1, 1152681))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152682)]' (**arg(2, 1152682))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1152683)]' (**arg(3, 1152683))
hide p2
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152684)]' (**arg(4, 1152684))
hide p239
hide p3
$ update_narrator('c43')
with fade
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1152685)]' (**arg(5, 1152685))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152686)]' (**arg(6, 1152686))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c12401') '[convertstrid(1152687)]' (**arg(7, 1152687))
get_char('c12401') '[convertstrid(1152688)]' (**arg(8, 1152688))
hide p1
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152689)]' (**arg(9, 1152689))
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
get_char('c12401') '[convertstrid(1152690)]' (**arg(10, 1152690))
get_char('c12401') '[convertstrid(1152691)]' (**arg(11, 1152691))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152692)]' (**arg(12, 1152692))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152693)]' (**arg(13, 1152693))
return