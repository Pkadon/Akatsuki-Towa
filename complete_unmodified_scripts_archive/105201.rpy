label avg105201(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219236)]' (**arg(1, 1219236))
hide p1
$ update_portrait('sc052_01 1', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219237)]' (**arg(2, 1219237))
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219238)]' (**arg(3, 1219238))
hide p59
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219239)]' (**arg(4, 1219239))
hide p1
$ update_portrait('sc052_01 6', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219240)]' (**arg(5, 1219240))
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219241)]' (**arg(6, 1219241))
hide p59
$ update_portrait('oc001_01 24', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219242)]' (**arg(7, 1219242))
return "avg105201"