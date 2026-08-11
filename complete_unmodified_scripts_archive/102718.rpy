label avg102718(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
$ update_narrator('c273')
window show
with trans
get_char('c273') '[convertstrid(1219479)]' (**arg(1, 1219479))
hide p27
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219480)]' (**arg(2, 1219480))
hide p1
$ update_portrait('sc019_01 4', 'p27', [mid(-18), light], 6)
get_char('c273') '[convertstrid(1219481)]' (**arg(3, 1219481))
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
get_char('c273') '[convertstrid(1219482)]' (**arg(4, 1219482))
hide p27
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219483)]' (**arg(5, 1219483))
return "avg102718"