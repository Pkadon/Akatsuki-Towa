label avg26031(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215708)]' (**arg(1, 1215708))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215710)]' (**arg(2, 1215710))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215711)]' (**arg(3, 1215711))
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215712)]' (**arg(4, 1215712))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215713)]' (**arg(5, 1215713))
return "avg26031"