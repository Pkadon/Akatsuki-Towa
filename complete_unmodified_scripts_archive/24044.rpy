label avg24044(trans=fade_in):

stop music
scene placeholderbackground
$ update_narrator('c6543')
window show
with trans
get_char('c6543') '[convertstrid(1200176)]' (**arg(1, 1200176))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1200177)]' (**arg(2, 1200177))
return "avg24044"