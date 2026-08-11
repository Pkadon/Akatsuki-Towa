label avg19022(trans=fade_in):

stop music
scene avg_bg_023
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1216226)]' (**arg(1, 1216226, size=(0.9)))
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1216227)]' (**arg(2, 1216227, size=(0.9)))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1216228)]' (**arg(3, 1216228, size=(0.9)))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1216229)]' (**arg(4, 1216229, size=(0.9)))
return "avg19022"