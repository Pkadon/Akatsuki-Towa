label avg12479:

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1144108)]' (**arg(1, 1144108))
get_char('c0') '[convertstrid(1144109)]' (**arg(2, 1144109))
get_char('c0') '[convertstrid(1144110)]' (**arg(3, 1144110))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144111)]' (**arg(4, 1144111))
stop music
$ update_portrait('oc006_01 4', 'p6', [l(-5), dark, flip], 5)
play sfx2 "other_7080.ogg"
get_char('c10543') '[convertstrid(1144112)]' (**arg(5, 1144112))
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144113)]' (**arg(6, 1144113))
$ play_music("ed7511.ogg")
hide p6
get_char('c0') '[convertstrid(1144114)]' (**arg(7, 1144114))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144115)]' (**arg(8, 1144115))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144116)]' (**arg(9, 1144116))
$ update_portrait('oc006_01 4', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144117)]' (**arg(10, 1144117))
return