label avg101801(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1222146)]' (**arg(1, 1222146))
hide p1
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222147)]' (**arg(2, 1222147))
hide p18
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222148)]' (**arg(3, 1222148))
hide p1
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222149)]' (**arg(4, 1222149))
$ update_portrait('sc010_01 4', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222150)]' (**arg(5, 1222150))
hide p18
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222151)]' (**arg(6, 1222151))
return "avg101801"