label avg102018:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
$ update_narrator('c203')
window show
with fade_in
get_char('c203') '[convertstrid(1218667)]' (**arg(1, 1218667))
hide p20
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218668)]' (**arg(2, 1218668))
hide p1
$ update_portrait('sc012_01 5', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218669)]' (**arg(3, 1218669))
hide p20
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218670)]' (**arg(4, 1218670))
hide p1
$ update_portrait('sc012_01 1', 'p20', [mid(-16), light], 6)
get_char('c203') '[convertstrid(1218671)]' (**arg(5, 1218671))
return