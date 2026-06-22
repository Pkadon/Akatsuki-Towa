label avg12658:

$ play_music("ED6300.ogg")
scene avg_bg_070
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
get_char('c33') '[convertstrid(1166397)]' (**arg(1, 1166397))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166398)]' (**arg(2, 1166398))
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166399)]' (**arg(3, 1166399))
hide p3
$ update_portrait('oc004_01 17', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166400)]' (**arg(4, 1166400))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166401)]' (**arg(5, 1166401))
hide p1
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166402)]' (**arg(6, 1166402))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166403)]' (**arg(7, 1166403))
$ play_music("ed7511.ogg")
hide p4
play sfx2 "other_7079.ogg"
get_char('c13091') '[convertstrid(1166404)]' (**arg(8, 1166404)) with shake
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166405)]' (**arg(9, 1166405))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c33') '[convertstrid(1166406)]' (**arg(10, 1166406))
return