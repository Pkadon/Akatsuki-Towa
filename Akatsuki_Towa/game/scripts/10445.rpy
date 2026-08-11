label avg10445(trans=fade_in):

$ play_music("ed7544.ogg")
scene avg_bg_062
$ update_narrator('c11163')
$ update_portrait('uc003_04 3', 'p1116', [r(-14), light], 6)
window show
with trans
$ update_portrait('uc003_04 3', 'p1116', [r(-14), r_shake, light], 6)
get_char('c11163') '[convertstrid(1141899)]' (**arg(1, 1141899))
hide p1116
$ update_portrait('uc003_04 4', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141900)]' (**arg(2, 1141900))
hide p1117
$ update_portrait('uc003_04 3', 'p1118', [r_entrance(-14), light], 6)
get_char('c11183') '[convertstrid(1141901)]' (**arg(3, 1141901))
$ update_portrait('uc003_04 3', 'p1118', [r(-14), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1141902)]' (**arg(4, 1141902))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1141903)]' (**arg(5, 1141903))
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1141904)]' (**arg(6, 1141904))
hide p1118
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('uc003_04 4', 'p1116', [r(-14), light], 6)
get_char('c11163') '[convertstrid(1141905)]' (**arg(7, 1141905))
hide p1116
$ update_portrait('uc003_04 1', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141906)]' (**arg(8, 1141906))
hide p1117
$ update_portrait('uc003_04 1', 'p1118', [r_entrance(-14), light], 6)
get_char('c11183') '[convertstrid(1141907)]' (**arg(9, 1141907))
$ update_portrait('uc003_04 1', 'p1118', [r(-14), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch22.ogg"
get_char('c21') '[convertstrid(1141908)]' (**arg(10, 1141908))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1141909)]' (**arg(11, 1141909))
hide p1
hide p1118
$ update_portrait('uc003_04 2', 'p1116', [r(-14), light], 6)
$ update_narrator('c11163')
with fade
get_char('c11163') '[convertstrid(1141910)]' (**arg(12, 1141910))
hide p1116
$ update_portrait('uc003_04 3', 'p1045', [r(-14), light], 6)
$ update_narrator('c10453')
with fade
get_char('c10453') '[convertstrid(1141911)]' (**arg(13, 1141911))
hide p1045
$ update_portrait('uc003_04 3', 'p1046', [r(-14), r_shake, light], 6)
get_char('c10463') '[convertstrid(1141912)]' (**arg(14, 1141912))
$ update_portrait('uc003_04 3', 'p1046', [r(-14), dark], 5)
get_char('c11101') '[convertstrid(1141913)]' (**arg(15, 1141913))
get_char('c11111') '[convertstrid(1141914)]' (**arg(16, 1141914))
get_char('c11101') '[convertstrid(1141915)]' (**arg(17, 1141915))
hide p1046
$ update_narrator('c10543')
with fade
play sfx2 "other_7076.ogg"
get_char('c10543') '[convertstrid(1141916)]' (**arg(18, 1141916))
$ update_portrait('sc071_01 1', 'p73', [l(-20), l_shake, light, flip], 6)
play sfx2 "other_7086.ogg"
get_char('c731') '[convertstrid(1141917)]' (**arg(19, 1141917))
$ update_portrait('sc071_01 4', 'p73', [l(-20), light, flip], 6)
get_char('c731') '[convertstrid(1141918)]' (**arg(20, 1141918))
$ update_portrait('sc071_01 4', 'p73', [l(-20), dark, flip], 5)
play sfx2 "other_7076.ogg"
get_char('c10543') '[convertstrid(1141919)]' (**arg(21, 1141919))
$ update_portrait('uc003_04 2', 'p1045', [r(-14), r_shake, light], 6)
play sfx2 "other_7086.ogg"
get_char('c10453') '[convertstrid(1141920)]' (**arg(22, 1141920))
hide p1045
$ update_portrait('uc003_04 4', 'p1046', [r(-14), r_shake, light], 6)
get_char('c10463') '[convertstrid(1141921)]' (**arg(23, 1141921))
hide p73
hide p1046
$ update_portrait('st029_01 1', 'p610', [l(-28), light, flip], 6)
$ update_narrator('c6101')
with fade
get_char('c6101') '[convertstrid(1141922)]' (**arg(24, 1141922))
$ update_portrait('st029_01 1', 'p610', [l(-28), dark, flip], 5)
$ update_portrait('sc071_01 4', 'p73', [r_entrance(-20), light], 6)
get_char('c733') '[convertstrid(1141923)]' (**arg(25, 1141923))
hide p610
hide p73
$ update_narrator('c2361')
with fade
$ update_portrait('st037_01 4', 'p236', [l_entrance(-10), light, flip], 6)
get_char('c2361') '[convertstrid(1141924)]' (**arg(26, 1141924))
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 5)
get_char('c11123') '[convertstrid(1141925)]' (**arg(27, 1141925)) with shake
hide p236
$ update_narrator('c10263')
with fade
get_char('c10263') '[convertstrid(1141926)]' (**arg(28, 1141926))
$ update_portrait('sc046_01 4', 'p1004', [l_entrance(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1141927)]' (**arg(29, 1141927))
hide p1004
$ update_narrator('c11243')
with fade
$ update_portrait('uc003_04 3', 'p1124', [r_entrance(-14), light], 6)
get_char('c11243') '[convertstrid(1141928)]' (**arg(30, 1141928))
$ update_portrait('uc003_04 3', 'p1124', [r(-14), dark], 5)
$ update_portrait('uc003_04 4', 'p1125', [l_entrance(-14), r_shake, light, flip], 6)
get_char('c11251') '[convertstrid(1141929)]' (**arg(31, 1141929))
hide p1124
$ update_portrait('uc003_04 4', 'p1125', [l(-14), dark, flip], 5)
$ update_portrait('uc003_04 3', 'p1126', [r_entrance(-14), r_shake, light], 6)
get_char('c11263') '[convertstrid(1141930)]' (**arg(32, 1141930))
hide p1125
$ update_portrait('uc003_04 3', 'p1126', [r(-14), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l_entrance(-7), light, flip], 6)
get_char('c551') '[convertstrid(1141931)]' (**arg(33, 1141931))
hide p1126
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('uc003_04 3', 'p1139', [r(-14), r_shake, light], 6)
get_char('c11393') '[convertstrid(1141932)]' (**arg(34, 1141932))
$ update_portrait('uc003_04 3', 'p1139', [r(-14), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
play sfx2 "fight_6022.ogg"
get_char('c551') '[convertstrid(1141933)]' (**arg(35, 1141933)) with shake
hide p1139
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('uc003_04 3', 'p1124', [r(-14), r_shake, light], 6)
play sfx2 "other_7057.ogg"
get_char('c11243') '[convertstrid(1141934)]' (**arg(36, 1141934))
hide p1124
$ update_portrait('uc003_04 3', 'p1125', [r(-14), r_shake, light], 6)
play sfx2 "other_7057.ogg"
get_char('c11253') '[convertstrid(1141935)]' (**arg(37, 1141935))
hide p1125
$ update_portrait('uc003_04 3', 'p1126', [r_exit(-14), light], 6)
play sfx2 "other_7057.ogg"
get_char('c11263') '[convertstrid(1141936)]' (**arg(38, 1141936))
hide p1126
$ update_portrait('sc048_01 4', 'p55', [l(-7), l_shake, light, flip], 6)
get_char('c551') '[convertstrid(1141937)]' (**arg(39, 1141937))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1141938)]' (**arg(40, 1141938))
hide p55
$ update_narrator('c11163')
with fade
$ update_portrait('uc003_04 2', 'p1116', [r_entrance(-14), light], 6)
get_char('c11163') '[convertstrid(1141939)]' (**arg(41, 1141939))
hide p1116
$ update_portrait('uc003_04 4', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141940)]' (**arg(42, 1141940))
hide p1117
$ update_portrait('uc003_04 3', 'p1118', [r_entrance(-14), light], 6)
get_char('c11183') '[convertstrid(1141941)]' (**arg(43, 1141941))
hide p1118
$ update_portrait('uc003_04 3', 'p1116', [r_entrance(-14), light], 6)
get_char('c11163') '[convertstrid(1141942)]' (**arg(44, 1141942))
$ update_portrait('uc003_04 2', 'p1116', [r_entrance(-14), light], 6)
get_char('c11163') '[convertstrid(1141943)]' (**arg(45, 1141943))
$ update_portrait('uc003_04 2', 'p1116', [r(-14), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1141944)]' (**arg(46, 1141944))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1141945)]' (**arg(47, 1141945))
hide p1116
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc003_04 3', 'p1118', [r(-14), r_shake, light], 6)
get_char('c11183') '[convertstrid(1141946)]' (**arg(48, 1141946))
hide p1118
$ update_portrait('uc003_04 4', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141947)]' (**arg(49, 1141947))
hide p1117
$ update_portrait('uc003_04 4', 'p1116', [r_entrance(-14), light], 6)
get_char('c11163') '[convertstrid(1141948)]' (**arg(50, 1141948))
$ update_portrait('uc003_04 3', 'p1116', [r_entrance(-14), light], 6)
get_char('c11163') '[convertstrid(1141949)]' (**arg(51, 1141949))
hide p1116
$ update_portrait('uc003_04 3', 'p1117', [r_entrance(-14), light], 6)
get_char('c11173') '[convertstrid(1141950)]' (**arg(52, 1141950))
hide p1117
$ update_portrait('uc003_04 3', 'p1118', [r_exit(-14), light], 6)
get_char('c11183') '[convertstrid(1141951)]' (**arg(53, 1141951))
hide p1118
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7033.ogg"
get_char('c21') '[convertstrid(1141952)]' (**arg(54, 1141952))
stop music
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1141953)]' (**arg(55, 1141953))
$ play_music("ed7514.ogg")
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141954)]' (**arg(56, 1141954))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1141955)]' (**arg(57, 1141955))
hide p2
hide p1
$ update_narrator('c53')
with fade
$ update_portrait('oc005_01 7', 'p5', [r_entrance(-6), light], 6)
get_char('c53') '[convertstrid(1141956)]' (**arg(58, 1141956))
$ update_portrait('oc005_01 7', 'p5', [r(-6), dark], 5)
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141957)]' (**arg(59, 1141957))
hide p5
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141958)]' (**arg(60, 1141958))
$ update_portrait('oc004_01 19', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1141959)]' (**arg(61, 1141959))
hide p238
hide p4
get_char('c0') '[convertstrid(1141960)]' (**arg(62, 1141960))
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141961)]' (**arg(63, 1141961))
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141962)]' (**arg(64, 1141962))
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141963)]' (**arg(65, 1141963))
$ update_portrait('oc004_01 20', 'p4', [r(-5), dark], 5)
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141964)]' (**arg(66, 1141964))
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141965)]' (**arg(67, 1141965))
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1141966)]' (**arg(68, 1141966))
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141967)]' (**arg(69, 1141967))
hide p238
$ update_portrait('oc004_01 19', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c21') '[convertstrid(1141968)]' (**arg(70, 1141968))
hide p4
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1141969)]' (**arg(71, 1141969))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1141970)]' (**arg(72, 1141970))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141971)]' (**arg(73, 1141971))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 10', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1141972)]' (**arg(74, 1141972))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1141973)]' (**arg(75, 1141973))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro05.ogg"
get_char('c31') '[convertstrid(1141974)]' (**arg(76, 1141974))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 10', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1141975)]' (**arg(77, 1141975))
$ play_music("ed7151.ogg")
hide p3
hide p5
get_char('c0') '[convertstrid(1141976)]' (**arg(78, 1141976))
get_char('c11713') '[convertstrid(1141977)]' (**arg(79, 1141977))
get_char('c11713') '[convertstrid(1141978)]' (**arg(80, 1141978))
$ update_portrait('sc046_01 4', 'p1004', [l(-5), light, flip], 6)
get_char('c10041') '[convertstrid(1141979)]' (**arg(81, 1141979))
hide p1004
$ update_narrator('c11283')
$ update_portrait('uc003_04 2', 'p1128', [r(-14), light], 6)
with fade
$ update_portrait('uc003_04 2', 'p1128', [r(-14), r_shake, light], 6)
get_char('c11283') '[convertstrid(1141980)]' (**arg(82, 1141980))
hide p1128
$ update_portrait('uc003_04 4', 'p1129', [r(-14), light], 6)
get_char('c11293') '[convertstrid(1141981)]' (**arg(83, 1141981))
hide p1129
$ update_portrait('uc003_04 4', 'p1130', [r(-14), light], 6)
get_char('c11303') '[convertstrid(1141982)]' (**arg(84, 1141982))
hide p1130
$ update_portrait('uc003_04 4', 'p1129', [r(-14), light], 6)
get_char('c11293') '[convertstrid(1141983)]' (**arg(85, 1141983))
hide p1129
$ update_portrait('uc003_04 4', 'p1130', [r(-14), light], 6)
get_char('c11303') '[convertstrid(1141984)]' (**arg(86, 1141984))
hide p1130
$ update_narrator('c11313')
with fade
get_char('c11313') '[convertstrid(1141985)]' (**arg(87, 1141985))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1141986)]' (**arg(88, 1141986))
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1141987)]' (**arg(89, 1141987))
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
get_char('c11313') '[convertstrid(1141988)]' (**arg(90, 1141988))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1141989)]' (**arg(91, 1141989))
get_char('c0') '[convertstrid(1141990)]' (**arg(92, 1141990))
get_char('c0') '[convertstrid(1141991)]' (**arg(93, 1141991))
return "avg10445"