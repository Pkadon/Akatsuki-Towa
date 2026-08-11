label avg29003(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1216018)]' (**arg(1, 1216018))
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1216019)]' (**arg(2, 1216019))
return "avg29003"