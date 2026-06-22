label avg106003:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1219049)]' (**arg(1, 1219049))
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219050)]' (**arg(2, 1219050))
hide p1
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219051)]' (**arg(3, 1219051))
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219052)]' (**arg(4, 1219052))
hide p60
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219053)]' (**arg(5, 1219053))
return