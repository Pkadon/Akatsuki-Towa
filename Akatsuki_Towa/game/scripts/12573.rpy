label avg12573:

$ play_music("ED6102.ogg")
scene avg_bg_023
$ update_narrator('c12321')
window show
with fade_in
get_char('c12321') '[convertstrid(1155183)]' (**arg(1, 1155183))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155184)]' (**arg(2, 1155184))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155185)]' (**arg(3, 1155185))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12321') '[convertstrid(1155186)]' (**arg(4, 1155186))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155187)]' (**arg(5, 1155187))
hide p1
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1155188)]' (**arg(6, 1155188))
return