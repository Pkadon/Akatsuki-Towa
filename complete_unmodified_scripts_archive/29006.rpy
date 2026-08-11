label avg29006(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1216038)]' (**arg(1, 1216038))
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216039)]' (**arg(2, 1216039))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216040)]' (**arg(3, 1216040))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1216041)]' (**arg(4, 1216041))
return "avg29006"