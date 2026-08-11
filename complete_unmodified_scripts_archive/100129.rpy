label avg100129(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with trans
get_char('c93') '[convertstrid(1218104)]' (**arg(1, 1218104))
return "avg100129"