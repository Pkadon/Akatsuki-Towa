label avg24019(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200080)]' (**arg(1, 1200080))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c9851') '[convertstrid(1200081)]' (**arg(2, 1200081))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200082)]' (**arg(3, 1200082))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c9851') '[convertstrid(1200083)]' (**arg(4, 1200083))
get_char('c9851') '[convertstrid(1200084)]' (**arg(5, 1200084))
get_char('c9851') '[convertstrid(1200085)]' (**arg(6, 1200085))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200086)]' (**arg(7, 1200086))
return "avg24019"