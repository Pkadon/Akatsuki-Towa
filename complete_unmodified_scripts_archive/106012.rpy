label avg106012(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc053_01 5', 'p60', [mid(-32), light], 6)
$ update_narrator('c603')
window show
with trans
get_char('c603') '[convertstrid(1219078)]' (**arg(1, 1219078))
return "avg106012"