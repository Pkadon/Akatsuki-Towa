label avg10032:

$ play_music("ed7151.ogg")
scene avg_bg_034
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
get_char('c21') '[convertstrid(1002911)]' (**arg(1, 1002911))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002912)]' (**arg(2, 1002912))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002913)]' (**arg(3, 1002913))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002914)]' (**arg(4, 1002914))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002915)]' (**arg(5, 1002915))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002916)]' (**arg(6, 1002916))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002917)]' (**arg(7, 1002917))
hide p3
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002918)]' (**arg(8, 1002918))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002919)]' (**arg(9, 1002919))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002920)]' (**arg(10, 1002920))
hide p1
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002921)]' (**arg(11, 1002921))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002922)]' (**arg(12, 1002922))
hide p4
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1002923)]' (**arg(13, 1002923))
hide p3
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002924)]' (**arg(14, 1002924))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002925)]' (**arg(15, 1002925))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002926)]' (**arg(16, 1002926))
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7071.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1002927)]' (**arg(17, 1002927))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002928)]' (**arg(18, 1002928))
hide p1
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1002929)]' (**arg(19, 1002929))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002930)]' (**arg(20, 1002930))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1002931)]' (**arg(21, 1002931))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002932)]' (**arg(22, 1002932))
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002933)]' (**arg(23, 1002933))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1002934)]' (**arg(24, 1002934))
hide p4
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na08.ogg"
get_char('c11') '[convertstrid(1002935)]' (**arg(25, 1002935))
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7072.ogg"
get_char('c11') '[convertstrid(1002936)]' (**arg(26, 1002936))
scene avg_bg_070
$ update_narrator('c4983')
with fade
get_char('c4983') '[convertstrid(1002937)]' (**arg(27, 1002937))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002938)]' (**arg(28, 1002938))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002939)]' (**arg(29, 1002939))
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002940)]' (**arg(30, 1002940))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c4983') '[convertstrid(1002941)]' (**arg(31, 1002941))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002942)]' (**arg(32, 1002942))
$ play_music("ed7561.ogg")
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c4983') '[convertstrid(1002943)]' (**arg(33, 1002943))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1002944)]' (**arg(34, 1002944, size=(1.2))) with shake
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c43') '[convertstrid(1002945)]' (**arg(35, 1002945))
hide p4
get_char('c4973') '[convertstrid(1002946)]' (**arg(36, 1002946))
hide p2
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro18.ogg"
get_char('c31') '[convertstrid(1002947)]' (**arg(37, 1002947, size=(1.2))) with shake
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
get_char('c4973') '[convertstrid(1002948)]' (**arg(38, 1002948))
get_char('c4973') '[convertstrid(1002949)]' (**arg(39, 1002949))
get_char('c4973') '[convertstrid(1002950)]' (**arg(40, 1002950))
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002951)]' (**arg(41, 1002951))
hide p2
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002952)]' (**arg(42, 1002952))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
get_char('c4973') '[convertstrid(1002953)]' (**arg(43, 1002953))
get_char('c4973') '[convertstrid(1002954)]' (**arg(44, 1002954))
get_char('c4973') '[convertstrid(1002955)]' (**arg(45, 1002955))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1002956)]' (**arg(46, 1002956))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
get_char('c4973') '[convertstrid(1002957)]' (**arg(47, 1002957))
get_char('c4973') '[convertstrid(1002958)]' (**arg(48, 1002958))
get_char('c4973') '[convertstrid(1002959)]' (**arg(49, 1002959))
play sfx2 "other_7073.ogg"
get_char('c4973') '[convertstrid(1002960)]' (**arg(50, 1002960))
scene avg_bg_034
$ update_narrator('c11')
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
with fade
$ update_portrait('oc001_01 9', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1002961)]' (**arg(51, 1002961))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 19', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1002962)]' (**arg(52, 1002962))
hide p1
$ update_portrait('oc002_01 19', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1002963)]' (**arg(53, 1002963))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1002964)]' (**arg(54, 1002964))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002965)]' (**arg(55, 1002965))
hide p4
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1002966)]' (**arg(56, 1002966))
return