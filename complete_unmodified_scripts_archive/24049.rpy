label avg24049:

stop music
scene placeholderbackground
$ update_narrator('c7603')
window show
with fade_in
get_char('c7603') '[convertstrid(1200212)]' (**arg(1, 1200212))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200213)]' (**arg(2, 1200213))
hide p1
get_char('c7313') '[convertstrid(1200214)]' (**arg(3, 1200214))
return