label avg24060(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200248)]' (**arg(1, 1200248))
hide p1
get_char('c7543') '[convertstrid(1200249)]' (**arg(2, 1200249))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200250)]' (**arg(3, 1200250))
return "avg24060"