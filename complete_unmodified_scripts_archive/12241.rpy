label avg12241:

$ play_music("ed7102.ogg")
scene avg_bg_022
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1121507)]' (**arg(1, 1121507))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121234)]' (**arg(2, 1121234))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121235)]' (**arg(3, 1121235))
hide p1
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121236)]' (**arg(4, 1121236))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121508)]' (**arg(5, 1121508))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121237)]' (**arg(6, 1121237))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121238)]' (**arg(7, 1121238))
hide p4
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121239)]' (**arg(8, 1121239))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121509)]' (**arg(9, 1121509))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121510)]' (**arg(10, 1121510))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7044.ogg"
get_char('c41') '[convertstrid(1121240)]' (**arg(11, 1121240))
hide p4
hide p1
$ update_narrator('c10073')
with fade
$ update_portrait('st053_01 1', 'p1007', [r_entrance(-12), light], 6)
play sfx2 "other_7045.ogg"
get_char('c10073') '[convertstrid(1121241)]' (**arg(12, 1121241))
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 6)
get_char('c10073') '[convertstrid(1121511)]' (**arg(13, 1121511))
$ update_portrait('st053_01 1', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121242)]' (**arg(14, 1121242))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1121243)]' (**arg(15, 1121243))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 6)
get_char('c10073') '[convertstrid(1121244)]' (**arg(16, 1121244))
hide p4
$ update_portrait('st053_01 1', 'p1007', [r(-12), dark], 5)
get_char('c11041') '[convertstrid(1121245)]' (**arg(17, 1121245))
get_char('c9771') '[convertstrid(1121246)]' (**arg(18, 1121246))
get_char('c11041') '[convertstrid(1121512)]' (**arg(19, 1121512))
hide p1007
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121247)]' (**arg(20, 1121247))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(1121248)]' (**arg(21, 1121248))
$ update_portrait('st053_01 2', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(1121513)]' (**arg(22, 1121513))
$ update_portrait('st053_01 2', 'p1007', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121514)]' (**arg(23, 1121514))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(1121515)]' (**arg(24, 1121515))
hide p1007
get_char('c11041') '[convertstrid(1121586)]' (**arg(25, 1121586))
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121587)]' (**arg(26, 1121587))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c9771') '[convertstrid(1121588)]' (**arg(27, 1121588))
return