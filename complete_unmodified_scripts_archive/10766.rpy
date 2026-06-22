label avg10766:

$ play_music("ed6323.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1175209)]' (**arg(1, 1175209))
play sfx2 "other_7080.ogg"
get_char('c0') '[convertstrid(1175210)]' (**arg(2, 1175210))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175211)]' (**arg(3, 1175211))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175212)]' (**arg(4, 1175212))
hide p3
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1175213)]' (**arg(5, 1175213))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1175214)]' (**arg(6, 1175214))
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175215)]' (**arg(7, 1175215))
hide p1
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175216)]' (**arg(8, 1175216))
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175217)]' (**arg(9, 1175217))
hide p3
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1175218)]' (**arg(10, 1175218))
hide p1304
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1175219)]' (**arg(11, 1175219))
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1175220)]' (**arg(12, 1175220))
hide p4
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175221)]' (**arg(13, 1175221))
hide p1
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175222)]' (**arg(14, 1175222))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1175223)]' (**arg(15, 1175223))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175224)]' (**arg(16, 1175224))
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175225)]' (**arg(17, 1175225))
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1175226)]' (**arg(18, 1175226))
hide p1304
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1175227)]' (**arg(19, 1175227))
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1175228)]' (**arg(20, 1175228))
return