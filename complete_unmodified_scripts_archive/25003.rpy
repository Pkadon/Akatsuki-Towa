label avg25003(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7079.ogg"
get_char('c13') '[convertstrid(1210004)]' (**arg(1, 1210004))
return "avg25003"