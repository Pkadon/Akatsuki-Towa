label avg101901(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1218315)]' (**arg(1, 1218315))
hide p1
$ update_portrait('sc011_01 4', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218316)]' (**arg(2, 1218316))
hide p19
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218317)]' (**arg(3, 1218317))
hide p1
$ update_portrait('sc011_01 1', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218318)]' (**arg(4, 1218318))
$ update_portrait('sc011_01 5', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218319)]' (**arg(5, 1218319))
hide p19
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218320)]' (**arg(6, 1218320))
return "avg101901"