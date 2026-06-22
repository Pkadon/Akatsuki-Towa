label avg102003:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 5', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with fade_in
get_char('c203') '[convertstrid(1218632)]' (**arg(1, 1218632))
hide p20
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218633)]' (**arg(2, 1218633))
hide p1
$ update_portrait('sc012_01 2', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218634)]' (**arg(3, 1218634))
hide p20
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218635)]' (**arg(4, 1218635))
hide p1
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218636)]' (**arg(5, 1218636))
hide p20
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218637)]' (**arg(6, 1218637))
return