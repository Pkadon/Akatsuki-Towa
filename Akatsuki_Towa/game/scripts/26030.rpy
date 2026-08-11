label avg26030(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215700)]' (**arg(1, 1215700))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215701)]' (**arg(2, 1215701))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215702)]' (**arg(3, 1215702))
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215703)]' (**arg(4, 1215703))
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215752)]' (**arg(5, 1215752))
get_char('c0') '[convertstrid(1215704)]' (**arg(6, 1215704))
get_char('c0') '[convertstrid(1215705)]' (**arg(7, 1215705))
get_char('c0') '[convertstrid(1215706)]' (**arg(8, 1215706))
get_char('c0') '[convertstrid(1215707)]' (**arg(9, 1215707))
return "avg26030"