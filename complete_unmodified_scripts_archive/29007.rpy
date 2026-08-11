label avg29007(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1216042)]' (**arg(1, 1216042))
get_char('c0') '[convertstrid(1216043)]' (**arg(2, 1216043))
get_char('c0') '[convertstrid(1216044)]' (**arg(3, 1216044))
get_char('c0') '[convertstrid(1216045)]' (**arg(4, 1216045))
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216046)]' (**arg(5, 1216046))
hide p2
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216047)]' (**arg(6, 1216047))
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216048)]' (**arg(7, 1216048))
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216049)]' (**arg(8, 1216049))
hide p239
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216050)]' (**arg(9, 1216050))
hide p1
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216051)]' (**arg(10, 1216051))
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216052)]' (**arg(11, 1216052))
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216053)]' (**arg(12, 1216053))
hide p239
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216054)]' (**arg(13, 1216054))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216055)]' (**arg(14, 1216055))
hide p1
$ update_portrait('st040_01 1', 'p239', [mid(-19), light], 6)
get_char('c2393') '[convertstrid(1216056)]' (**arg(15, 1216056))
menu:
    extend ""
    '[convertstrid(1216057)]':
        call avg29008
    '[convertstrid(1216058)]':
        call avg29009
return _return