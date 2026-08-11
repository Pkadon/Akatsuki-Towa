label avg100122(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218083)]' (**arg(1, 1218083))
return "avg100122"