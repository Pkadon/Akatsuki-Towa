label avg12636:

$ play_music("ed7203.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1162956)]' (**arg(1, 1162956))
scene avg_bg_070
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
get_char('c41') '[convertstrid(1162957)]' (**arg(2, 1162957))
hide p4
get_char('c13251') '[convertstrid(1162958)]' (**arg(3, 1162958))
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1162959)]' (**arg(4, 1162959))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
get_char('c13251') '[convertstrid(1162960)]' (**arg(5, 1162960))
get_char('c13251') '[convertstrid(1162961)]' (**arg(6, 1162961))
get_char('c13251') '[convertstrid(1162962)]' (**arg(7, 1162962))
get_char('c13251') '[convertstrid(1162963)]' (**arg(8, 1162963))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1162964)]' (**arg(9, 1162964))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1162965)]' (**arg(10, 1162965))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c13251') '[convertstrid(1162966)]' (**arg(11, 1162966))
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1162967)]' (**arg(12, 1162967))
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
get_char('c13251') '[convertstrid(1162968)]' (**arg(13, 1162968))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162969)]' (**arg(14, 1162969))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162970)]' (**arg(15, 1162970))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13251') '[convertstrid(1162971)]' (**arg(16, 1162971))
return