label avg102002:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 3', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with fade_in
get_char('c203') '[convertstrid(1218625)]' (**arg(1, 1218625))
hide p20
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218626)]' (**arg(2, 1218626))
hide p1
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218627)]' (**arg(3, 1218627))
hide p20
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218628)]' (**arg(4, 1218628))
hide p1
$ update_portrait('sc012_01 4', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218629)]' (**arg(5, 1218629))
hide p20
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218630)]' (**arg(6, 1218630))
return