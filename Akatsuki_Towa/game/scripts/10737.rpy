label avg10737:

$ play_music("ed7561.ogg")
scene avg_bg_004
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
get_char('c31') '[convertstrid(1172596)]' (**arg(1, 1172596))
$ update_portrait('oc003_01 21', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172597)]' (**arg(2, 1172597))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172598)]' (**arg(3, 1172598))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172599)]' (**arg(4, 1172599))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172600)]' (**arg(5, 1172600))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172601)]' (**arg(6, 1172601))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172602)]' (**arg(7, 1172602))
hide p3
hide p1
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1172603)]' (**arg(8, 1172603))
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172604)]' (**arg(9, 1172604))
$ update_portrait('oc003_01 21', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172605)]' (**arg(10, 1172605))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172606)]' (**arg(11, 1172606))
return