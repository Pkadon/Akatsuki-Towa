label avg12653(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_036
$ update_narrator('c13041')
window show
with trans
$ update_portrait('st061_01 1', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163257)]' (**arg(1, 1163257))
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163258)]' (**arg(2, 1163258))
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163259)]' (**arg(3, 1163259))
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1163260)]' (**arg(4, 1163260))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163261)]' (**arg(5, 1163261))
hide p4
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1163262)]' (**arg(6, 1163262))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 3', 'p1304', [l(-2), l_shake, light, flip], 6)
get_char('c13041') '[convertstrid(1163263)]' (**arg(7, 1163263))
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1163264)]' (**arg(8, 1163264))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163265)]' (**arg(9, 1163265))
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163266)]' (**arg(10, 1163266))
hide p2
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163267)]' (**arg(11, 1163267))
hide p1304
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1163268)]' (**arg(12, 1163268))
hide p3
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163269)]' (**arg(13, 1163269))
$ update_portrait('st061_01 4', 'p1304', [l(-2), l_shake, light, flip], 6)
get_char('c13041') '[convertstrid(1163270)]' (**arg(14, 1163270))
hide p1
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1163271)]' (**arg(15, 1163271))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163272)]' (**arg(16, 1163272))
hide p4
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163273)]' (**arg(17, 1163273))
hide p1304
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1163274)]' (**arg(18, 1163274))
hide p4
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1163275)]' (**arg(19, 1163275))
hide p1
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1163276)]' (**arg(20, 1163276))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), l_shake, light, flip], 6)
get_char('c13041') '[convertstrid(1163277)]' (**arg(21, 1163277))
hide p2
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1163278)]' (**arg(22, 1163278))
hide p1304
hide p4
get_char('c0') '[convertstrid(1163279)]' (**arg(23, 1163279))
return "avg12653"