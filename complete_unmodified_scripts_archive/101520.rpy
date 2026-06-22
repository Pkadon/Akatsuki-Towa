label avg101520:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1221313)]' (**arg(1, 1221313))
hide p1
$ update_portrait('sc007_01 1', 'p15', [mid(-17), light], 6)
get_char('c153') '[convertstrid(1221314)]' (**arg(2, 1221314))
$ update_portrait('sc007_01 5', 'p15', [mid(-17), light], 6)
get_char('c153') '[convertstrid(1221315)]' (**arg(3, 1221315))
hide p15
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221316)]' (**arg(4, 1221316))
hide p1
$ update_portrait('sc007_01 6', 'p15', [mid(-17), light], 6)
get_char('c153') '[convertstrid(1221317)]' (**arg(5, 1221317))
return