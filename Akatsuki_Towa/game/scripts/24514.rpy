label avg24514(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1206036)]' (**arg(1, 1206036))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1206037)]' (**arg(2, 1206037))
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1206038)]' (**arg(3, 1206038))
return "avg24514"