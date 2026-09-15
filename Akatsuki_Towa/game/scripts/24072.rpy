label avg24072(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_074
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200282)]' (**arg(1, 1200282))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 1', 'p1037', [l(2), light, flip], 6)
get_char('c10371') '[convertstrid(1200283)]' (**arg(2, 1200283))
return "avg24072"