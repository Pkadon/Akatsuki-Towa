label avg20125(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_030
$ update_narrator('c451')
window show
with trans
$ update_portrait('sc038_01 1', 'p45', [l_entrance(-1), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c451') '[convertstrid(1006453)]' (**arg(1, 1006453))
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1006454)]' (**arg(2, 1006454))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1006455)]' (**arg(3, 1006455))
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006456)]' (**arg(4, 1006456))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006457)]' (**arg(5, 1006457))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 5', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1006458)]' (**arg(6, 1006458))
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1006459)]' (**arg(7, 1006459))
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1006460)]' (**arg(8, 1006460))
$ update_portrait('sc038_01 5', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1006461)]' (**arg(9, 1006461))
$ update_portrait('sc038_01 5', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1006462)]' (**arg(10, 1006462))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006463)]' (**arg(11, 1006463))
hide p45
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006464)]' (**arg(12, 1006464))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006465)]' (**arg(13, 1006465))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006466)]' (**arg(14, 1006466))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(1006467)]' (**arg(15, 1006467))
hide p1
hide p2
$ update_portrait('sc041_01 5', 'p48', [l(-9), light, flip], 6)
$ update_narrator('c481')
with fade
get_char('c481') '[convertstrid(1006468)]' (**arg(16, 1006468))
$ update_portrait('sc041_01 5', 'p48', [l(-9), dark, flip], 5)
$ update_portrait('sc040_01 2', 'p47', [r_entrance(-9), light], 6)
get_char('c473') '[convertstrid(1006469)]' (**arg(17, 1006469))
return "avg20125"