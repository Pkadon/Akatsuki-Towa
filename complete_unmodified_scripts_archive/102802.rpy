label avg102802(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with trans
get_char('c283') '[convertstrid(1219707)]' (**arg(1, 1219707))
hide p28
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219708)]' (**arg(2, 1219708))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219709)]' (**arg(3, 1219709))
hide p1
$ update_portrait('sc020_01 4', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219710)]' (**arg(4, 1219710))
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219711)]' (**arg(5, 1219711))
hide p28
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219712)]' (**arg(6, 1219712))
hide p1
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219713)]' (**arg(7, 1219713))
hide p28
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219714)]' (**arg(8, 1219714))
return "avg102802"