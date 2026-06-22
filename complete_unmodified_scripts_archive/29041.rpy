label avg29041:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1100022)]' (**arg(1, 1100022))
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1100023)]' (**arg(2, 1100023))
return