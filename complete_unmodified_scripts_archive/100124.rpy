label avg100124(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218086)]' (**arg(1, 1218086))
return "avg100124"