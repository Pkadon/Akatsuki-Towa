label avg101919(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc011_01 5', 'p19', [mid(-1), light], 6)
$ update_narrator('c193')
window show
with trans
get_char('c193') '[convertstrid(1218368)]' (**arg(1, 1218368))
hide p19
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218369)]' (**arg(2, 1218369))
hide p1
$ update_portrait('sc011_01 5', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218370)]' (**arg(3, 1218370))
hide p19
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218371)]' (**arg(4, 1218371))
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218372)]' (**arg(5, 1218372))
hide p1
$ update_portrait('sc011_01 1', 'p19', [mid(-1), light], 6)
get_char('c193') '[convertstrid(1218373)]' (**arg(6, 1218373))
hide p19
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218374)]' (**arg(7, 1218374))
return "avg101919"