label avg26017(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215615)]' (**arg(1, 1215615))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215616)]' (**arg(2, 1215616))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215617)]' (**arg(3, 1215617))
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215618)]' (**arg(4, 1215618))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215619)]' (**arg(5, 1215619))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215620)]' (**arg(6, 1215620))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215621)]' (**arg(7, 1215621))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215747)]' (**arg(8, 1215747))
get_char('c0') '[convertstrid(1215622)]' (**arg(9, 1215622))
get_char('c0') '[convertstrid(1215623)]' (**arg(10, 1215623))
return "avg26017"