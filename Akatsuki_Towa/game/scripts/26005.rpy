label avg26005(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215525)]' (**arg(1, 1215525))
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215526)]' (**arg(2, 1215526))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215527)]' (**arg(3, 1215527))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215528)]' (**arg(4, 1215528))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215529)]' (**arg(5, 1215529))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215530)]' (**arg(6, 1215530))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215531)]' (**arg(7, 1215531))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215532)]' (**arg(8, 1215532))
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215533)]' (**arg(9, 1215533))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215739)]' (**arg(10, 1215739))
get_char('c0') '[convertstrid(1215534)]' (**arg(11, 1215534))
get_char('c0') '[convertstrid(1215535)]' (**arg(12, 1215535))
return "avg26005"