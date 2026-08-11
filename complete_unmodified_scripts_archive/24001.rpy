label avg24001(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c9643')
window show
with trans
get_char('c9643') '[convertstrid(1200000)]' (**arg(1, 1200000))
$ update_portrait('oc001_01 2', 'p9', [mid(-2), light], 6)
get_char('c93') '[convertstrid(1200001)]' (**arg(2, 1200001))
hide p9
get_char('c9643') '[convertstrid(1200002)]' (**arg(3, 1200002))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200003)]' (**arg(4, 1200003))
return "avg24001"