label avg10045(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7064.ogg"
get_char('c13') '[convertstrid(1003854)]' (**arg(1, 1003854))
scene avg_bg_070
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1003855)]' (**arg(2, 1003855))
scene avg_bg_014
$ update_narrator('c11')
with fade
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003856)]' (**arg(3, 1003856))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6453') '[convertstrid(1003857)]' (**arg(4, 1003857))
get_char('c5343') '[convertstrid(1003858)]' (**arg(5, 1003858))
get_char('c6453') '[convertstrid(1003859)]' (**arg(6, 1003859))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003860)]' (**arg(7, 1003860))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c5343') '[convertstrid(1003861)]' (**arg(8, 1003861))
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003862)]' (**arg(9, 1003862))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
get_char('c6473') '[convertstrid(1003863)]' (**arg(10, 1003863))
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003864)]' (**arg(11, 1003864))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
get_char('c6473') '[convertstrid(1003865)]' (**arg(12, 1003865))
get_char('c6473') '[convertstrid(1003866)]' (**arg(13, 1003866))
hide p4
get_char('c5341') '[convertstrid(1003867)]' (**arg(14, 1003867))
get_char('c6473') '[convertstrid(1003868)]' (**arg(15, 1003868))
get_char('c6473') '[convertstrid(1003869)]' (**arg(16, 1003869))
get_char('c6451') '[convertstrid(1003870)]' (**arg(17, 1003870))
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1003871)]' (**arg(18, 1003871))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003872)]' (**arg(19, 1003872))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003873)]' (**arg(20, 1003873))
scene avg_bg_014
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1003874)]' (**arg(21, 1003874))
return "avg10045"