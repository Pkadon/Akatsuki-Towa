label avg20116:

stop music
scene placeholderbackground
$ update_narrator('c6963')
window show
with fade_in
get_char('c6963') '[convertstrid(1005614)]' (**arg(1, 1005614))
get_char('c6963') '[convertstrid(1005615)]' (**arg(2, 1005615))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1005616)]' (**arg(3, 1005616))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1005617)]' (**arg(4, 1005617))
hide p1
get_char('c6973') '[convertstrid(1005618)]' (**arg(5, 1005618))
get_char('c6973') '[convertstrid(1005619)]' (**arg(6, 1005619))
get_char('c6963') '[convertstrid(1005620)]' (**arg(7, 1005620))
$ update_portrait('sc039_01 5', 'p46', [mid(-13), light], 6)
get_char('c463') '[convertstrid(1005621)]' (**arg(8, 1005621))
return