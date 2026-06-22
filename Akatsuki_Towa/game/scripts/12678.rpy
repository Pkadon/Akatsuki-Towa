label avg12678:

$ play_music("ED6105.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1166954)]' (**arg(1, 1166954))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166955)]' (**arg(2, 1166955))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166956)]' (**arg(3, 1166956))
hide p1
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166957)]' (**arg(4, 1166957))
hide p3
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166958)]' (**arg(5, 1166958))
hide p4
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166959)]' (**arg(6, 1166959))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166960)]' (**arg(7, 1166960))
get_char('c13351') '[convertstrid(1166961)]' (**arg(8, 1166961))
get_char('c13351') '[convertstrid(1166962)]' (**arg(9, 1166962))
hide p1
get_char('c0') '[convertstrid(1166963)]' (**arg(10, 1166963))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166964)]' (**arg(11, 1166964))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c13351') '[convertstrid(1166965)]' (**arg(12, 1166965))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166966)]' (**arg(13, 1166966))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c13351') '[convertstrid(1166967)]' (**arg(14, 1166967))
get_char('c13351') '[convertstrid(1166968)]' (**arg(15, 1166968))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166969)]' (**arg(16, 1166969))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166970)]' (**arg(17, 1166970))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166971)]' (**arg(18, 1166971))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166972)]' (**arg(19, 1166972))
return