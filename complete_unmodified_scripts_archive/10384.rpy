label avg10384(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_011
$ update_narrator('c10321')
window show
with trans
get_char('c10321') '[convertstrid(1132333)]' (**arg(1, 1132333))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132334)]' (**arg(2, 1132334))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10321') '[convertstrid(1132335)]' (**arg(3, 1132335))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132336)]' (**arg(4, 1132336))
hide p1
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132337)]' (**arg(5, 1132337))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
get_char('c10321') '[convertstrid(1132338)]' (**arg(6, 1132338))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132339)]' (**arg(7, 1132339))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132340)]' (**arg(8, 1132340))
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1132341)]' (**arg(9, 1132341))
$ update_portrait('oc004_01 6', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132342)]' (**arg(10, 1132342))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132343)]' (**arg(11, 1132343))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132344)]' (**arg(12, 1132344))
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132345)]' (**arg(13, 1132345))
hide p2
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
get_char('c10321') '[convertstrid(1132346)]' (**arg(14, 1132346))
get_char('c10321') '[convertstrid(1132347)]' (**arg(15, 1132347))
get_char('c10321') '[convertstrid(1132348)]' (**arg(16, 1132348))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132349)]' (**arg(17, 1132349))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c10321') '[convertstrid(1132350)]' (**arg(18, 1132350))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132351)]' (**arg(19, 1132351))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c10321') '[convertstrid(1132352)]' (**arg(20, 1132352))
return "avg10384"