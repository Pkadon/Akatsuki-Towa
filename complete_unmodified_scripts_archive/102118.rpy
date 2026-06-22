label avg102118:

stop music
scene placeholderbackground
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with fade_in
get_char('c213') '[convertstrid(1218848)]' (**arg(1, 1218848))
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218849)]' (**arg(2, 1218849))
hide p21
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218850)]' (**arg(3, 1218850))
hide p1
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218851)]' (**arg(4, 1218851))
hide p21
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218852)]' (**arg(5, 1218852))
hide p1
$ update_portrait('sc013_01 5', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218853)]' (**arg(6, 1218853))
hide p21
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218854)]' (**arg(7, 1218854))
return