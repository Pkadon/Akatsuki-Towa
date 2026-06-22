label avg102020:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 3', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with fade_in
get_char('c203') '[convertstrid(1218679)]' (**arg(1, 1218679))
hide p20
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218680)]' (**arg(2, 1218680))
hide p1
$ update_portrait('sc012_01 4', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218681)]' (**arg(3, 1218681))
hide p20
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218682)]' (**arg(4, 1218682))
hide p1
$ update_portrait('sc012_01 3', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218683)]' (**arg(5, 1218683))
return