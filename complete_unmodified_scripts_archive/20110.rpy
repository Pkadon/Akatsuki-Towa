label avg20110(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1005374)]' (**arg(1, 1005374))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1005375)]' (**arg(2, 1005375))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1005376)]' (**arg(3, 1005376))
hide p1
$ update_portrait('sc025_01 2', 'p622', [mid(-1), light], 6)
get_char('c6223') '[convertstrid(1005377)]' (**arg(4, 1005377))
hide p622
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1005378)]' (**arg(5, 1005378))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1005379)]' (**arg(6, 1005379))
return "avg20110"