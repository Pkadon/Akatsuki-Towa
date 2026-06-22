label avg101618:

stop music
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
$ update_narrator('c163')
window show
with fade_in
get_char('c163') '[convertstrid(1221567)]' (**arg(1, 1221567))
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221568)]' (**arg(2, 1221568))
hide p16
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221569)]' (**arg(3, 1221569))
hide p1
$ update_portrait('sc008_01 4', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221570)]' (**arg(4, 1221570))
hide p16
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1221571)]' (**arg(5, 1221571))
hide p1
$ update_portrait('sc008_01 1', 'p16', [mid(-18), light], 6)
get_char('c163') '[convertstrid(1221572)]' (**arg(6, 1221572))
return