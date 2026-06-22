label avg102019:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with fade_in
get_char('c203') '[convertstrid(1218673)]' (**arg(1, 1218673))
hide p20
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218674)]' (**arg(2, 1218674))
hide p1
$ update_portrait('sc012_01 4', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218675)]' (**arg(3, 1218675))
$ update_portrait('sc012_01 5', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218676)]' (**arg(4, 1218676))
hide p20
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218677)]' (**arg(5, 1218677))
return