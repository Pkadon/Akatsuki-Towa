label avg12820(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_201
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1183812)]' (**arg(1, 1183812))
get_char('c25521') '[convertstrid(1183813)]' (**arg(2, 1183813))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183814)]' (**arg(3, 1183814))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1183815)]' (**arg(4, 1183815))
hide p1
$ update_portrait('oc002_01 23', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183816)]' (**arg(5, 1183816))
hide p2
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1183817)]' (**arg(6, 1183817))
hide p3
get_char('c25521') '[convertstrid(1183818)]' (**arg(7, 1183818))
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183819)]' (**arg(8, 1183819))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c25521') '[convertstrid(1183820)]' (**arg(9, 1183820))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183821)]' (**arg(10, 1183821))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
get_char('c25521') '[convertstrid(1183822)]' (**arg(11, 1183822))
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183823)]' (**arg(12, 1183823))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c25531') '[convertstrid(1183824)]' (**arg(13, 1183824))
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1183825)]' (**arg(14, 1183825))
$ update_portrait('oc002_01 22', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183826)]' (**arg(15, 1183826))
hide p2
hide p1304
play sfx2 "other_7013.ogg"
get_char('c0') '[convertstrid(1183827)]' (**arg(16, 1183827))
return "avg12820"