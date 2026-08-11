label avg101920(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1218376)]' (**arg(1, 1218376))
hide p1
$ update_portrait('sc011_01 2', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218377)]' (**arg(2, 1218377))
hide p19
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218378)]' (**arg(3, 1218378))
hide p1
$ update_portrait('sc011_01 1', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218379)]' (**arg(4, 1218379))
$ update_portrait('sc011_01 5', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218380)]' (**arg(5, 1218380))
hide p19
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218381)]' (**arg(6, 1218381))
return "avg101920"