label avg20115(trans=fade_in):

$ play_music("ed7104.ogg")
scene avg_bg_038
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
get_char('c41') '[convertstrid(1005588)]' (**arg(1, 1005588))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), r_shake, light], 6)
get_char('c153') '[convertstrid(1005589)]' (**arg(2, 1005589))
hide p15
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005590)]' (**arg(3, 1005590))
hide p23
$ update_portrait('oc002_01 9', 'p2', [r(-3), l_shake, light], 6)
get_char('c23') '[convertstrid(1005591)]' (**arg(4, 1005591))
hide p4
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005592)]' (**arg(5, 1005592))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005593)]' (**arg(6, 1005593))
hide p15
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005594)]' (**arg(7, 1005594))
hide p1
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1005595)]' (**arg(8, 1005595))
hide p4
$ update_portrait('sc040_01 2', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005596)]' (**arg(9, 1005596))
hide p47
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005597)]' (**arg(10, 1005597))
hide p46
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005598)]' (**arg(11, 1005598))
hide p1
$ update_portrait('oc002_01 5', 'p2', [l_midback(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005599)]' (**arg(12, 1005599))
hide p2
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1005600)]' (**arg(13, 1005600))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005601)]' (**arg(14, 1005601))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005602)]' (**arg(15, 1005602))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005603)]' (**arg(16, 1005603))
$ update_portrait('oc004_01 3', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1005604)]' (**arg(17, 1005604))
hide p4
$ update_portrait('oc002_01 11', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005605)]' (**arg(18, 1005605))
hide p2
$ update_portrait('oc004_01 12', 'p4', [l_exit(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005606)]' (**arg(19, 1005606))
hide p4
hide p23
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005607)]' (**arg(20, 1005607))
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005608)]' (**arg(21, 1005608))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005609)]' (**arg(22, 1005609))
$ update_portrait('sc007_01 5', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005610)]' (**arg(23, 1005610))
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005611)]' (**arg(24, 1005611))
hide p15
$ update_portrait('sc015_01 5', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(1005612)]' (**arg(25, 1005612))
$ update_portrait('sc015_01 5', 'p23', [r(9), dark], 5)
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005613)]' (**arg(26, 1005613))
return "avg20115"