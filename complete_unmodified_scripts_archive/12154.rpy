label avg12154(trans=fade_in):

$ play_music("ED6107.ogg")
scene avg_bg_038
$ update_narrator('c9621')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c9621') '[convertstrid(1128381)]' (**arg(1, 1128381))
get_char('c9621') '[convertstrid(1128382)]' (**arg(2, 1128382))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128383)]' (**arg(3, 1128383))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c9621') '[convertstrid(1128384)]' (**arg(4, 1128384))
get_char('c9621') '[convertstrid(1128385)]' (**arg(5, 1128385))
get_char('c9621') '[convertstrid(1128386)]' (**arg(6, 1128386))
get_char('c9621') '[convertstrid(1128387)]' (**arg(7, 1128387))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1128388)]' (**arg(8, 1128388))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128389)]' (**arg(9, 1128389))
hide p2
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128390)]' (**arg(10, 1128390))
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
get_char('c9621') '[convertstrid(1128391)]' (**arg(11, 1128391))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128392)]' (**arg(12, 1128392))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128393)]' (**arg(13, 1128393))
hide p3
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128394)]' (**arg(14, 1128394))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128395)]' (**arg(15, 1128395))
hide p4
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
get_char('c9621') '[convertstrid(1128396)]' (**arg(16, 1128396))
get_char('c9621') '[convertstrid(1128397)]' (**arg(17, 1128397))
play sfx2 "common_quest.ogg"
get_char('c9621') '[convertstrid(1128398)]' (**arg(18, 1128398))
$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7021.ogg"
get_char('c13') '[convertstrid(1128399)]' (**arg(19, 1128399))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128400)]' (**arg(20, 1128400))
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128401)]' (**arg(21, 1128401))
hide p2
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128402)]' (**arg(22, 1128402))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128403)]' (**arg(23, 1128403))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007725)]' (**arg(24, 1007725))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1007726)]' (**arg(25, 1007726))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007727)]' (**arg(26, 1007727))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007728)]' (**arg(27, 1007728))
return "avg12154"