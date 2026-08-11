label avg12376(trans=fade_in):

stop music
scene avg_bg_058
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c21') '[convertstrid(1134077)]' (**arg(1, 1134077))
return "avg12376"