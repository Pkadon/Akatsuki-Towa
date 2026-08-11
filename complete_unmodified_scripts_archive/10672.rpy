label avg10672(trans=fade_in):

$ play_music("ed6324.ogg")
scene avg_bg_041
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1165956)]' (**arg(1, 1165956))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165957)]' (**arg(2, 1165957))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165958)]' (**arg(3, 1165958))
hide p3
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165959)]' (**arg(4, 1165959))
hide p4
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1165960)]' (**arg(5, 1165960))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165961)]' (**arg(6, 1165961))
hide p2
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165962)]' (**arg(7, 1165962))
hide p1304
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1165963)]' (**arg(8, 1165963))
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1165964)]' (**arg(9, 1165964))
$ update_portrait('oc004_01 17', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165965)]' (**arg(10, 1165965))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165966)]' (**arg(11, 1165966))
hide p2
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165967)]' (**arg(12, 1165967))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165968)]' (**arg(13, 1165968))
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165969)]' (**arg(14, 1165969))
hide p1
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165970)]' (**arg(15, 1165970))
hide p1304
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165971)]' (**arg(16, 1165971))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165972)]' (**arg(17, 1165972))
hide p3
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165973)]' (**arg(18, 1165973))
hide p2
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165974)]' (**arg(19, 1165974))
hide p1304
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165975)]' (**arg(20, 1165975))
return "avg10672"