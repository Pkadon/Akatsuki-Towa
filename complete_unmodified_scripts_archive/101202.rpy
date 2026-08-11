label avg101202(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220654)]' (**arg(1, 1220654))
hide p1
$ update_portrait('sc004_01 1', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220655)]' (**arg(2, 1220655))
$ update_portrait('sc004_01 4', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220656)]' (**arg(3, 1220656))
hide p12
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220657)]' (**arg(4, 1220657))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220658)]' (**arg(5, 1220658))
hide p1
$ update_portrait('sc004_01 5', 'p12', [mid(-12), light], 6)
get_char('c123') '[convertstrid(1220659)]' (**arg(6, 1220659))
hide p12
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220660)]' (**arg(7, 1220660))
return "avg101202"