label avg1114:

stop music
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(2102839)]' (**arg(1, 2102839))
$ play_music("ed7123.ogg")
get_char('c0') '[convertstrid(2102840)]' (**arg(2, 2102840))
scene avg_bg_046
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2102841)]' (**arg(3, 2102841))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102842)]' (**arg(4, 2102842))
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102843)]' (**arg(5, 2102843))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102844)]' (**arg(6, 2102844))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102845)]' (**arg(7, 2102845))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st004_01 5', 'p204', [r_exit(4), light], 6)
get_char('c2043') '[convertstrid(2102846)]' (**arg(8, 2102846))
hide p204
$ update_portrait('oc004_01 13', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(2102847)]' (**arg(9, 2102847))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2102848)]' (**arg(10, 2102848))
scene avg_bg_040
$ update_narrator('c2353')
with fade
$ update_portrait('st036_01 1', 'p235', [r_entrance(-17), light], 6)
get_char('c2353') '[convertstrid(2102849)]' (**arg(11, 2102849))
$ update_portrait('st036_01 1', 'p235', [r(-17), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l_entrance(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102850)]' (**arg(12, 2102850))
hide p204
$ update_portrait('oc004_01 13', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102851)]' (**arg(13, 2102851))
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st036_01 1', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(2102852)]' (**arg(14, 2102852))
$ update_portrait('st036_01 1', 'p235', [r(-17), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102853)]' (**arg(15, 2102853))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(2102854)]' (**arg(16, 2102854))
$ update_portrait('st036_01 1', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(2102855)]' (**arg(17, 2102855))
hide p4
$ update_portrait('st036_01 1', 'p235', [r(-17), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102856)]' (**arg(18, 2102856))
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102857)]' (**arg(19, 2102857))
$ update_portrait('st004_01 6', 'p204', [l(4), dark, flip], 5)
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(2102858)]' (**arg(20, 2102858))
hide p204
$ update_portrait('st036_01 5', 'p235', [r(-17), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102859)]' (**arg(21, 2102859))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st036_01 5', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(2102860)]' (**arg(22, 2102860))
hide p4
$ update_portrait('st036_01 5', 'p235', [r(-17), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102861)]' (**arg(23, 2102861))
$ update_portrait('st004_01 6', 'p204', [l(4), dark, flip], 5)
$ update_portrait('st036_01 1', 'p235', [r(-17), light], 6)
get_char('c2353') '[convertstrid(2102862)]' (**arg(24, 2102862))
return