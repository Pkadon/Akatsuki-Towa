label avg103001:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1222399)]' (**arg(1, 1222399))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222400)]' (**arg(2, 1222400))
hide p30
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222401)]' (**arg(3, 1222401))
hide p1
$ update_portrait('sc022_01 4', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222402)]' (**arg(4, 1222402))
hide p30
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222403)]' (**arg(5, 1222403))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222404)]' (**arg(6, 1222404))
return