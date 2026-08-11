label avg105902(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1219244)]' (**arg(1, 1219244))
hide p1
$ update_portrait('sc052_01 2', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219245)]' (**arg(2, 1219245))
hide p59
$ update_portrait('oc001_01 23', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219246)]' (**arg(3, 1219246))
hide p1
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
get_char('c593') '[convertstrid(1219247)]' (**arg(4, 1219247))
hide p59
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219248)]' (**arg(5, 1219248))
return "avg105902"