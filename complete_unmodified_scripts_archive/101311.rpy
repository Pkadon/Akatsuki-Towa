label avg101311:

stop music
scene placeholderbackground
$ update_portrait('sc005_01 5', 'p13', [l(-17), light, flip], 6)
$ update_narrator('c131')
window show
with fade_in
get_char('c131') '[convertstrid(1220979)]' (**arg(1, 1220979))
$ update_portrait('sc005_01 5', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220980)]' (**arg(2, 1220980))
return