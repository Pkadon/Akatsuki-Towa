label avg102120:

stop music
scene placeholderbackground
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with fade_in
get_char('c213') '[convertstrid(1218862)]' (**arg(1, 1218862))
hide p21
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218863)]' (**arg(2, 1218863))
hide p1
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218864)]' (**arg(3, 1218864))
hide p21
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218865)]' (**arg(4, 1218865))
hide p1
$ update_portrait('sc013_01 5', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218866)]' (**arg(5, 1218866))
hide p21
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218867)]' (**arg(6, 1218867))
return