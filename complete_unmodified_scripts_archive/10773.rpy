label avg10773(trans=fade_in):

$ play_music("ed7511.ogg")
scene avg_bg_216
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7079.ogg"
get_char('c0') '[convertstrid(1176025)]' (**arg(1, 1176025))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1176026)]' (**arg(2, 1176026))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1176027)]' (**arg(3, 1176027))
hide p1
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1176028)]' (**arg(4, 1176028))
hide p4
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176029)]' (**arg(5, 1176029))
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176030)]' (**arg(6, 1176030))
hide p3
$ update_portrait('st064_01 3', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1176031)]' (**arg(7, 1176031))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176032)]' (**arg(8, 1176032))
$ update_portrait('st064_01 3', 'p1469', [l(-2), light, flip], 6)
get_char('c14691') '[convertstrid(1176033)]' (**arg(9, 1176033))
hide p2
$ update_portrait('st064_01 3', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1176034)]' (**arg(10, 1176034))
hide p1469
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1176035)]' (**arg(11, 1176035))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1176036)]' (**arg(12, 1176036))
hide p4
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1176037)]' (**arg(13, 1176037))
hide p3
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1176038)]' (**arg(14, 1176038))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1176039)]' (**arg(15, 1176039))
return "avg10773"