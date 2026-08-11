label avg102902(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219894)]' (**arg(1, 1219894))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219895)]' (**arg(2, 1219895))
$ update_portrait('sc021_01 4', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219896)]' (**arg(3, 1219896))
hide p29
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219897)]' (**arg(4, 1219897))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219898)]' (**arg(5, 1219898))
hide p29
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219899)]' (**arg(6, 1219899))
return "avg102902"