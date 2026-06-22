label avg24052:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1200221)]' (**arg(1, 1200221))
hide p1
get_char('c7613') '[convertstrid(1200222)]' (**arg(2, 1200222))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200223)]' (**arg(3, 1200223))
return