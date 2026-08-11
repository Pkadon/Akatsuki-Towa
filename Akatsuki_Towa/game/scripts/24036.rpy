label avg24036(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c7623')
window show
with trans
get_char('c7623') '[convertstrid(1200146)]' (**arg(1, 1200146))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200147)]' (**arg(2, 1200147))
return "avg24036"