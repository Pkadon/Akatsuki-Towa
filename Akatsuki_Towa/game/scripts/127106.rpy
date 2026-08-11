label avg127106(trans=fade_in):

$ play_music("ed6323.ogg")
scene avg_bg_214
$ update_narrator('c14741')
window show
with trans
get_char('c14741') '[convertstrid(1178605)]' (**arg(1, 1178605))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1178606)]' (**arg(2, 1178606))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c14741') '[convertstrid(1178607)]' (**arg(3, 1178607))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1178608)]' (**arg(4, 1178608))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1178609)]' (**arg(5, 1178609))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1178610)]' (**arg(6, 1178610))
$ play_music("ed7511.ogg")
hide p4
play sfx2 "other_7080.ogg"
get_char('c13091') '[convertstrid(1178611)]' (**arg(7, 1178611)) with shake
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1178612)]' (**arg(8, 1178612))
hide p1
get_char('c0') '[convertstrid(1178613)]' (**arg(9, 1178613))
get_char('c14751') '[convertstrid(1178614)]' (**arg(10, 1178614))
get_char('c14761') '[convertstrid(1178615)]' (**arg(11, 1178615))
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1178616)]' (**arg(12, 1178616))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), l_shake, light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c31') '[convertstrid(1178617)]' (**arg(13, 1178617))
hide p2
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1178618)]' (**arg(14, 1178618))
return "avg127106"