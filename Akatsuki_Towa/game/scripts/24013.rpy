label avg24013(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1200051)]' (**arg(1, 1200051))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c7631') '[convertstrid(1200052)]' (**arg(2, 1200052))
get_char('c7631') '[convertstrid(1200053)]' (**arg(3, 1200053))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200054)]' (**arg(4, 1200054))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c7631') '[convertstrid(1200055)]' (**arg(5, 1200055))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200056)]' (**arg(6, 1200056))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c7631') '[convertstrid(1200057)]' (**arg(7, 1200057))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200058)]' (**arg(8, 1200058))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200059)]' (**arg(9, 1200059))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c7631') '[convertstrid(1200060)]' (**arg(10, 1200060))
return "avg24013"