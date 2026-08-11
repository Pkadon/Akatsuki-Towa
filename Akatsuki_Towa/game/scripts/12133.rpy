label avg12133(trans=fade_in):

$ play_music("ED6104.ogg")
scene avg_bg_038
$ update_narrator('c9591')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c9591') '[convertstrid(1128272)]' (**arg(1, 1128272))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128273)]' (**arg(2, 1128273))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c9591') '[convertstrid(1128274)]' (**arg(3, 1128274))
get_char('c9591') '[convertstrid(1128275)]' (**arg(4, 1128275))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128276)]' (**arg(5, 1128276))
return "avg12133"