label avg100109(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218042)]' (**arg(1, 1218042))
return "avg100109"