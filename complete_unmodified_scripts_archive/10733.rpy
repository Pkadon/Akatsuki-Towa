label avg10733(trans=fade_in):

$ play_music("ed6564.ogg")
scene avg_bg_038
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1172525)]' (**arg(1, 1172525))
$ update_portrait('st063_01 4', 'p1346', [l(-16), light, flip], 6)
get_char('c13461') '[convertstrid(1172526)]' (**arg(2, 1172526))
hide p1346
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172527)]' (**arg(3, 1172527))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172528)]' (**arg(4, 1172528))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st063_01 4', 'p1346', [l(-16), light, flip], 6)
get_char('c13461') '[convertstrid(1172529)]' (**arg(5, 1172529))
$ update_portrait('st063_01 4', 'p1346', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172530)]' (**arg(6, 1172530))
hide p1346
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172531)]' (**arg(7, 1172531))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172532)]' (**arg(8, 1172532))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172533)]' (**arg(9, 1172533))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st063_01 1', 'p1346', [l(-16), light, flip], 6)
get_char('c13461') '[convertstrid(1172534)]' (**arg(10, 1172534))
return "avg10733"