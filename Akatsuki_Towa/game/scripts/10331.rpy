label avg10331(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_030
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 8', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7047.ogg"
get_char('c23') '[convertstrid(1130875)]' (**arg(1, 1130875))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130876)]' (**arg(2, 1130876))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc060_01 5', 'p65', [l_entrance(-16), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c651') '[convertstrid(1130877)]' (**arg(3, 1130877))
hide p65
$ update_portrait('sc045_01 1', 'p52', [l(-11), light, flip], 6)
get_char('c521') '[convertstrid(1130878)]' (**arg(4, 1130878))
hide p52
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130882)]' (**arg(5, 1130882))
hide p2
$ update_portrait('sc038_01 1', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li13.ogg"
get_char('c43') '[convertstrid(1130883)]' (**arg(6, 1130883))
hide p45
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1130884)]' (**arg(7, 1130884))
$ update_portrait('sc039_01 2', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc004_01 24', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li08.ogg"
get_char('c43') '[convertstrid(1130885)]' (**arg(8, 1130885))
hide p46
$ update_portrait('oc004_01 24', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c31') '[convertstrid(1130886)]' (**arg(9, 1130886))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r_midback(-5), light], 6)
get_char('c43') '[convertstrid(1130887)]' (**arg(10, 1130887))
stop music
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1130888)]' (**arg(11, 1130888))
get_char('c0') '[convertstrid(1130889)]' (**arg(12, 1130889))
get_char('c0') '[convertstrid(1130890)]' (**arg(13, 1130890))
$ play_music("ed7151.ogg")
scene avg_bg_030
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1130891)]' (**arg(14, 1130891))
$ update_portrait('oc002_01 17', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1130892)]' (**arg(15, 1130892))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130893)]' (**arg(16, 1130893))
hide p2
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130894)]' (**arg(17, 1130894))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130895)]' (**arg(18, 1130895))
hide p4
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130896)]' (**arg(19, 1130896))
hide p3
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130897)]' (**arg(20, 1130897))
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130898)]' (**arg(21, 1130898))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130899)]' (**arg(22, 1130899))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130900)]' (**arg(23, 1130900))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130901)]' (**arg(24, 1130901))
hide p1
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130902)]' (**arg(25, 1130902))
hide p45
$ update_portrait('oc004_01 21', 'p4', [r(-5), dark], 5)
$ update_portrait('sc041_01 4', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130903)]' (**arg(26, 1130903))
hide p4
$ update_portrait('sc041_01 4', 'p48', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130904)]' (**arg(27, 1130904))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130905)]' (**arg(28, 1130905))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc041_01 4', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130906)]' (**arg(29, 1130906))
$ update_portrait('sc041_01 4', 'p48', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1130907)]' (**arg(30, 1130907)) with shake
hide p48
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1130908)]' (**arg(31, 1130908))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130909)]' (**arg(32, 1130909))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc041_01 4', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130910)]' (**arg(33, 1130910))
hide p1
$ update_portrait('sc041_01 4', 'p48', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130911)]' (**arg(34, 1130911))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130912)]' (**arg(35, 1130912))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc041_01 4', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130913)]' (**arg(36, 1130913))
hide p48
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1130914)]' (**arg(37, 1130914))
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130915)]' (**arg(38, 1130915))
hide p1
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130916)]' (**arg(39, 1130916))
hide p47
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc045_01 4', 'p52', [l(-11), light, flip], 6)
get_char('c521') '[convertstrid(1130917)]' (**arg(40, 1130917))
$ update_portrait('sc045_01 4', 'p52', [l(-11), light, flip], 6)
get_char('c521') '[convertstrid(1130918)]' (**arg(41, 1130918))
hide p52
$ update_portrait('sc041_01 4', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130919)]' (**arg(42, 1130919))
$ update_portrait('sc041_01 1', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130920)]' (**arg(43, 1130920))
hide p48
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130921)]' (**arg(44, 1130921))
hide p4
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130922)]' (**arg(45, 1130922))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1130923)]' (**arg(46, 1130923))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c43') '[convertstrid(1130924)]' (**arg(47, 1130924))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130925)]' (**arg(48, 1130925))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130926)]' (**arg(49, 1130926))
hide p1
$ update_portrait('oc004_01 17', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130927)]' (**arg(50, 1130927))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130928)]' (**arg(51, 1130928))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130929)]' (**arg(52, 1130929))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130930)]' (**arg(53, 1130930))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130931)]' (**arg(54, 1130931))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130932)]' (**arg(55, 1130932))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130933)]' (**arg(56, 1130933))
hide p1
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130934)]' (**arg(57, 1130934))
hide p45
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1130935)]' (**arg(58, 1130935))
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1130936)]' (**arg(59, 1130936))
hide p46
$ update_portrait('sc038_01 2', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130937)]' (**arg(60, 1130937))
hide p45
hide p3
get_char('c0') '[convertstrid(1130938)]' (**arg(61, 1130938))
get_char('c0') '[convertstrid(1130939)]' (**arg(62, 1130939))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130940)]' (**arg(63, 1130940))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130941)]' (**arg(64, 1130941))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130942)]' (**arg(65, 1130942))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130943)]' (**arg(66, 1130943))
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130944)]' (**arg(67, 1130944))
hide p45
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc041_01 4', 'p48', [l(-9), light, flip], 6)
get_char('c481') '[convertstrid(1130945)]' (**arg(68, 1130945))
hide p48
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1130946)]' (**arg(69, 1130946))
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1130947)]' (**arg(70, 1130947))
hide p46
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130948)]' (**arg(71, 1130948))
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130949)]' (**arg(72, 1130949))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130950)]' (**arg(73, 1130950))
hide p45
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc060_01 4', 'p65', [l(-16), light, flip], 6)
get_char('c651') '[convertstrid(1130951)]' (**arg(74, 1130951))
hide p2
$ update_portrait('sc060_01 4', 'p65', [l(-16), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130952)]' (**arg(75, 1130952))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130953)]' (**arg(76, 1130953))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130954)]' (**arg(77, 1130954))
hide p65
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130955)]' (**arg(78, 1130955))
hide p4
$ update_portrait('sc040_01 2', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1130956)]' (**arg(79, 1130956))
hide p1
$ update_portrait('sc040_01 2', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130957)]' (**arg(80, 1130957))
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130958)]' (**arg(81, 1130958))
hide p47
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130959)]' (**arg(82, 1130959))
hide p3
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130960)]' (**arg(83, 1130960))
$ update_portrait('oc004_01 14', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130961)]' (**arg(84, 1130961))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130962)]' (**arg(85, 1130962))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130963)]' (**arg(86, 1130963))
$ update_portrait('oc004_01 14', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130964)]' (**arg(87, 1130964))
$ update_portrait('oc004_01 3', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130965)]' (**arg(88, 1130965))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130996)]' (**arg(89, 1130996))
hide p45
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc040_01 3', 'p47', [l(-9), r_shake, light, flip], 6)
get_char('c471') '[convertstrid(1130967)]' (**arg(90, 1130967))
hide p4
$ update_portrait('sc040_01 3', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130968)]' (**arg(91, 1130968))
hide p47
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130969)]' (**arg(92, 1130969))
hide p3
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130970)]' (**arg(93, 1130970))
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130971)]' (**arg(94, 1130971))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130972)]' (**arg(95, 1130972))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130973)]' (**arg(96, 1130973))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130974)]' (**arg(97, 1130974))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130975)]' (**arg(98, 1130975))
hide p1
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130976)]' (**arg(99, 1130976))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc038_01 1', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130977)]' (**arg(100, 1130977))
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130978)]' (**arg(101, 1130978))
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1130979)]' (**arg(102, 1130979))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130980)]' (**arg(103, 1130980))
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130981)]' (**arg(104, 1130981))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130982)]' (**arg(105, 1130982))
hide p45
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc060_01 5', 'p65', [l(-16), light, flip], 6)
get_char('c651') '[convertstrid(1130983)]' (**arg(106, 1130983))
$ update_portrait('sc060_01 1', 'p65', [l(-16), light, flip], 6)
get_char('c651') '[convertstrid(1130984)]' (**arg(107, 1130984))
$ update_portrait('sc060_01 1', 'p65', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130985)]' (**arg(108, 1130985))
hide p65
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130986)]' (**arg(109, 1130986))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130987)]' (**arg(110, 1130987))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130988)]' (**arg(111, 1130988))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130989)]' (**arg(112, 1130989))
hide p3
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1130990)]' (**arg(113, 1130990))
hide p46
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1130991)]' (**arg(114, 1130991))
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1130992)]' (**arg(115, 1130992))
hide p1
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130993)]' (**arg(116, 1130993))
$ update_portrait('oc003_01 18', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130994)]' (**arg(117, 1130994))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130995)]' (**arg(118, 1130995))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130966)]' (**arg(119, 1130966))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130997)]' (**arg(120, 1130997))
hide p47
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc038_01 4', 'p45', [l(-1), light, flip], 6)
get_char('c451') '[convertstrid(1130998)]' (**arg(121, 1130998))
return "avg10331"