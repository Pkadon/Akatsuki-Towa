label avg24516(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1206042)]' (**arg(1, 1206042))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1206043)]' (**arg(2, 1206043))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1206044)]' (**arg(3, 1206044))
return "avg24516"