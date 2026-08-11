label avg20001(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1000019)]' (**arg(1, 1000019))
$ update_portrait('oc001_01 13', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000020)]' (**arg(2, 1000020))
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000021)]' (**arg(3, 1000021))
$ update_portrait('oc001_01 14', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000022)]' (**arg(4, 1000022))
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000023)]' (**arg(5, 1000023))
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000024)]' (**arg(6, 1000024))
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000025)]' (**arg(7, 1000025))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000026)]' (**arg(8, 1000026))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000027)]' (**arg(9, 1000027))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000028)]' (**arg(10, 1000028))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000029)]' (**arg(11, 1000029))
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000030)]' (**arg(12, 1000030))
return "avg20001"