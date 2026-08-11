label avg10061(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_035
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1004915)]' (**arg(1, 1004915))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004916)]' (**arg(2, 1004916))
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1004917)]' (**arg(3, 1004917))
hide p2
$ update_portrait('st044_01 1', 'p692', [r(10), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004918)]' (**arg(4, 1004918))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1004919)]' (**arg(5, 1004919))
hide p4
$ update_portrait('st044_01 4', 'p692', [r(10), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004920)]' (**arg(6, 1004920))
hide p692
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st025_01 1', 'p224', [r(-17), light], 6)
get_char('c2243') '[convertstrid(1004921)]' (**arg(7, 1004921))
hide p1
$ update_portrait('st025_01 1', 'p224', [r(-17), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004922)]' (**arg(8, 1004922))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st025_01 5', 'p224', [r(-17), light], 6)
get_char('c2243') '[convertstrid(1004923)]' (**arg(9, 1004923))
hide p2
$ update_portrait('st025_01 5', 'p224', [r(-17), dark], 5)
$ update_portrait('st044_01 5', 'p692', [l(10), light, flip], 6)
get_char('c6921') '[convertstrid(1004924)]' (**arg(10, 1004924))
hide p692
$ update_portrait('sc007_01 1', 'p15', [l_entrance(-17), light, flip], 6)
get_char('c151') '[convertstrid(1004925)]' (**arg(11, 1004925))
hide p224
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('sc040_01 2', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1004926)]' (**arg(12, 1004926))
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1004927)]' (**arg(13, 1004927))
hide p15
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004928)]' (**arg(14, 1004928))
hide p47
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1004929)]' (**arg(15, 1004929))
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1004930)]' (**arg(16, 1004930))
hide p46
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1004931)]' (**arg(17, 1004931))
hide p47
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004932)]' (**arg(18, 1004932))
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004933)]' (**arg(19, 1004933))
hide p15
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('st025_01 2', 'p224', [r(-17), light], 6)
get_char('c2243') '[convertstrid(1004934)]' (**arg(20, 1004934))
$ update_portrait('st025_01 2', 'p224', [r(-17), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004935)]' (**arg(21, 1004935))
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('st025_01 1', 'p224', [r(-17), light], 6)
get_char('c2243') '[convertstrid(1004936)]' (**arg(22, 1004936))
hide p46
$ update_portrait('st025_01 1', 'p224', [r(-17), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004937)]' (**arg(23, 1004937))
hide p224
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004938)]' (**arg(24, 1004938))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7075.ogg"
get_char('c21') '[convertstrid(1004939)]' (**arg(25, 1004939))
hide p2
hide p1
get_char('c0') '[convertstrid(1004940)]' (**arg(26, 1004940))
$ update_portrait('st044_01 4', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1004941)]' (**arg(27, 1004941))
$ update_portrait('st044_01 4', 'p692', [r(10), dark], 5)
$ update_portrait('sc007_01 5', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1004942)]' (**arg(28, 1004942))
$ update_portrait('sc007_01 5', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('st044_01 5', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1004943)]' (**arg(29, 1004943))
$ update_portrait('st044_01 1', 'p692', [r(10), light], 6)
get_char('c6923') '[convertstrid(1004944)]' (**arg(30, 1004944))
hide p15
$ update_portrait('st044_01 1', 'p692', [r(10), dark], 5)
$ update_portrait('st025_01 1', 'p224', [l(-17), light, flip], 6)
get_char('c2241') '[convertstrid(1004945)]' (**arg(31, 1004945))
hide p224
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004946)]' (**arg(32, 1004946))
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1004947)]' (**arg(33, 1004947))
hide p692
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004948)]' (**arg(34, 1004948))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004949)]' (**arg(35, 1004949))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004950)]' (**arg(36, 1004950))
hide p46
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004951)]' (**arg(37, 1004951))
hide p4
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004952)]' (**arg(38, 1004952))
return "avg10061"