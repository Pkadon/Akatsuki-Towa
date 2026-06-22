label avg12301:

$ play_music("ed9998.ogg")
scene avg_bg_061
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1131025)]' (**arg(1, 1131025))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131026)]' (**arg(2, 1131026))
hide p2
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131027)]' (**arg(3, 1131027))
hide p4
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131028)]' (**arg(4, 1131028))
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1131035)]' (**arg(5, 1131035))
hide p3
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1131036)]' (**arg(6, 1131036))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1131037)]' (**arg(7, 1131037))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1131038)]' (**arg(8, 1131038))
hide p3
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1131039)]' (**arg(9, 1131039))
$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_narrator('c0')
with fade
play sfx2 "other_7021.ogg"
get_char('c0') '[convertstrid(1133001)]' (**arg(10, 1133001))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133002)]' (**arg(11, 1133002))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133003)]' (**arg(12, 1133003))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c561') '[convertstrid(1133004)]' (**arg(13, 1133004))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1133005)]' (**arg(14, 1133005))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133006)]' (**arg(15, 1133006))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133007)]' (**arg(16, 1133007))
hide p1
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1133008)]' (**arg(17, 1133008))
hide p56
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133009)]' (**arg(18, 1133009))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133010)]' (**arg(19, 1133010))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1133011)]' (**arg(20, 1133011))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133012)]' (**arg(21, 1133012))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c21') '[convertstrid(1133013)]' (**arg(22, 1133013))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1133014)]' (**arg(23, 1133014))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c31') '[convertstrid(1133015)]' (**arg(24, 1133015))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133016)]' (**arg(25, 1133016))
hide p3
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133017)]' (**arg(26, 1133017))
hide p1
$ update_portrait('sc049_01 8', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133018)]' (**arg(27, 1133018))
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133019)]' (**arg(28, 1133019))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c43') '[convertstrid(1133020)]' (**arg(29, 1133020))
hide p56
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c21') '[convertstrid(1133021)]' (**arg(30, 1133021))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133022)]' (**arg(31, 1133022))
hide p2
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c31') '[convertstrid(1133023)]' (**arg(32, 1133023, size=(1.2)))
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133024)]' (**arg(33, 1133024))
hide p3
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 9', 'p1', [l(-2), l_shake, light, flip], 6)
play sfxvoice "bcv_oc001_c01_01.ogg"
get_char('c11') '[convertstrid(1133025)]' (**arg(34, 1133025, size=(1.2)))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c43') '[convertstrid(1133026)]' (**arg(35, 1133026))
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133027)]' (**arg(36, 1133027))
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c11') '[convertstrid(1133028)]' (**arg(37, 1133028, size=(1.2)))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 24', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133029)]' (**arg(38, 1133029))
$ update_portrait('oc004_01 24', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133030)]' (**arg(39, 1133030))
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li08.ogg"
get_char('c43') '[convertstrid(1133031)]' (**arg(40, 1133031))
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133032)]' (**arg(41, 1133032))
hide p1
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c10811') '[convertstrid(1133033)]' (**arg(42, 1133033, size=(1.4))) with shake
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133034)]' (**arg(43, 1133034))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133035)]' (**arg(44, 1133035))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133036)]' (**arg(45, 1133036))
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133037)]' (**arg(46, 1133037))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133038)]' (**arg(47, 1133038))
hide p4
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1133039)]' (**arg(48, 1133039))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133040)]' (**arg(49, 1133040))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1133041)]' (**arg(50, 1133041))
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133042)]' (**arg(51, 1133042))
$ play_music("ed7302.ogg")
hide p56
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133043)]' (**arg(52, 1133043))
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133044)]' (**arg(53, 1133044))
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133045)]' (**arg(54, 1133045))
hide p4
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c21') '[convertstrid(1133046)]' (**arg(55, 1133046))
hide p3
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133047)]' (**arg(56, 1133047))
hide p1
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133048)]' (**arg(57, 1133048))
hide p2
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133049)]' (**arg(58, 1133049))
hide p3
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na13.ogg"
get_char('c13') '[convertstrid(1133050)]' (**arg(59, 1133050))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1133051)]' (**arg(60, 1133051))
$ update_portrait('oc002_01 19', 'p2', [l_midback(-3), light, flip], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c21') '[convertstrid(1133052)]' (**arg(61, 1133052))
hide p2
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7042.ogg"
play sfxvoice "avg_vocal_li07.ogg"
get_char('c41') '[convertstrid(1133053)]' (**arg(62, 1133053))
$ play_music("ed7105.ogg")
hide p1
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133054)]' (**arg(63, 1133054))
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133055)]' (**arg(64, 1133055))
hide p4
$ update_portrait('oc002_01 7', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1133056)]' (**arg(65, 1133056))
hide p3
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133057)]' (**arg(66, 1133057))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133058)]' (**arg(67, 1133058))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1133059)]' (**arg(68, 1133059))
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133060)]' (**arg(69, 1133060))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133061)]' (**arg(70, 1133061))
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133062)]' (**arg(71, 1133062))
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133063)]' (**arg(72, 1133063))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133064)]' (**arg(73, 1133064))
hide p3
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1133065)]' (**arg(74, 1133065))
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133066)]' (**arg(75, 1133066))
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1133067)]' (**arg(76, 1133067))
hide p56
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133068)]' (**arg(77, 1133068))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133069)]' (**arg(78, 1133069))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133070)]' (**arg(79, 1133070))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133071)]' (**arg(80, 1133071))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133072)]' (**arg(81, 1133072))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133073)]' (**arg(82, 1133073))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c21') '[convertstrid(1133074)]' (**arg(83, 1133074))
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133075)]' (**arg(84, 1133075))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133076)]' (**arg(85, 1133076))
$ update_portrait('sc049_01 8', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133077)]' (**arg(86, 1133077))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1133078)]' (**arg(87, 1133078))
hide p56
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133079)]' (**arg(88, 1133079))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133080)]' (**arg(89, 1133080))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro12.ogg"
get_char('c33') '[convertstrid(1133081)]' (**arg(90, 1133081))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133082)]' (**arg(91, 1133082))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133083)]' (**arg(92, 1133083))
hide p1
$ update_portrait('oc004_01 17', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133084)]' (**arg(93, 1133084))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133085)]' (**arg(94, 1133085))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133086)]' (**arg(95, 1133086))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1133087)]' (**arg(96, 1133087))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133088)]' (**arg(97, 1133088))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c21') '[convertstrid(1133089)]' (**arg(98, 1133089))
hide p3
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1133090)]' (**arg(99, 1133090))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c21') '[convertstrid(1133091)]' (**arg(100, 1133091))
return