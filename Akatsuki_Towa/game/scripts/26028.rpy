label avg26028(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215684)]' (**arg(1, 1215684))
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215685)]' (**arg(2, 1215685))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215686)]' (**arg(3, 1215686))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215687)]' (**arg(4, 1215687))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215688)]' (**arg(5, 1215688))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215689)]' (**arg(6, 1215689))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215690)]' (**arg(7, 1215690))
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215691)]' (**arg(8, 1215691))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215692)]' (**arg(9, 1215692))
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215693)]' (**arg(10, 1215693))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215694)]' (**arg(11, 1215694))
return "avg26028"