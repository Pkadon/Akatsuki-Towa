label avg24067(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200267)]' (**arg(1, 1200267))
hide p2
get_char('c7553') '[convertstrid(1200268)]' (**arg(2, 1200268))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200269)]' (**arg(3, 1200269))
return "avg24067"