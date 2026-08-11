label avg12638(trans=fade_in):

$ play_music("ed7203.ogg")
scene avg_bg_070
$ update_portrait('oc002_01 3', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "fight_6019.ogg"
get_char('c23') '[convertstrid(1162984)]' (**arg(1, 1162984))
$ update_portrait('oc002_01 3', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1162985)]' (**arg(2, 1162985))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1162986)]' (**arg(3, 1162986))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c13251') '[convertstrid(1162987)]' (**arg(4, 1162987))
return "avg12638"