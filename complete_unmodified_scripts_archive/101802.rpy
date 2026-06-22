label avg101802:

stop music
scene placeholderbackground
$ update_portrait('sc010_01 2', 'p18', [mid(-10), light], 6)
$ update_narrator('c183')
window show
with fade_in
get_char('c183') '[convertstrid(1222153)]' (**arg(1, 1222153))
hide p18
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222154)]' (**arg(2, 1222154))
hide p1
$ update_portrait('sc010_01 1', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222155)]' (**arg(3, 1222155))
hide p18
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222156)]' (**arg(4, 1222156))
hide p1
$ update_portrait('sc010_01 5', 'p18', [mid(-10), light], 6)
get_char('c183') '[convertstrid(1222157)]' (**arg(5, 1222157))
return