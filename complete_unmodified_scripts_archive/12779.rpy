label avg12779:

$ play_music("ed7120.ogg")
scene avg_bg_077
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1176264)]' (**arg(1, 1176264))
$ update_portrait('st065_01 1', 'p1468', [l(-6), light, flip], 6)
get_char('c14681') '[convertstrid(1176265)]' (**arg(2, 1176265))
$ update_portrait('st065_01 1', 'p1468', [l(-6), light, flip], 6)
get_char('c14681') '[convertstrid(1176266)]' (**arg(3, 1176266))
$ update_portrait('st065_01 1', 'p1468', [l(-6), dark, flip], 5)
$ update_portrait('st064_01 1', 'p1469', [r(-2), light], 6)
get_char('c14693') '[convertstrid(1176267)]' (**arg(4, 1176267))
hide p1468
$ update_portrait('st064_01 1', 'p1469', [r(-2), dark], 5)
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1176268)]' (**arg(5, 1176268))
hide p1469
$ update_portrait('oc002_01 22', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1176269)]' (**arg(6, 1176269))
hide p2
$ update_portrait('st061_01 5', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1176270)]' (**arg(7, 1176270))
hide p1304
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1176271)]' (**arg(8, 1176271))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1176272)]' (**arg(9, 1176272))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1176273)]' (**arg(10, 1176273))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st064_01 2', 'p1469', [r(-2), l_shake, light], 6)
get_char('c14693') '[convertstrid(1176274)]' (**arg(11, 1176274))
$ update_portrait('st064_01 3', 'p1469', [r(-2), light], 6)
get_char('c14693') '[convertstrid(1176275)]' (**arg(12, 1176275))
hide p3
$ update_portrait('st064_01 3', 'p1469', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1176276)]' (**arg(13, 1176276))
hide p1469
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1176277)]' (**arg(14, 1176277))
return