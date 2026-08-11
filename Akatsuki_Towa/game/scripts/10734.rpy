label avg10734(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_072
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
$ update_narrator('c13043')
window show
with trans
get_char('c13043') '[convertstrid(1172536)]' (**arg(1, 1172536))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c13361') '[convertstrid(1172537)]' (**arg(2, 1172537))
get_char('c13361') '[convertstrid(1172538)]' (**arg(3, 1172538))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172539)]' (**arg(4, 1172539))
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172540)]' (**arg(5, 1172540))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c13361') '[convertstrid(1172541)]' (**arg(6, 1172541))
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172542)]' (**arg(7, 1172542))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c13361') '[convertstrid(1172543)]' (**arg(8, 1172543))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172544)]' (**arg(9, 1172544))
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172545)]' (**arg(10, 1172545))
hide p1304
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1172546)]' (**arg(11, 1172546))
get_char('c13361') '[convertstrid(1172547)]' (**arg(12, 1172547))
get_char('c13361') '[convertstrid(1172548)]' (**arg(13, 1172548))
get_char('c5003') '[convertstrid(1172549)]' (**arg(14, 1172549))
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1172550)]' (**arg(15, 1172550))
return "avg10734"