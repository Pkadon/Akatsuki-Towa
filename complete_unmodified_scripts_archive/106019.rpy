label avg106019:

stop music
scene placeholderbackground
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
$ update_narrator('c603')
window show
with fade_in
get_char('c603') '[convertstrid(1219093)]' (**arg(1, 1219093))
hide p60
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219094)]' (**arg(2, 1219094))
hide p1
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219095)]' (**arg(3, 1219095))
hide p60
$ update_portrait('oc001_01 14', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219096)]' (**arg(4, 1219096))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219097)]' (**arg(5, 1219097))
hide p1
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219098)]' (**arg(6, 1219098))
hide p60
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219099)]' (**arg(7, 1219099))
return