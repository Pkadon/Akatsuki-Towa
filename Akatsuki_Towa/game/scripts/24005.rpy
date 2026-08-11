label avg24005(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200016)]' (**arg(1, 1200016))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200017)]' (**arg(2, 1200017))
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200018)]' (**arg(3, 1200018))
return "avg24005"