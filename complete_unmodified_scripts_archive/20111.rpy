label avg20111(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1005380)]' (**arg(1, 1005380))
return "avg20111"