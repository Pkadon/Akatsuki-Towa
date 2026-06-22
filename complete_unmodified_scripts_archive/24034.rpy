label avg24034:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1200138)]' (**arg(1, 1200138))
hide p1
get_char('c10153') '[convertstrid(1200139)]' (**arg(2, 1200139))
get_char('c10153') '[convertstrid(1200140)]' (**arg(3, 1200140))
get_char('c7643') '[convertstrid(1200141)]' (**arg(4, 1200141))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200142)]' (**arg(5, 1200142))
return