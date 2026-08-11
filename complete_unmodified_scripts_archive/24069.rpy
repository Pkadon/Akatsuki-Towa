label avg24069(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200273)]' (**arg(1, 1200273))
hide p2
get_char('c7553') '[convertstrid(1200274)]' (**arg(2, 1200274))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200275)]' (**arg(3, 1200275))
return "avg24069"