label avg101118(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc003_01 2', 'p11', [mid(-4), light], 6)
$ update_narrator('c113')
window show
with trans
get_char('c113') '[convertstrid(1220427)]' (**arg(1, 1220427))
hide p11
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220428)]' (**arg(2, 1220428))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220429)]' (**arg(3, 1220429))
hide p1
$ update_portrait('sc003_01 6', 'p11', [mid(-4), light], 6)
get_char('c113') '[convertstrid(1220430)]' (**arg(4, 1220430))
hide p11
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220431)]' (**arg(5, 1220431))
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220432)]' (**arg(6, 1220432))
return "avg101118"