label avg102119(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 3', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218856)]' (**arg(1, 1218856))
hide p21
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218857)]' (**arg(2, 1218857))
hide p1
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218858)]' (**arg(3, 1218858))
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218859)]' (**arg(4, 1218859))
hide p21
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218860)]' (**arg(5, 1218860))
return "avg102119"