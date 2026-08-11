label avg24003(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200011)]' (**arg(1, 1200011))
hide p1
$ update_portrait('st044_01 1', 'p243', [mid(10), light], 6)
get_char('c2433') '[convertstrid(1200012)]' (**arg(2, 1200012))
hide p243
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200013)]' (**arg(3, 1200013))
return "avg24003"