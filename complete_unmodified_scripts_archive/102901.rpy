label avg102901(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219888)]' (**arg(1, 1219888))
hide p1
$ update_portrait('sc021_01 4', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219889)]' (**arg(2, 1219889))
hide p29
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219890)]' (**arg(3, 1219890))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219891)]' (**arg(4, 1219891))
hide p29
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219892)]' (**arg(5, 1219892))
return "avg102901"