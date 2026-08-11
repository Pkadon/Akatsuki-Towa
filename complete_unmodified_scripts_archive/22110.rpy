label avg22110(trans=fade_in):

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1128090)]' (**arg(1, 1128090))
hide p1
$ update_portrait('st033_01 3', 'p537', [mid(-7), light], 6)
get_char('c5373') '[convertstrid(1128091)]' (**arg(2, 1128091))
hide p537
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1128092)]' (**arg(3, 1128092))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128093)]' (**arg(4, 1128093))
hide p1
get_char('c0') '[convertstrid(1128094)]' (**arg(5, 1128094))
$ update_portrait('st033_01 4', 'p537', [mid(-7), light], 6)
get_char('c5373') '[convertstrid(1128095)]' (**arg(6, 1128095))
hide p537
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128096)]' (**arg(7, 1128096))
hide p1
get_char('c5383') '[convertstrid(1128097)]' (**arg(8, 1128097))
$ update_portrait('st033_01 3', 'p537', [mid(-7), light], 6)
get_char('c5373') '[convertstrid(1128098)]' (**arg(9, 1128098))
hide p537
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128099)]' (**arg(10, 1128099))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1128100)]' (**arg(11, 1128100))
hide p2
$ update_portrait('oc003_01 2', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128101)]' (**arg(12, 1128101))
hide p3
get_char('c5383') '[convertstrid(1128102)]' (**arg(13, 1128102))
$ update_portrait('st033_01 3', 'p537', [mid(-7), light], 6)
get_char('c5373') '[convertstrid(1128103)]' (**arg(14, 1128103))
hide p537
$ update_portrait('oc003_01 14', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128104)]' (**arg(15, 1128104))
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1128105)]' (**arg(16, 1128105))
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1128106)]' (**arg(17, 1128106))
hide p2
$ update_portrait('oc003_01 14', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128107)]' (**arg(18, 1128107))
$ update_portrait('oc003_01 1', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1128108)]' (**arg(19, 1128108))
hide p3
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128109)]' (**arg(20, 1128109))
return "avg22110"