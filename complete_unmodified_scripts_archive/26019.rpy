label avg26019(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215633)]' (**arg(1, 1215633))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215634)]' (**arg(2, 1215634))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215635)]' (**arg(3, 1215635))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215636)]' (**arg(4, 1215636))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215637)]' (**arg(5, 1215637))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215638)]' (**arg(6, 1215638))
return "avg26019"