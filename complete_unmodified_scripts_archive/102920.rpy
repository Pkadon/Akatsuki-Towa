label avg102920:

stop music
scene placeholderbackground
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
$ update_narrator('c293')
window show
with fade_in
get_char('c293') '[convertstrid(1219948)]' (**arg(1, 1219948))
hide p29
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219949)]' (**arg(2, 1219949))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219950)]' (**arg(3, 1219950))
hide p29
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219951)]' (**arg(4, 1219951))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219952)]' (**arg(5, 1219952))
return