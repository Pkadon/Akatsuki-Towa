label avg26021(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215641)]' (**arg(1, 1215641))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215642)]' (**arg(2, 1215642))
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215643)]' (**arg(3, 1215643))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215644)]' (**arg(4, 1215644))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215645)]' (**arg(5, 1215645))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215646)]' (**arg(6, 1215646))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215647)]' (**arg(7, 1215647))
return "avg26021"