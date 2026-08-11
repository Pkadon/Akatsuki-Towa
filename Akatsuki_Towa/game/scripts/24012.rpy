label avg24012(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200041)]' (**arg(1, 1200041))
hide p1
$ update_portrait('st026_01 2', 'p225', [mid(-14), light], 6)
get_char('c2253') '[convertstrid(1200042)]' (**arg(2, 1200042))
$ update_portrait('st026_01 1', 'p225', [mid(-14), light], 6)
get_char('c2253') '[convertstrid(1200043)]' (**arg(3, 1200043))
hide p225
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200044)]' (**arg(4, 1200044))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200045)]' (**arg(5, 1200045))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200046)]' (**arg(6, 1200046))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200047)]' (**arg(7, 1200047))
hide p1
$ update_portrait('st026_01 1', 'p225', [mid(-14), light], 6)
get_char('c2253') '[convertstrid(1200048)]' (**arg(8, 1200048))
hide p225
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200049)]' (**arg(9, 1200049))
hide p1
$ update_portrait('st026_01 1', 'p225', [mid(-14), light], 6)
get_char('c2253') '[convertstrid(1200050)]' (**arg(10, 1200050))
return "avg24012"