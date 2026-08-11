label avg12516(trans=fade_in):

$ play_music("ed7120.ogg")
scene avg_bg_077
$ update_narrator('c7401')
window show
with trans
get_char('c7401') '[convertstrid(1151099)]' (**arg(1, 1151099))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151100)]' (**arg(2, 1151100))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151101)]' (**arg(3, 1151101))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1151102)]' (**arg(4, 1151102))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151103)]' (**arg(5, 1151103))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151104)]' (**arg(6, 1151104))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c7401') '[convertstrid(1151105)]' (**arg(7, 1151105))
get_char('c10901') '[convertstrid(1151106)]' (**arg(8, 1151106))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151107)]' (**arg(9, 1151107))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c7401') '[convertstrid(1151108)]' (**arg(10, 1151108))
hide p1
get_char('c10903') '[convertstrid(1151109)]' (**arg(11, 1151109))
get_char('c7401') '[convertstrid(1151110)]' (**arg(12, 1151110))
get_char('c11501') '[convertstrid(1151111)]' (**arg(13, 1151111))
get_char('c11501') '[convertstrid(1151112)]' (**arg(14, 1151112))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151113)]' (**arg(15, 1151113))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c11501') '[convertstrid(1151114)]' (**arg(16, 1151114))
hide p2
get_char('c10903') '[convertstrid(1151115)]' (**arg(17, 1151115))
get_char('c11501') '[convertstrid(1151116)]' (**arg(18, 1151116))
get_char('c7403') '[convertstrid(1151117)]' (**arg(19, 1151117))
get_char('c11501') '[convertstrid(1151118)]' (**arg(20, 1151118))
get_char('c11501') '[convertstrid(1151119)]' (**arg(21, 1151119))
get_char('c11501') '[convertstrid(1151120)]' (**arg(22, 1151120))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1151121)]' (**arg(23, 1151121))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151122)]' (**arg(24, 1151122))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c7401') '[convertstrid(1151123)]' (**arg(25, 1151123))
get_char('c10901') '[convertstrid(1151124)]' (**arg(26, 1151124))
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151125)]' (**arg(27, 1151125))
hide p2
get_char('c0') '[convertstrid(1151126)]' (**arg(28, 1151126))
return "avg12516"