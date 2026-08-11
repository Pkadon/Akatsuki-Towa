label avg107109(trans=fade_in):

$ play_music("ed7544.ogg")
scene avg_bg_003
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
get_char('c41') '[convertstrid(1180056)]' (**arg(1, 1180056))
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1180057)]' (**arg(2, 1180057))
$ update_portrait('oc005_01 7', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1180058)]' (**arg(3, 1180058))
hide p5
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1180059)]' (**arg(4, 1180059))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 19', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1180060)]' (**arg(5, 1180060))
hide p1
$ update_portrait('oc004_01 19', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1180061)]' (**arg(6, 1180061))
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1180062)]' (**arg(7, 1180062))
hide p3
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1180063)]' (**arg(8, 1180063))
hide p1304
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1180064)]' (**arg(9, 1180064))
stop music
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1180065)]' (**arg(10, 1180065)) with shake
hide p4
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1180066)]' (**arg(11, 1180066))
hide p2
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1180067)]' (**arg(12, 1180067))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1180068)]' (**arg(13, 1180068))
$ play_music("ed7551.ogg")
scene avg_bg_507
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1180069)]' (**arg(14, 1180069))
get_char('c0') '[convertstrid(1180070)]' (**arg(15, 1180070))
get_char('c0') '[convertstrid(1180071)]' (**arg(16, 1180071))
return "avg107109"