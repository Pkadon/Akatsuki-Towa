label avg106002(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 4', 'p60', [mid(-32), light], 6)
$ update_narrator('c603')
window show
with trans
get_char('c603') '[convertstrid(1219042)]' (**arg(1, 1219042))
hide p60
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219043)]' (**arg(2, 1219043))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219044)]' (**arg(3, 1219044))
hide p1
$ update_portrait('sc053_01 1', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219045)]' (**arg(4, 1219045))
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
get_char('c603') '[convertstrid(1219046)]' (**arg(5, 1219046))
hide p60
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219047)]' (**arg(6, 1219047))
return "avg106002"