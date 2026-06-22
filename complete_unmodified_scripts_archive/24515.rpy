label avg24515:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 13', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1206039)]' (**arg(1, 1206039))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1206040)]' (**arg(2, 1206040))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1206041)]' (**arg(3, 1206041))
return