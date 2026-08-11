label avg24055(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200230)]' (**arg(1, 1200230))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200231)]' (**arg(2, 1200231))
hide p1
get_char('c7613') '[convertstrid(1200232)]' (**arg(3, 1200232))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200233)]' (**arg(4, 1200233))
return "avg24055"