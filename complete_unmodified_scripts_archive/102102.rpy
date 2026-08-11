label avg102102(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc013_01 1', 'p21', [mid(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1218807)]' (**arg(1, 1218807))
hide p21
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218808)]' (**arg(2, 1218808))
hide p1
$ update_portrait('sc013_01 4', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218809)]' (**arg(3, 1218809))
hide p21
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1218810)]' (**arg(4, 1218810))
hide p1
$ update_portrait('sc013_01 5', 'p21', [mid(-12), light], 6)
get_char('c213') '[convertstrid(1218811)]' (**arg(5, 1218811))
return "avg102102"