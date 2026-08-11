label avg26001(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215501)]' (**arg(1, 1215501))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215502)]' (**arg(2, 1215502))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215503)]' (**arg(3, 1215503))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215504)]' (**arg(4, 1215504))
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215505)]' (**arg(5, 1215505))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215506)]' (**arg(6, 1215506))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215507)]' (**arg(7, 1215507))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215736)]' (**arg(8, 1215736))
get_char('c0') '[convertstrid(1215508)]' (**arg(9, 1215508))
get_char('c0') '[convertstrid(1215509)]' (**arg(10, 1215509))
return "avg26001"