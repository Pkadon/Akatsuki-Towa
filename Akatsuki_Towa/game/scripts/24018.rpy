label avg24018(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_027
$ update_narrator('c9851')
window show
with trans
get_char('c9851') '[convertstrid(1200078)]' (**arg(1, 1200078))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200079)]' (**arg(2, 1200079))
return "avg24018"