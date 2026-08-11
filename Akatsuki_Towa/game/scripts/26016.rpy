label avg26016(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215604)]' (**arg(1, 1215604))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215605)]' (**arg(2, 1215605))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215606)]' (**arg(3, 1215606))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215607)]' (**arg(4, 1215607))
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215608)]' (**arg(5, 1215608))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215609)]' (**arg(6, 1215609))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215610)]' (**arg(7, 1215610))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215746)]' (**arg(8, 1215746))
get_char('c0') '[convertstrid(1215611)]' (**arg(9, 1215611))
get_char('c0') '[convertstrid(1215612)]' (**arg(10, 1215612))
get_char('c0') '[convertstrid(1215613)]' (**arg(11, 1215613))
get_char('c0') '[convertstrid(1215614)]' (**arg(12, 1215614))
return "avg26016"