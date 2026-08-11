label avg29046(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1100041)]' (**arg(1, 1100041))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1100042)]' (**arg(2, 1100042))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1100043)]' (**arg(3, 1100043))
return "avg29046"