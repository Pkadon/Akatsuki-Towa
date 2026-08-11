label avg29005(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1216031)]' (**arg(1, 1216031))
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216032)]' (**arg(2, 1216032))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216033)]' (**arg(3, 1216033))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216034)]' (**arg(4, 1216034))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216035)]' (**arg(5, 1216035))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216036)]' (**arg(6, 1216036))
hide p1
get_char('c13') '[convertstrid(1216037)]' (**arg(7, 1216037))
return "avg29005"