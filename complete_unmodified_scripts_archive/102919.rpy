label avg102919:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1219942)]' (**arg(1, 1219942))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219943)]' (**arg(2, 1219943))
hide p29
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219944)]' (**arg(3, 1219944))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219945)]' (**arg(4, 1219945))
hide p29
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219946)]' (**arg(5, 1219946))
return