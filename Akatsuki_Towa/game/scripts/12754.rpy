label avg12754:

$ play_music("ed7544.ogg")
scene avg_bg_003
$ update_portrait('oc005_01 22', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
window show
with fade_in
get_char('c53') '[convertstrid(1174331)]' (**arg(1, 1174331))
$ update_portrait('oc005_01 22', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174332)]' (**arg(2, 1174332))
hide p4
$ update_portrait('st044_01 2', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(1174333)]' (**arg(3, 1174333))
$ update_portrait('st044_01 4', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(1174334)]' (**arg(4, 1174334))
$ update_portrait('st044_01 4', 'p692', [l(10), dark, flip], 5)
$ update_portrait('oc005_01 7', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1174335)]' (**arg(5, 1174335))
$ update_portrait('oc005_01 20', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1174336)]' (**arg(6, 1174336))
hide p692
$ update_portrait('oc005_01 20', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1174337)]' (**arg(7, 1174337))
hide p5
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1174338)]' (**arg(8, 1174338))
scene avg_bg_036
$ update_narrator('c14581')
with fade
get_char('c14581') '[convertstrid(1174339)]' (**arg(9, 1174339)) with shake
play sfx2 "other_7013.ogg"
get_char('c0') '[convertstrid(1174340)]' (**arg(10, 1174340))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174341)]' (**arg(11, 1174341))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174342)]' (**arg(12, 1174342))
hide p3
play sfx2 "other_7080.ogg"
get_char('c14661') '[convertstrid(1174343)]' (**arg(13, 1174343)) with shake
get_char('c14581') '[convertstrid(1174344)]' (**arg(14, 1174344))
get_char('c14581') '[convertstrid(1174345)]' (**arg(15, 1174345))
play sfx2 "other_7013.ogg"
get_char('c14581') '[convertstrid(1174346)]' (**arg(16, 1174346))
hide p1
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174347)]' (**arg(17, 1174347))
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174348)]' (**arg(18, 1174348))
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174349)]' (**arg(19, 1174349))
return