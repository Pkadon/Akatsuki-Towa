label avg101302(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1220945)]' (**arg(1, 1220945))
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220946)]' (**arg(2, 1220946))
hide p13
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220947)]' (**arg(3, 1220947))
hide p1
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220948)]' (**arg(4, 1220948))
$ update_portrait('sc005_01 4', 'p13', [mid(-17), light], 6)
get_char('c133') '[convertstrid(1220949)]' (**arg(5, 1220949))
hide p13
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1220950)]' (**arg(6, 1220950))
return "avg101302"