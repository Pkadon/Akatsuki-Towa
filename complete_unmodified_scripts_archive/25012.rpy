label avg25012(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7043.ogg"
get_char('c13') '[convertstrid(1210020)]' (**arg(1, 1210020))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210021)]' (**arg(2, 1210021))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210022)]' (**arg(3, 1210022))
return "avg25012"