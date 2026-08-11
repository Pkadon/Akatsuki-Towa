label avg24027(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200109)]' (**arg(1, 1200109))
hide p1
get_char('c9573') '[convertstrid(1200110)]' (**arg(2, 1200110))
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200111)]' (**arg(3, 1200111))
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200112)]' (**arg(4, 1200112))
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200113)]' (**arg(5, 1200113))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200114)]' (**arg(6, 1200114))
hide p1
get_char('c9573') '[convertstrid(1200115)]' (**arg(7, 1200115))
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1200116)]' (**arg(8, 1200116))
return "avg24027"