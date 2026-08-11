label avg12605(trans=fade_in):

$ play_music("ED6102.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1161236)]' (**arg(1, 1161236))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1161237)]' (**arg(2, 1161237))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
get_char('c12321') '[convertstrid(1161238)]' (**arg(3, 1161238))
get_char('c12321') '[convertstrid(1161239)]' (**arg(4, 1161239))
hide p2
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161240)]' (**arg(5, 1161240))
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161241)]' (**arg(6, 1161241))
hide p3
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161242)]' (**arg(7, 1161242))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161243)]' (**arg(8, 1161243))
hide p4
get_char('c12321') '[convertstrid(1161244)]' (**arg(9, 1161244))
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161245)]' (**arg(10, 1161245))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
get_char('c12321') '[convertstrid(1161246)]' (**arg(11, 1161246))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161247)]' (**arg(12, 1161247))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161248)]' (**arg(13, 1161248))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161249)]' (**arg(14, 1161249))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161250)]' (**arg(15, 1161250))
return "avg12605"