label avg12738:

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1172861)]' (**arg(1, 1172861))
play sfx2 "other_7014.ogg"
get_char('c0') '[convertstrid(1172862)]' (**arg(2, 1172862))
get_char('c14401') '[convertstrid(1172863)]' (**arg(3, 1172863))
get_char('c14401') '[convertstrid(1172864)]' (**arg(4, 1172864))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1172865)]' (**arg(5, 1172865))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172866)]' (**arg(6, 1172866))
hide p1304
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
get_char('c14401') '[convertstrid(1172867)]' (**arg(7, 1172867))
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172868)]' (**arg(8, 1172868))
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172869)]' (**arg(9, 1172869))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c14401') '[convertstrid(1172870)]' (**arg(10, 1172870))
hide p1
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1172871)]' (**arg(11, 1172871))
return