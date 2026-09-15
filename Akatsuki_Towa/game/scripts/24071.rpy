label avg24071(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_074
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200279)]' (**arg(1, 1200279))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 5', 'p1037', [l(2), light, flip], 6)
get_char('c10371') '[convertstrid(1200280)]' (**arg(2, 1200280))
$ update_portrait('st032_01 5', 'p1037', [l(2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200281)]' (**arg(3, 1200281))
return "avg24071"