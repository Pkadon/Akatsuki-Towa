label avg12577:

$ play_music("ED6523.ogg")
scene avg_bg_080
$ update_narrator('c12611')
window show
with fade_in
get_char('c12611') '[convertstrid(1155350)]' (**arg(1, 1155350))
get_char('c12611') '[convertstrid(1155351)]' (**arg(2, 1155351))
$ update_portrait('uc004_02 1', 'p570', [r(-9), light], 6)
get_char('c5703') '[convertstrid(1155352)]' (**arg(3, 1155352))
hide p570
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1155353)]' (**arg(4, 1155353))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155354)]' (**arg(5, 1155354))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155355)]' (**arg(6, 1155355))
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1155356)]' (**arg(7, 1155356))
hide p4
hide p2
$ update_narrator('c12611')
with fade
get_char('c12611') '[convertstrid(1155357)]' (**arg(8, 1155357))
return