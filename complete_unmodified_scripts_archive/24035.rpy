label avg24035:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1200143)]' (**arg(1, 1200143))
hide p2
get_char('c7623') '[convertstrid(1200144)]' (**arg(2, 1200144))
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200145)]' (**arg(3, 1200145))
return