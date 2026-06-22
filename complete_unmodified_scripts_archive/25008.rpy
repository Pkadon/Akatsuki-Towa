label avg25008:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210011)]' (**arg(1, 1210011))
hide p1
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210012)]' (**arg(2, 1210012))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210013)]' (**arg(3, 1210013))
return