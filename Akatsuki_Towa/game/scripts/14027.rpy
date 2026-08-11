label avg14027(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_013
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1202509)]' (**arg(1, 1202509))
get_char('c7471') '[convertstrid(1202564)]' (**arg(2, 1202564))
$ update_portrait('oc002_01 8', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1202565)]' (**arg(3, 1202565))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c7471') '[convertstrid(1202566)]' (**arg(4, 1202566))
get_char('c7471') '[convertstrid(1202567)]' (**arg(5, 1202567))
get_char('c7471') '[convertstrid(1202568)]' (**arg(6, 1202568))
get_char('c7471') '[convertstrid(1202569)]' (**arg(7, 1202569))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202570)]' (**arg(8, 1202570))
hide p2
get_char('c0') '[convertstrid(1202571)]' (**arg(9, 1202571))
play sfx2 "other_7047.ogg"
get_char('c7471') '[convertstrid(1202572)]' (**arg(10, 1202572))
get_char('c7471') '[convertstrid(1202573)]' (**arg(11, 1202573))
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1202574)]' (**arg(12, 1202574))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c7471') '[convertstrid(1202575)]' (**arg(13, 1202575))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202576)]' (**arg(14, 1202576))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c7471') '[convertstrid(1202577)]' (**arg(15, 1202577))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202578)]' (**arg(16, 1202578))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202579)]' (**arg(17, 1202579))
return "avg14027"