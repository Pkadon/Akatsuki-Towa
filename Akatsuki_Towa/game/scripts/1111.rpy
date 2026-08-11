label avg1111(trans=fade_in):

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2102762)]' (**arg(1, 2102762))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102763)]' (**arg(2, 2102763))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102764)]' (**arg(3, 2102764))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st004_01 5', 'p204', [r(4), light], 6)
get_char('c2043') '[convertstrid(2102765)]' (**arg(4, 2102765))
hide p204
get_char('c9773') '[convertstrid(2102766)]' (**arg(5, 2102766))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7013.ogg"
get_char('c41') '[convertstrid(2102767)]' (**arg(6, 2102767))
return "avg1111"