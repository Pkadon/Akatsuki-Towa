label avg12637(trans=fade_in):

$ play_music("ed7203.ogg")
scene avg_bg_070
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1162973)]' (**arg(1, 1162973))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c13251') '[convertstrid(1162974)]' (**arg(2, 1162974))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1162975)]' (**arg(3, 1162975))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1162976)]' (**arg(4, 1162976))
hide p4
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162977)]' (**arg(5, 1162977))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13251') '[convertstrid(1162978)]' (**arg(6, 1162978))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1162979)]' (**arg(7, 1162979))
$ play_music("ed7511.ogg")
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
play sfx2 "other_7079.ogg"
get_char('c13091') '[convertstrid(1162980)]' (**arg(8, 1162980)) with shake
hide p3
get_char('c13253') '[convertstrid(1162981)]' (**arg(9, 1162981))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1162982)]' (**arg(10, 1162982))
return "avg12637"