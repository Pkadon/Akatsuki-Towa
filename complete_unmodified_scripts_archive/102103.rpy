label avg102103(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218813)]' (**arg(1, 1218813))
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218814)]' (**arg(2, 1218814))
hide p21
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218815)]' (**arg(3, 1218815))
hide p1
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218816)]' (**arg(4, 1218816))
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218817)]' (**arg(5, 1218817))
hide p21
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218818)]' (**arg(6, 1218818))
return "avg102103"