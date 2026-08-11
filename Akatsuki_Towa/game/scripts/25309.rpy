label avg25309(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c23') '[convertstrid(1211186)]' (**arg(1, 1211186))
return "avg25309"