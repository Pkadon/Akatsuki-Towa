label avg24017(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200074)]' (**arg(1, 1200074))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c9851') '[convertstrid(1200075)]' (**arg(2, 1200075))
get_char('c9851') '[convertstrid(1200076)]' (**arg(3, 1200076))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200077)]' (**arg(4, 1200077))
return "avg24017"