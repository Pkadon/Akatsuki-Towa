label avg10524(trans=fade_in):

$ play_music("ED6100.ogg")
scene avg_bg_078
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1152103)]' (**arg(1, 1152103))
get_char('c0') '[convertstrid(1152104)]' (**arg(2, 1152104))
get_char('c0') '[convertstrid(1152105)]' (**arg(3, 1152105))
get_char('c12301') '[convertstrid(1152106)]' (**arg(4, 1152106))
get_char('c12293') '[convertstrid(1152107)]' (**arg(5, 1152107, size=(1.2))) with shake
get_char('c12301') '[convertstrid(1152108)]' (**arg(6, 1152108))
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1152109)]' (**arg(7, 1152109))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152110)]' (**arg(8, 1152110))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12291') '[convertstrid(1152111)]' (**arg(9, 1152111))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152112)]' (**arg(10, 1152112))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12301') '[convertstrid(1152113)]' (**arg(11, 1152113))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152114)]' (**arg(12, 1152114))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
get_char('c12311') '[convertstrid(1152115)]' (**arg(13, 1152115))
hide p4
get_char('c12293') '[convertstrid(1152116)]' (**arg(14, 1152116))
get_char('c12311') '[convertstrid(1152117)]' (**arg(15, 1152117))
get_char('c12293') '[convertstrid(1152118)]' (**arg(16, 1152118))
get_char('c12301') '[convertstrid(1152119)]' (**arg(17, 1152119))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152120)]' (**arg(18, 1152120))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12301') '[convertstrid(1152121)]' (**arg(19, 1152121))
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1152122)]' (**arg(20, 1152122))
hide p4
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152123)]' (**arg(21, 1152123))
return "avg10524"