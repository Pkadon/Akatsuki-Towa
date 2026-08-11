label avg103018(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
$ update_narrator('c303')
window show
with trans
get_char('c303') '[convertstrid(1222451)]' (**arg(1, 1222451))
hide p30
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222452)]' (**arg(2, 1222452))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222453)]' (**arg(3, 1222453))
$ update_portrait('sc022_01 4', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222454)]' (**arg(4, 1222454))
hide p30
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1222455)]' (**arg(5, 1222455))
hide p1
$ update_portrait('sc022_01 1', 'p30', [mid(-9), light], 6)
get_char('c303') '[convertstrid(1222456)]' (**arg(6, 1222456))
return "avg103018"