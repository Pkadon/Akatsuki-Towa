label avg24026(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c9573')
window show
with trans
get_char('c9573') '[convertstrid(1200107)]' (**arg(1, 1200107))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200108)]' (**arg(2, 1200108))
return "avg24026"