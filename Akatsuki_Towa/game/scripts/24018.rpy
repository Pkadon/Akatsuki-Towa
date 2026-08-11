label avg24018(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c9853')
window show
with trans
get_char('c9853') '[convertstrid(1200078)]' (**arg(1, 1200078))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200079)]' (**arg(2, 1200079))
return "avg24018"