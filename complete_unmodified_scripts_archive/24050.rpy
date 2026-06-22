label avg24050:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1200215)]' (**arg(1, 1200215))
hide p1
get_char('c7603') '[convertstrid(1200216)]' (**arg(2, 1200216))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200217)]' (**arg(3, 1200217))
return