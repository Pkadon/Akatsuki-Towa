label avg24508(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1206017)]' (**arg(1, 1206017))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1206018)]' (**arg(2, 1206018))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1206019)]' (**arg(3, 1206019))
return "avg24508"