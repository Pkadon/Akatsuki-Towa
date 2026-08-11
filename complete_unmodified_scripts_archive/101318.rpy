label avg101318(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1220990)]' (**arg(1, 1220990))
hide p13
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220991)]' (**arg(2, 1220991))
hide p1
$ update_portrait('sc005_01 4', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220992)]' (**arg(3, 1220992))
hide p13
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220993)]' (**arg(4, 1220993))
hide p1
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220994)]' (**arg(5, 1220994))
hide p13
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220995)]' (**arg(6, 1220995))
return "avg101318"