label avg102903(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219901)]' (**arg(1, 1219901))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219902)]' (**arg(2, 1219902))
hide p29
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219903)]' (**arg(3, 1219903))
hide p1
$ update_portrait('sc021_01 1', 'p29', [mid(-17), light], 6)
get_char('c293') '[convertstrid(1219904)]' (**arg(4, 1219904))
hide p29
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219905)]' (**arg(5, 1219905))
return "avg102903"