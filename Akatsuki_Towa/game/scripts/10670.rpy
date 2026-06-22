label avg10670:

$ play_music("ed6324.ogg")
scene avg_bg_041
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
$ update_narrator('c13041')
window show
with fade_in
get_char('c13041') '[convertstrid(1165913)]' (**arg(1, 1165913))
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165914)]' (**arg(2, 1165914))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165915)]' (**arg(3, 1165915))
hide p2
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165916)]' (**arg(4, 1165916))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), l_shake, light, flip], 6)
get_char('c13041') '[convertstrid(1165917)]' (**arg(5, 1165917))
hide p3
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165918)]' (**arg(6, 1165918))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165919)]' (**arg(7, 1165919))
hide p4
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165920)]' (**arg(8, 1165920))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165921)]' (**arg(9, 1165921))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165922)]' (**arg(10, 1165922))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165923)]' (**arg(11, 1165923))
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165924)]' (**arg(12, 1165924))
hide p1
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165925)]' (**arg(13, 1165925))
hide p1304
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1165926)]' (**arg(14, 1165926))
hide p3
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165927)]' (**arg(15, 1165927))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165928)]' (**arg(16, 1165928))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165929)]' (**arg(17, 1165929))
hide p2
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165930)]' (**arg(18, 1165930))
hide p1304
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165931)]' (**arg(19, 1165931))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1165932)]' (**arg(20, 1165932))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165933)]' (**arg(21, 1165933))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1165934)]' (**arg(22, 1165934))
return