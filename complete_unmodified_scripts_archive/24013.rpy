label avg24013(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200051)]' (**arg(1, 1200051))
hide p1
get_char('c7633') '[convertstrid(1200052)]' (**arg(2, 1200052))
get_char('c7633') '[convertstrid(1200053)]' (**arg(3, 1200053))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200054)]' (**arg(4, 1200054))
hide p1
get_char('c7633') '[convertstrid(1200055)]' (**arg(5, 1200055))
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200056)]' (**arg(6, 1200056))
hide p2
get_char('c7633') '[convertstrid(1200057)]' (**arg(7, 1200057))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200058)]' (**arg(8, 1200058))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200059)]' (**arg(9, 1200059))
hide p1
get_char('c7633') '[convertstrid(1200060)]' (**arg(10, 1200060))
return "avg24013"