label avg12578(trans=fade_in):

$ play_music("ED6523.ogg")
scene avg_bg_080
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1155359)]' (**arg(1, 1155359))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1155360)]' (**arg(2, 1155360))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155361)]' (**arg(3, 1155361))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1155362)]' (**arg(4, 1155362))
hide p3
hide p1
$ update_narrator('c12611')
with fade
get_char('c12611') '[convertstrid(1155363)]' (**arg(5, 1155363))
$ update_portrait('sc021_01 1', 'p29', [r(-17), light], 6)
get_char('c293') '[convertstrid(1155364)]' (**arg(6, 1155364))
$ update_portrait('sc021_01 1', 'p29', [r(-17), dark], 5)
get_char('c12611') '[convertstrid(1155365)]' (**arg(7, 1155365))
get_char('c12611') '[convertstrid(1155366)]' (**arg(8, 1155366))
hide p29
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155367)]' (**arg(9, 1155367))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12611') '[convertstrid(1155368)]' (**arg(10, 1155368))
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1155369)]' (**arg(11, 1155369))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c12611') '[convertstrid(1155370)]' (**arg(12, 1155370))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1155371)]' (**arg(13, 1155371))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155372)]' (**arg(14, 1155372))
hide p4
hide p1
$ update_narrator('c12611')
with fade
get_char('c12611') '[convertstrid(1155373)]' (**arg(15, 1155373))
return "avg12578"