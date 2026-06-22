label avg12842:

$ play_music("ed7302.ogg")
scene avg_bg_074
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1186256)]' (**arg(1, 1186256))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1186257)]' (**arg(2, 1186257))
hide p2
hide p1
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1186258)]' (**arg(3, 1186258))
get_char('c15281') '[convertstrid(1186259)]' (**arg(4, 1186259)) with shake
get_char('c15291') '[convertstrid(1186260)]' (**arg(5, 1186260))
get_char('c15291') '[convertstrid(1186261)]' (**arg(6, 1186261))
get_char('c15301') '[convertstrid(1186262)]' (**arg(7, 1186262))
get_char('c15301') '[convertstrid(1186263)]' (**arg(8, 1186263))
get_char('c15291') '[convertstrid(1186264)]' (**arg(9, 1186264))
get_char('c15301') '[convertstrid(1186265)]' (**arg(10, 1186265))
get_char('c15301') '[convertstrid(1186266)]' (**arg(11, 1186266))
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1186267)]' (**arg(12, 1186267))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1186268)]' (**arg(13, 1186268))
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1186269)]' (**arg(14, 1186269))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1186270)]' (**arg(15, 1186270))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1186271)]' (**arg(16, 1186271))
get_char('c0') '[convertstrid(1186272)]' (**arg(17, 1186272))
get_char('c0') '[convertstrid(1186273)]' (**arg(18, 1186273))
return