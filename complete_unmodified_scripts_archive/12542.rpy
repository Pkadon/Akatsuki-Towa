label avg12542:

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1152924)]' (**arg(1, 1152924))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152925)]' (**arg(2, 1152925))
hide p2
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1152926)]' (**arg(3, 1152926))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152927)]' (**arg(4, 1152927))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1152928)]' (**arg(5, 1152928))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152929)]' (**arg(6, 1152929))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152930)]' (**arg(7, 1152930))
hide p3
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1152931)]' (**arg(8, 1152931))
hide p4
get_char('c0') '[convertstrid(1152932)]' (**arg(9, 1152932))
return