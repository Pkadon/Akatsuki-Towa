label avg102719:

stop music
scene placeholderbackground
$ update_portrait('sc019_01 1', 'p27', [mid(-18), light], 6)
$ update_narrator('c273')
window show
with fade_in
get_char('c273') '[convertstrid(1219485)]' (**arg(1, 1219485))
hide p27
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219486)]' (**arg(2, 1219486))
hide p1
$ update_portrait('sc019_01 4', 'p27', [mid(-18), light], 6)
get_char('c273') '[convertstrid(1219487)]' (**arg(3, 1219487))
hide p27
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219488)]' (**arg(4, 1219488))
hide p1
$ update_portrait('sc019_01 6', 'p27', [mid(-18), light], 6)
get_char('c273') '[convertstrid(1219489)]' (**arg(5, 1219489))
hide p27
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1219490)]' (**arg(6, 1219490))
return