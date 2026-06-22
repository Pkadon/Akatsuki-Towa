label avg102101:

stop music
scene placeholderbackground
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with fade_in
get_char('c213') '[convertstrid(1218800)]' (**arg(1, 1218800))
hide p21
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218801)]' (**arg(2, 1218801))
hide p1
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218802)]' (**arg(3, 1218802))
hide p21
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218803)]' (**arg(4, 1218803))
hide p1
$ update_portrait('sc013_01 5', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218804)]' (**arg(5, 1218804))
hide p21
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218805)]' (**arg(6, 1218805))
return