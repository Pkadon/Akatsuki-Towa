label avg102720:

stop music
scene placeholderbackground
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
$ update_narrator('c273')
window show
with fade_in
get_char('c273') '[convertstrid(1219492)]' (**arg(1, 1219492))
hide p27
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219493)]' (**arg(2, 1219493))
hide p1
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
get_char('c273') '[convertstrid(1219494)]' (**arg(3, 1219494))
hide p27
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219495)]' (**arg(4, 1219495))
return