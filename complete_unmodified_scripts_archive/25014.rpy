label avg25014:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1210026)]' (**arg(1, 1210026))
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "common_tag_2.ogg"
get_char('c13') '[convertstrid(1210027)]' (**arg(2, 1210027))
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210028)]' (**arg(3, 1210028))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210029)]' (**arg(4, 1210029))
return