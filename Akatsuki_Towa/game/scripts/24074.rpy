label avg24074:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200287)]' (**arg(1, 1200287))
hide p2
$ update_portrait('st032_01 5', 'p1037', [mid(2), light], 6)
get_char('c10373') '[convertstrid(1200288)]' (**arg(2, 1200288))
hide p1037
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200289)]' (**arg(3, 1200289))
return