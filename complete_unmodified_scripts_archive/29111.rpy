label avg29111(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 5', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with trans
get_char('c93') '[convertstrid(1218044)]' (**arg(1, 1218044))
return "avg29111"