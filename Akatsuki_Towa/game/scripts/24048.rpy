label avg24048(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200209)]' (**arg(1, 1200209))
hide p1
get_char('c7603') '[convertstrid(1200210)]' (**arg(2, 1200210))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200211)]' (**arg(3, 1200211))
return "avg24048"