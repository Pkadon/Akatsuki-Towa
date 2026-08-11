label avg24014(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200061)]' (**arg(1, 1200061))
hide p1
get_char('c7423') '[convertstrid(1200062)]' (**arg(2, 1200062))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200063)]' (**arg(3, 1200063))
return "avg24014"