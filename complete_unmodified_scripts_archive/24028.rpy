label avg24028(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
$ update_narrator('c43')
window show
with trans
get_char('c43') '[convertstrid(1200117)]' (**arg(1, 1200117))
hide p4
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1200118)]' (**arg(2, 1200118))
hide p3
$ update_portrait('oc004_01 1', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1200119)]' (**arg(3, 1200119))
return "avg24028"