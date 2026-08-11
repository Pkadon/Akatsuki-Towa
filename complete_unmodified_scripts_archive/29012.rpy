label avg29012(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc049_01 1', 'p56', [mid(-8), light], 6)
$ update_narrator('c563')
window show
with trans
get_char('c563') '[convertstrid(1007046)]' (**arg(1, 1007046))
$ update_portrait('sc049_01 6', 'p56', [mid(-8), light], 6)
get_char('c563') '[convertstrid(1000133)]' (**arg(2, 1000133))
$ update_portrait('sc049_01 6', 'p56', [mid(-8), light], 6)
get_char('c563') '[convertstrid(1000134)]' (**arg(3, 1000134))
return "avg29012"