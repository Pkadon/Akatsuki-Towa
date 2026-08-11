label avg26006(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215536)]' (**arg(1, 1215536))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215537)]' (**arg(2, 1215537))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215538)]' (**arg(3, 1215538))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215539)]' (**arg(4, 1215539))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215540)]' (**arg(5, 1215540))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215541)]' (**arg(6, 1215541))
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215542)]' (**arg(7, 1215542))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215543)]' (**arg(8, 1215543))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215544)]' (**arg(9, 1215544))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215740)]' (**arg(10, 1215740))
get_char('c0') '[convertstrid(1215545)]' (**arg(11, 1215545))
get_char('c0') '[convertstrid(1215546)]' (**arg(12, 1215546))
get_char('c0') '[convertstrid(1215547)]' (**arg(13, 1215547))
return "avg26006"