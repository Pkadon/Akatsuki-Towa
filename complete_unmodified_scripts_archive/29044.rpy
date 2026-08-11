label avg29044(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c13') '[convertstrid(1100031)]' (**arg(1, 1100031))
return "avg29044"