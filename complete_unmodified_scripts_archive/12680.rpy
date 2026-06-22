label avg12680:

$ play_music("ed7203.ogg")
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
get_char('c31') '[convertstrid(1166980)]' (**arg(1, 1166980))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166981)]' (**arg(2, 1166981))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166982)]' (**arg(3, 1166982))
hide p4
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166983)]' (**arg(4, 1166983))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166984)]' (**arg(5, 1166984))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7080.ogg"
get_char('c31') '[convertstrid(1166985)]' (**arg(6, 1166985))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1166986)]' (**arg(7, 1166986))
return