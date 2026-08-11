label avg103019(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1222458)]' (**arg(1, 1222458))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222459)]' (**arg(2, 1222459))
hide p30
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222460)]' (**arg(3, 1222460))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222461)]' (**arg(4, 1222461))
hide p30
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222462)]' (**arg(5, 1222462))
return "avg103019"