label avg12509:

$ play_music("ed7101.ogg")
scene avg_bg_011
$ update_narrator('c9521')
window show
with fade_in
get_char('c9521') '[convertstrid(1150930)]' (**arg(1, 1150930))
get_char('c9521') '[convertstrid(1150931)]' (**arg(2, 1150931))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150932)]' (**arg(3, 1150932))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c9521') '[convertstrid(1150933)]' (**arg(4, 1150933))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150934)]' (**arg(5, 1150934))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c9521') '[convertstrid(1150935)]' (**arg(6, 1150935))
get_char('c9531') '[convertstrid(1150936)]' (**arg(7, 1150936))
get_char('c9521') '[convertstrid(1150937)]' (**arg(8, 1150937))
get_char('c9521') '[convertstrid(1150938)]' (**arg(9, 1150938))
get_char('c9531') '[convertstrid(1150939)]' (**arg(10, 1150939))
get_char('c9531') '[convertstrid(1150940)]' (**arg(11, 1150940))
get_char('c9531') '[convertstrid(1150941)]' (**arg(12, 1150941))
get_char('c9531') '[convertstrid(1150942)]' (**arg(13, 1150942))
hide p2
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150943)]' (**arg(14, 1150943))
hide p3
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150944)]' (**arg(15, 1150944))
return