label avg101334(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc005_01 1', 'p13', [mid(-17), light], 6)
$ update_narrator('c133')
window show
with trans
get_char('c133') '[convertstrid(1221041)]' (**arg(1, 1221041))
return "avg101334"