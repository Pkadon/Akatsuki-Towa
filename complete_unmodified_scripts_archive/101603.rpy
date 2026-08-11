label avg101603(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
$ update_narrator('c163')
window show
with trans
get_char('c163') '[convertstrid(1221532)]' (**arg(1, 1221532))
hide p16
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221533)]' (**arg(2, 1221533))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221534)]' (**arg(3, 1221534))
$ update_portrait('sc008_01 4', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221535)]' (**arg(4, 1221535))
hide p16
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221536)]' (**arg(5, 1221536))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221537)]' (**arg(6, 1221537))
return "avg101603"