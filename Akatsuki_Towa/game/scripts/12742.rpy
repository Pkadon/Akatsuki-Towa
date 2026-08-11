label avg12742(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_203
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1172916)]' (**arg(1, 1172916))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172917)]' (**arg(2, 1172917))
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172918)]' (**arg(3, 1172918))
$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1172919)]' (**arg(4, 1172919))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172920)]' (**arg(5, 1172920))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172921)]' (**arg(6, 1172921))
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172922)]' (**arg(7, 1172922))
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172923)]' (**arg(8, 1172923))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172924)]' (**arg(9, 1172924))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c31') '[convertstrid(1172925)]' (**arg(10, 1172925))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1172926)]' (**arg(11, 1172926))
return "avg12742"