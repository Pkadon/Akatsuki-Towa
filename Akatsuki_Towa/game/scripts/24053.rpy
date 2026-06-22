label avg24053:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1200224)]' (**arg(1, 1200224))
hide p1
get_char('c7613') '[convertstrid(1200225)]' (**arg(2, 1200225))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200226)]' (**arg(3, 1200226))
return