label avg101803(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 2', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with trans
get_char('c183') '[convertstrid(1222159)]' (**arg(1, 1222159))
hide p18
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222160)]' (**arg(2, 1222160))
hide p1
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222161)]' (**arg(3, 1222161))
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222162)]' (**arg(4, 1222162))
hide p18
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222163)]' (**arg(5, 1222163))
hide p1
$ update_portrait('sc010_01 4', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222164)]' (**arg(6, 1222164))
return "avg101803"