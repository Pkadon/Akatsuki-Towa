label avg26018(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1215624)]' (**arg(1, 1215624))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215625)]' (**arg(2, 1215625))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215626)]' (**arg(3, 1215626))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1215627)]' (**arg(4, 1215627))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1215628)]' (**arg(5, 1215628))
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215748)]' (**arg(6, 1215748))
get_char('c0') '[convertstrid(1215629)]' (**arg(7, 1215629))
get_char('c0') '[convertstrid(1215630)]' (**arg(8, 1215630))
get_char('c0') '[convertstrid(1215631)]' (**arg(9, 1215631))
get_char('c0') '[convertstrid(1215632)]' (**arg(10, 1215632))
return "avg26018"