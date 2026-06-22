label avg24031:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1200125)]' (**arg(1, 1200125))
hide p1
get_char('c10153') '[convertstrid(1200126)]' (**arg(2, 1200126))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200127)]' (**arg(3, 1200127))
return