label avg24503(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1206004)]' (**arg(1, 1206004))
return "avg24503"