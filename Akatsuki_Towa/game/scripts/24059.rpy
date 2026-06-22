label avg24059:

stop music
scene placeholderbackground
$ update_narrator('c7583')
window show
with fade_in
get_char('c7583') '[convertstrid(1200243)]' (**arg(1, 1200243))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200244)]' (**arg(2, 1200244))
hide p1
get_char('c7583') '[convertstrid(1200245)]' (**arg(3, 1200245))
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200246)]' (**arg(4, 1200246))
hide p2
get_char('c7583') '[convertstrid(1200247)]' (**arg(5, 1200247))
return