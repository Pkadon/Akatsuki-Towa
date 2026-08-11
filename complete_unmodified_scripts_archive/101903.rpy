label avg101903(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 1', 'p19', [mid(-1), light], 6)
$ update_narrator('c193')
window show
with trans
get_char('c193') '[convertstrid(1218327)]' (**arg(1, 1218327))
hide p19
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218328)]' (**arg(2, 1218328))
hide p1
$ update_portrait('sc011_01 4', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218329)]' (**arg(3, 1218329))
hide p19
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218330)]' (**arg(4, 1218330))
hide p1
$ update_portrait('sc011_01 5', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218331)]' (**arg(5, 1218331))
return "avg101903"