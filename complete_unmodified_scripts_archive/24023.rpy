label avg24023(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc005_01 1', 'p5', [mid(-6), light], 6)
$ update_narrator('c53')
window show
with trans
get_char('c53') '[convertstrid(1200097)]' (**arg(1, 1200097))
hide p5
get_char('c7593') '[convertstrid(1200098)]' (**arg(2, 1200098))
$ update_portrait('oc005_01 8', 'p5', [mid(-6), light], 6)
get_char('c53') '[convertstrid(1200099)]' (**arg(3, 1200099))
hide p5
get_char('c7593') '[convertstrid(1200100)]' (**arg(4, 1200100))
$ update_portrait('oc005_01 8', 'p5', [mid(-6), light], 6)
get_char('c53') '[convertstrid(1200101)]' (**arg(5, 1200101))
return "avg24023"