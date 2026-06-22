label avg24017:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200074)]' (**arg(1, 1200074))
hide p2
get_char('c9853') '[convertstrid(1200075)]' (**arg(2, 1200075))
get_char('c9853') '[convertstrid(1200076)]' (**arg(3, 1200076))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200077)]' (**arg(4, 1200077))
return