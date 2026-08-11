label avg10667(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1165776)]' (**arg(1, 1165776))
scene avg_bg_035
$ update_narrator('c5001')
with fade
get_char('c5001') '[convertstrid(1165777)]' (**arg(2, 1165777))
$ update_portrait('oc001_01 20', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1165778)]' (**arg(3, 1165778))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165779)]' (**arg(4, 1165779))
hide p1308
get_char('c13161') '[convertstrid(1165780)]' (**arg(5, 1165780))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1165781)]' (**arg(6, 1165781))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165782)]' (**arg(7, 1165782))
hide p1308
get_char('c13161') '[convertstrid(1165783)]' (**arg(8, 1165783))
get_char('c13541') '[convertstrid(1165784)]' (**arg(9, 1165784))
get_char('c13161') '[convertstrid(1165785)]' (**arg(10, 1165785))
get_char('c13551') '[convertstrid(1165786)]' (**arg(11, 1165786))
hide p2
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165787)]' (**arg(12, 1165787))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1165788)]' (**arg(13, 1165788))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165789)]' (**arg(14, 1165789))
hide p1308
get_char('c13161') '[convertstrid(1165790)]' (**arg(15, 1165790))
hide p1
$ update_portrait('oc004_01 16', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1165791)]' (**arg(16, 1165791))
hide p4
$ update_portrait('oc003_01 17', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1165792)]' (**arg(17, 1165792))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165793)]' (**arg(18, 1165793))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1165794)]' (**arg(19, 1165794))
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165795)]' (**arg(20, 1165795))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1165796)]' (**arg(21, 1165796))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165797)]' (**arg(22, 1165797))
hide p3
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1165798)]' (**arg(23, 1165798))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1165799)]' (**arg(24, 1165799))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165800)]' (**arg(25, 1165800))
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165801)]' (**arg(26, 1165801))
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165802)]' (**arg(27, 1165802))
hide p3
$ update_portrait('oc004_01 21', 'p4', [r(-5), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165803)]' (**arg(28, 1165803))
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165804)]' (**arg(29, 1165804))
$ update_portrait('st062_01 4', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
play sfx2 "other_7087.ogg"
get_char('c43') '[convertstrid(1165805)]' (**arg(30, 1165805)) with shake
hide p1308
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165806)]' (**arg(31, 1165806))
hide p2
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165807)]' (**arg(32, 1165807))
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165808)]' (**arg(33, 1165808))
$ update_portrait('st062_01 4', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165809)]' (**arg(34, 1165809))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165810)]' (**arg(35, 1165810))
hide p1308
get_char('c13161') '[convertstrid(1165811)]' (**arg(36, 1165811))
hide p4
get_char('c0') '[convertstrid(1165812)]' (**arg(37, 1165812))
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165813)]' (**arg(38, 1165813))
$ update_portrait('st062_01 4', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165814)]' (**arg(39, 1165814))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165815)]' (**arg(40, 1165815))
hide p1308
get_char('c13571') '[convertstrid(1165816)]' (**arg(41, 1165816))
$ play_music("ed7511.ogg")
get_char('c13581') '[convertstrid(1165817)]' (**arg(42, 1165817))
$ update_portrait('oc002_01 12', 'p2', [l_exit(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165818)]' (**arg(43, 1165818))
hide p2
hide p4
$ update_portrait('oc001_01 12', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(1165819)]' (**arg(44, 1165819))
hide p1
$ update_portrait('st061_01 5', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1165820)]' (**arg(45, 1165820))
hide p1304
get_char('c13571') '[convertstrid(1165821)]' (**arg(46, 1165821))
get_char('c0') '[convertstrid(1165822)]' (**arg(47, 1165822))
get_char('c13591') '[convertstrid(1165823)]' (**arg(48, 1165823)) with shake
get_char('c13601') '[convertstrid(1165824)]' (**arg(49, 1165824))
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165825)]' (**arg(50, 1165825))
$ update_portrait('st062_01 4', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r_entrance(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1165826)]' (**arg(51, 1165826))
hide p1308
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
get_char('c31') '[convertstrid(1165827)]' (**arg(52, 1165827))
hide p3
hide p1
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(1165828)]' (**arg(53, 1165828))
get_char('c13571') '[convertstrid(1165829)]' (**arg(54, 1165829))
play sfx2 "other_7007.ogg"
get_char('c13571') '[convertstrid(1165830)]' (**arg(55, 1165830))
get_char('c0') '[convertstrid(1165831)]' (**arg(56, 1165831))
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1165832)]' (**arg(57, 1165832))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165833)]' (**arg(58, 1165833))
hide p2
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('st062_01 1', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165834)]' (**arg(59, 1165834))
$ play_music("ed7516.ogg")
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165835)]' (**arg(60, 1165835))
$ update_portrait('st062_01 1', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165836)]' (**arg(61, 1165836))
$ update_portrait('st062_01 1', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1165837)]' (**arg(62, 1165837))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165838)]' (**arg(63, 1165838))
hide p4
$ update_portrait('st062_01 4', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1165839)]' (**arg(64, 1165839))
hide p1308
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1165840)]' (**arg(65, 1165840))
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1165841)]' (**arg(66, 1165841))
hide p4
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165842)]' (**arg(67, 1165842))
hide p1304
$ update_portrait('st062_01 4', 'p1308', [l(-16), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1165843)]' (**arg(68, 1165843))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('st062_01 4', 'p1308', [l(-16), light, flip], 6)
get_char('c13081') '[convertstrid(1165844)]' (**arg(69, 1165844))
return "avg10667"