label avg101819(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1222201)]' (**arg(1, 1222201))
hide p1
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222202)]' (**arg(2, 1222202))
hide p18
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222203)]' (**arg(3, 1222203))
hide p1
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222204)]' (**arg(4, 1222204))
hide p18
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222205)]' (**arg(5, 1222205))
hide p1
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222206)]' (**arg(6, 1222206))
return "avg101819"