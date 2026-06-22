label avg11:

stop music
scene placeholderbackground
$ update_portrait('sc007_01 5', 'p0', [l(-17), light, flip], 6)
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(12)]' (**arg(1, 12, size=(2.0)))
hide p0
$ update_portrait('sc007_01 6', 'p0', [l(-17), light, flip], 6)
get_char('c0') '[convertstrid(12)]' (**arg(2, 12, size=(2.0)))
hide p0
$ update_portrait('sc005_01 5', 'p0', [l(-17), light], 6)
get_char('c0') '[convertstrid(12)]' (**arg(3, 12, size=(2.0)))
hide p0
$ update_portrait('sc005_01 6', 'p0', [l(-17), light], 6)
get_char('c0') '[convertstrid(12)]' (**arg(4, 12, size=(2.0)))
return