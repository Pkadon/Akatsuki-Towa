label avg24024(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c7593')
window show
with trans
get_char('c7593') '[convertstrid(1200102)]' (**arg(1, 1200102))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200103)]' (**arg(2, 1200103))
return "avg24024"