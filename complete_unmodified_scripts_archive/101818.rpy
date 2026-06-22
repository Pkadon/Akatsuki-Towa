label avg101818:

stop music
scene placeholderbackground
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with fade_in
get_char('c183') '[convertstrid(1222195)]' (**arg(1, 1222195))
hide p18
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222196)]' (**arg(2, 1222196))
hide p1
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222197)]' (**arg(3, 1222197))
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222198)]' (**arg(4, 1222198))
hide p18
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222199)]' (**arg(5, 1222199))
return