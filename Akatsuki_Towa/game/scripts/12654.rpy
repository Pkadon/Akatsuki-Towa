label avg12654(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1166344)]' (**arg(1, 1166344))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166345)]' (**arg(2, 1166345))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166346)]' (**arg(3, 1166346))
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "other_7087.ogg"
get_char('c23') '[convertstrid(1166347)]' (**arg(4, 1166347))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166348)]' (**arg(5, 1166348))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166349)]' (**arg(6, 1166349))
hide p3
$ update_portrait('oc004_01 17', 'p4', [r(-5), dark], 5)
get_char('c13351') '[convertstrid(1166350)]' (**arg(7, 1166350))
get_char('c13351') '[convertstrid(1166351)]' (**arg(8, 1166351))
get_char('c13351') '[convertstrid(1166352)]' (**arg(9, 1166352))
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166353)]' (**arg(10, 1166353))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166354)]' (**arg(11, 1166354))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166355)]' (**arg(12, 1166355))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166356)]' (**arg(13, 1166356))
hide p3
get_char('c13351') '[convertstrid(1166357)]' (**arg(14, 1166357))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166358)]' (**arg(15, 1166358))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166359)]' (**arg(16, 1166359))
get_char('c13351') '[convertstrid(1166360)]' (**arg(17, 1166360))
get_char('c13351') '[convertstrid(1166361)]' (**arg(18, 1166361))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166362)]' (**arg(19, 1166362))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166363)]' (**arg(20, 1166363))
return "avg12654"