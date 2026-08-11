label avg24016(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200066)]' (**arg(1, 1200066))
hide p2
get_char('c7563') '[convertstrid(1200067)]' (**arg(2, 1200067))
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200068)]' (**arg(3, 1200068))
hide p2
get_char('c7563') '[convertstrid(1200069)]' (**arg(4, 1200069))
get_char('c7563') '[convertstrid(1200070)]' (**arg(5, 1200070))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200071)]' (**arg(6, 1200071))
hide p2
get_char('c7563') '[convertstrid(1200072)]' (**arg(7, 1200072))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200073)]' (**arg(8, 1200073))
return "avg24016"