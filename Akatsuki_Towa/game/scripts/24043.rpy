label avg24043:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1200172)]' (**arg(1, 1200172))
hide p1
get_char('c6543') '[convertstrid(1200173)]' (**arg(2, 1200173))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200174)]' (**arg(3, 1200174))
hide p1
get_char('c6543') '[convertstrid(1200175)]' (**arg(4, 1200175))
return