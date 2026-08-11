label avg101918(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 5', 'p19', [mid(-1), light], 6)
$ update_narrator('c193')
window show
with trans
get_char('c193') '[convertstrid(1218361)]' (**arg(1, 1218361))
hide p19
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218362)]' (**arg(2, 1218362))
hide p1
$ update_portrait('sc011_01 4', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218363)]' (**arg(3, 1218363))
hide p19
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218364)]' (**arg(4, 1218364))
hide p1
$ update_portrait('sc011_01 1', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218365)]' (**arg(5, 1218365))
hide p19
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218366)]' (**arg(6, 1218366))
return "avg101918"