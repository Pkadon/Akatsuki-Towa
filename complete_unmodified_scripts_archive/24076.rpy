label avg24076(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c9643')
window show
with trans
get_char('c9643') '[convertstrid(1200004)]' (**arg(1, 1200004))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200005)]' (**arg(2, 1200005))
return "avg24076"