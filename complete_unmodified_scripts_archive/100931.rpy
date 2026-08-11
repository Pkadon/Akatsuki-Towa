label avg100931(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with trans
get_char('c93') '[convertstrid(1218102)]' (**arg(1, 1218102))
return "avg100931"