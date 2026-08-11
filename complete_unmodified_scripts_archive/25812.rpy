label avg25812(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1210067)]' (**arg(1, 1210067))
return "avg25812"