label avg25023(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7086.ogg"
get_char('c23') '[convertstrid(1210055)]' (**arg(1, 1210055))
hide p2
get_char('c20103') '[convertstrid(1210056)]' (**arg(2, 1210056))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210057)]' (**arg(3, 1210057))
return "avg25023"