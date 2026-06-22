label avg101820:

stop music
scene placeholderbackground
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with fade_in
get_char('c183') '[convertstrid(1222208)]' (**arg(1, 1222208))
hide p18
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222209)]' (**arg(2, 1222209))
hide p1
$ update_portrait('sc010_01 4', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222210)]' (**arg(3, 1222210))
hide p18
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222211)]' (**arg(4, 1222211))
hide p1
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222212)]' (**arg(5, 1222212))
hide p18
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222213)]' (**arg(6, 1222213))
return