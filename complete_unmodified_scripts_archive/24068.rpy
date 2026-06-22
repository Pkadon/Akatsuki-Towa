label avg24068:

stop music
scene placeholderbackground
$ update_narrator('c7553')
window show
with fade_in
get_char('c7553') '[convertstrid(1200270)]' (**arg(1, 1200270))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200271)]' (**arg(2, 1200271))
hide p2
get_char('c7553') '[convertstrid(1200272)]' (**arg(3, 1200272))
return