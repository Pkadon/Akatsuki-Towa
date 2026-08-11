label avg102820(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
$ update_narrator('c283')
window show
with trans
get_char('c283') '[convertstrid(1219770)]' (**arg(1, 1219770))
hide p28
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219771)]' (**arg(2, 1219771))
hide p1
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219772)]' (**arg(3, 1219772))
hide p28
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219773)]' (**arg(4, 1219773))
hide p1
$ update_portrait('sc020_01 1', 'p28', [mid(-10), light], 6)
get_char('c283') '[convertstrid(1219774)]' (**arg(5, 1219774))
hide p28
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219775)]' (**arg(6, 1219775))
return "avg102820"