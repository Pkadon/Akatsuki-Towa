label avg10327:

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_narrator('c11')
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c11') '[convertstrid(1130780)]' (**arg(1, 1130780))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130781)]' (**arg(2, 1130781))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130782)]' (**arg(3, 1130782))
scene avg_bg_074
$ update_narrator('c2343')
with fade
$ update_portrait('st035_01 2', 'p234', [r_entrance(20), light], 6)
play sfx2 "other_7047.ogg"
get_char('c2343') '[convertstrid(1130784)]' (**arg(4, 1130784))
$ play_music("ed7151.ogg")
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130785)]' (**arg(5, 1130785))
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130786)]' (**arg(6, 1130786))
hide p234
get_char('c0') '[convertstrid(1130787)]' (**arg(7, 1130787))
get_char('c0') '[convertstrid(1130788)]' (**arg(8, 1130788))
get_char('c0') '[convertstrid(1130789)]' (**arg(9, 1130789))
get_char('c0') '[convertstrid(1130790)]' (**arg(10, 1130790))
get_char('c0') '[convertstrid(1130791)]' (**arg(11, 1130791))
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130792)]' (**arg(12, 1130792))
$ update_portrait('oc004_01 3', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130793)]' (**arg(13, 1130793))
hide p4
$ update_portrait('oc001_01 3', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 3', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130794)]' (**arg(14, 1130794))
hide p1
$ update_portrait('oc003_01 3', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1130795)]' (**arg(15, 1130795))
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130796)]' (**arg(16, 1130796))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c11') '[convertstrid(1130797)]' (**arg(17, 1130797))
hide p3
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
play sfx2 "other_7004.ogg"
get_char('c2343') '[convertstrid(1130798)]' (**arg(18, 1130798))
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130799)]' (**arg(19, 1130799))
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130800)]' (**arg(20, 1130800))
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130801)]' (**arg(21, 1130801))
$ update_portrait('st035_01 1', 'p234', [r(20), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130802)]' (**arg(22, 1130802))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1130803)]' (**arg(23, 1130803))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130804)]' (**arg(24, 1130804))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130805)]' (**arg(25, 1130805))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st035_01 5', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130806)]' (**arg(26, 1130806))
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130807)]' (**arg(27, 1130807))
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130808)]' (**arg(28, 1130808))
$ update_portrait('st035_01 5', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130809)]' (**arg(29, 1130809))
hide p2
$ update_portrait('st035_01 5', 'p234', [r(20), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130810)]' (**arg(30, 1130810))
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130811)]' (**arg(31, 1130811))
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130812)]' (**arg(32, 1130812))
hide p4
$ update_portrait('st035_01 1', 'p234', [r(20), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130813)]' (**arg(33, 1130813))
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130814)]' (**arg(34, 1130814))
hide p4
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130815)]' (**arg(35, 1130815))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130816)]' (**arg(36, 1130816))
$ update_portrait('st035_01 3', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130817)]' (**arg(37, 1130817))
$ update_portrait('st035_01 4', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130818)]' (**arg(38, 1130818))
$ update_portrait('st035_01 4', 'p234', [r(20), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130819)]' (**arg(39, 1130819))
hide p1
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130820)]' (**arg(40, 1130820))
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st035_01 5', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130821)]' (**arg(41, 1130821))
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130822)]' (**arg(42, 1130822))
hide p4
$ update_portrait('st035_01 1', 'p234', [r(20), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c11') '[convertstrid(1130823)]' (**arg(43, 1130823))
hide p234
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfx2 "other_7074.ogg"
get_char('c33') '[convertstrid(1130824)]' (**arg(44, 1130824))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130826)]' (**arg(45, 1130826))
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130827)]' (**arg(46, 1130827))
hide p3
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130828)]' (**arg(47, 1130828))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130829)]' (**arg(48, 1130829))
hide p4
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfx2 "other_7073.ogg"
get_char('c33') '[convertstrid(1130830)]' (**arg(49, 1130830))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130831)]' (**arg(50, 1130831))
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130832)]' (**arg(51, 1130832))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st035_01 1', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130833)]' (**arg(52, 1130833))
$ update_portrait('st035_01 5', 'p234', [r(20), light], 6)
get_char('c2343') '[convertstrid(1130834)]' (**arg(53, 1130834))
hide p2
$ update_portrait('st035_01 5', 'p234', [r(20), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130835)]' (**arg(54, 1130835))
return