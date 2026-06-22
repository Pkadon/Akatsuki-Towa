label avg105220:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1219302)]' (**arg(1, 1219302))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219303)]' (**arg(2, 1219303))
hide p1
$ update_portrait('sc052_01 1', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219304)]' (**arg(3, 1219304))
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219305)]' (**arg(4, 1219305))
hide p59
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219306)]' (**arg(5, 1219306))
return