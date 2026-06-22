label avg102702:

stop music
scene placeholderbackground
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
$ update_narrator('c273')
window show
with fade_in
get_char('c273') '[convertstrid(1219440)]' (**arg(1, 1219440))
hide p27
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219441)]' (**arg(2, 1219441))
hide p1
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
get_char('c273') '[convertstrid(1219442)]' (**arg(3, 1219442))
hide p27
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219443)]' (**arg(4, 1219443))
return