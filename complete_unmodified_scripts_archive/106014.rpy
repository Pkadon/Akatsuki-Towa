label avg106014(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
$ update_narrator('c603')
window show
with trans
get_char('c603') '[convertstrid(1219080)]' (**arg(1, 1219080))
return "avg106014"