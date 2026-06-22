label avg105219:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 1', 'p59', [mid(-25), light], 6)
$ update_narrator('c593')
window show
with fade_in
get_char('c593') '[convertstrid(1219293)]' (**arg(1, 1219293))
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219294)]' (**arg(2, 1219294))
hide p59
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219295)]' (**arg(3, 1219295))
hide p1
$ update_portrait('sc052_01 6', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219296)]' (**arg(4, 1219296))
$ update_portrait('sc052_01 6', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219297)]' (**arg(5, 1219297))
hide p59
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219298)]' (**arg(6, 1219298))
hide p1
$ update_portrait('sc052_01 2', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219299)]' (**arg(7, 1219299))
hide p59
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219300)]' (**arg(8, 1219300))
return