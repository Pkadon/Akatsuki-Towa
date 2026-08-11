label avg12407(trans=fade_in):

$ play_music("ed7100.ogg")
scene avg_bg_023
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1140242)]' (**arg(1, 1140242))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c31') '[convertstrid(1140243)]' (**arg(2, 1140243))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1140244)]' (**arg(3, 1140244))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1140245)]' (**arg(4, 1140245))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140246)]' (**arg(5, 1140246))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140247)]' (**arg(6, 1140247))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140248)]' (**arg(7, 1140248))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1140249)]' (**arg(8, 1140249))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140250)]' (**arg(9, 1140250))
return "avg12407"