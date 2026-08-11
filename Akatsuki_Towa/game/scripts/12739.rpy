label avg12739(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c14401')
window show
with trans
get_char('c14401') '[convertstrid(1172873)]' (**arg(1, 1172873))
get_char('c14401') '[convertstrid(1172874)]' (**arg(2, 1172874))
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172875)]' (**arg(3, 1172875))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172876)]' (**arg(4, 1172876))
return "avg12739"