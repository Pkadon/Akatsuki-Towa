label avg10401:

$ play_music("ed7162.ogg")
scene avg_bg_065
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1140002)]' (**arg(1, 1140002))
get_char('c0') '[convertstrid(1140003)]' (**arg(2, 1140003))
get_char('c0') '[convertstrid(1140004)]' (**arg(3, 1140004))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfx2 "other_7064.ogg"
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1140005)]' (**arg(4, 1140005))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 1', 'p231', [l_entrance(2), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c2311') '[convertstrid(1140006)]' (**arg(5, 1140006))
$ update_portrait('st032_01 1', 'p231', [l(2), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140007)]' (**arg(6, 1140007))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140008)]' (**arg(7, 1140008))
hide p231
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1140009)]' (**arg(8, 1140009))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140010)]' (**arg(9, 1140010))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1140011)]' (**arg(10, 1140011))
hide p3
$ update_portrait('oc004_01 1', 'p1101', [l_entrance(-5), light, flip], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c11011') '[convertstrid(1140012)]' (**arg(11, 1140012))
$ update_portrait('oc004_01 1', 'p1101', [l(-5), light, flip], 6)
get_char('c11011') '[convertstrid(1140013)]' (**arg(12, 1140013))
$ update_portrait('oc004_01 5', 'p1101', [l(-5), light, flip], 6)
get_char('c11011') '[convertstrid(1140014)]' (**arg(13, 1140014))
$ update_portrait('oc004_01 5', 'p1101', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140015)]' (**arg(14, 1140015))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140016)]' (**arg(15, 1140016))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 13', 'p1101', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c11011') '[convertstrid(1140017)]' (**arg(16, 1140017))
hide p1101
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c31') '[convertstrid(1140018)]' (**arg(17, 1140018))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140019)]' (**arg(18, 1140019))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140020)]' (**arg(19, 1140020))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1140021)]' (**arg(20, 1140021))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140022)]' (**arg(21, 1140022))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140023)]' (**arg(22, 1140023))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140024)]' (**arg(23, 1140024))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p1101', [l(-5), light, flip], 6)
get_char('c11011') '[convertstrid(1140025)]' (**arg(24, 1140025))
hide p1
$ update_portrait('oc004_01 9', 'p1101', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c23') '[convertstrid(1140026)]' (**arg(25, 1140026))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140027)]' (**arg(26, 1140027))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 13', 'p1101', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c11011') '[convertstrid(1140028)]' (**arg(27, 1140028))
hide p1101
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140029)]' (**arg(28, 1140029))
hide p231
hide p2
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
$ update_narrator('c2381')
with fade
get_char('c2381') '[convertstrid(1140030)]' (**arg(29, 1140030))
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140031)]' (**arg(30, 1140031))
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('sc048_01 1', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1140032)]' (**arg(31, 1140032))
hide p55
$ update_portrait('st040_01 1', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1140033)]' (**arg(32, 1140033))
$ update_portrait('st040_01 5', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1140034)]' (**arg(33, 1140034))
hide p239
$ update_portrait('oc001_01 24', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140035)]' (**arg(34, 1140035))
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140036)]' (**arg(35, 1140036))
hide p238
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('st038_01 1', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140037)]' (**arg(36, 1140037))
$ update_portrait('st038_01 1', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140038)]' (**arg(37, 1140038))
$ update_portrait('st038_01 5', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140039)]' (**arg(38, 1140039))
hide p2
$ update_portrait('st038_01 5', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('oc004_01 18', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140040)]' (**arg(39, 1140040))
hide p1101
$ update_portrait('sc048_01 4', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1140041)]' (**arg(40, 1140041))
$ update_portrait('sc048_01 4', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1140042)]' (**arg(41, 1140042))
$ update_portrait('sc048_01 4', 'p55', [r(-7), dark], 5)
$ update_portrait('st038_01 1', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140043)]' (**arg(42, 1140043))
$ update_portrait('st038_01 1', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140044)]' (**arg(43, 1140044))
$ update_portrait('st038_01 1', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140045)]' (**arg(44, 1140045))
$ update_portrait('st038_01 1', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('sc048_01 4', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1140046)]' (**arg(45, 1140046))
$ update_portrait('sc048_01 4', 'p55', [r(-7), dark], 5)
$ update_portrait('st038_01 4', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140047)]' (**arg(46, 1140047))
$ update_portrait('st038_01 4', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140048)]' (**arg(47, 1140048))
hide p55
$ update_portrait('st038_01 4', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c11013') '[convertstrid(1140049)]' (**arg(48, 1140049))
$ update_portrait('oc004_01 11', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140050)]' (**arg(49, 1140050))
$ update_portrait('oc004_01 11', 'p1101', [r(-5), dark], 5)
$ update_portrait('st038_01 4', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140051)]' (**arg(50, 1140051))
$ update_portrait('st038_01 2', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140052)]' (**arg(51, 1140052))
hide p237
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140053)]' (**arg(52, 1140053))
hide p1101
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03_b.ogg"
get_char('c13') '[convertstrid(1140054)]' (**arg(53, 1140054))
hide p238
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c21') '[convertstrid(1140055)]' (**arg(54, 1140055))
hide p2
hide p1
$ update_portrait('st032_01 1', 'p231', [r(2), light], 6)
$ update_narrator('c2313')
with fade
get_char('c2313') '[convertstrid(1140056)]' (**arg(55, 1140056))
$ update_portrait('st032_01 1', 'p231', [r(2), light], 6)
get_char('c2313') '[convertstrid(1140057)]' (**arg(56, 1140057))
$ update_portrait('st032_01 1', 'p231', [r(2), dark], 5)
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140058)]' (**arg(57, 1140058))
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('st032_01 4', 'p231', [r(2), light], 6)
get_char('c2313') '[convertstrid(1140059)]' (**arg(58, 1140059))
$ update_portrait('st032_01 4', 'p231', [r(2), dark], 5)
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140060)]' (**arg(59, 1140060))
hide p231
$ update_portrait('st039_01 2', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('sc048_01 5', 'p55', [r(-7), light], 6)
get_char('c553') '[convertstrid(1140061)]' (**arg(60, 1140061))
hide p55
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140062)]' (**arg(61, 1140062))
hide p1
$ update_portrait('oc004_01 1', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140063)]' (**arg(62, 1140063))
$ update_portrait('oc004_01 1', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140064)]' (**arg(63, 1140064))
$ update_portrait('oc004_01 1', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li03.ogg"
get_char('c11013') '[convertstrid(1140065)]' (**arg(64, 1140065))
hide p238
$ update_portrait('oc004_01 1', 'p1101', [r(-5), dark], 5)
$ update_portrait('sc048_01 4', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140066)]' (**arg(65, 1140066))
hide p1101
$ update_portrait('sc048_01 4', 'p55', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1140067)]' (**arg(66, 1140067))
hide p1
$ update_portrait('oc004_01 10', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140068)]' (**arg(67, 1140068))
hide p55
$ update_portrait('oc004_01 10', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140069)]' (**arg(68, 1140069))
$ update_portrait('st039_01 1', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140070)]' (**arg(69, 1140070))
$ update_portrait('oc004_01 8', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c11013') '[convertstrid(1140071)]' (**arg(70, 1140071))
hide p1101
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1140072)]' (**arg(71, 1140072))
hide p238
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1140073)]' (**arg(72, 1140073))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1140074)]' (**arg(73, 1140074))
hide p3
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140075)]' (**arg(74, 1140075))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140076)]' (**arg(75, 1140076))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140077)]' (**arg(76, 1140077))
hide p1
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c11013') '[convertstrid(1140078)]' (**arg(77, 1140078))
$ update_portrait('oc004_01 7', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140079)]' (**arg(78, 1140079))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140080)]' (**arg(79, 1140080))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140081)]' (**arg(80, 1140081))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140082)]' (**arg(81, 1140082))
$ update_portrait('oc004_01 7', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140083)]' (**arg(82, 1140083))
hide p1101
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140084)]' (**arg(83, 1140084))
hide p238
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140085)]' (**arg(84, 1140085))
hide p2
$ update_portrait('st032_01 1', 'p231', [l(2), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140086)]' (**arg(85, 1140086))
hide p231
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140087)]' (**arg(86, 1140087))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140088)]' (**arg(87, 1140088))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140089)]' (**arg(88, 1140089))
hide p1
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c11013') '[convertstrid(1140090)]' (**arg(89, 1140090))
hide p238
$ update_portrait('oc004_01 21', 'p1101', [r(-5), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140091)]' (**arg(90, 1140091))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140092)]' (**arg(91, 1140092))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140093)]' (**arg(92, 1140093))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140094)]' (**arg(93, 1140094))
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
get_char('c551') '[convertstrid(1140095)]' (**arg(94, 1140095))
hide p55
$ update_portrait('st038_01 4', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140096)]' (**arg(95, 1140096))
hide p1101
$ update_portrait('st038_01 4', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('st040_01 1', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1140097)]' (**arg(96, 1140097))
hide p239
$ update_portrait('st032_01 4', 'p231', [r(2), light], 6)
get_char('c2313') '[convertstrid(1140098)]' (**arg(97, 1140098))
hide p237
hide p231
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1140099)]' (**arg(98, 1140099))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140100)]' (**arg(99, 1140100))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140101)]' (**arg(100, 1140101))
hide p2
hide p1
$ update_narrator('c11013')
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
with fade
$ update_portrait('oc004_01 21', 'p1101', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li20.ogg"
get_char('c11013') '[convertstrid(1140102)]' (**arg(101, 1140102))
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140103)]' (**arg(102, 1140103))
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140104)]' (**arg(103, 1140104))
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140105)]' (**arg(104, 1140105))
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140106)]' (**arg(105, 1140106))
$ update_portrait('oc004_01 16', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140107)]' (**arg(106, 1140107))
$ update_portrait('oc004_01 16', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140108)]' (**arg(107, 1140108))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140109)]' (**arg(108, 1140109))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140110)]' (**arg(109, 1140110))
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140111)]' (**arg(110, 1140111))
hide p1101
$ update_portrait('st039_01 2', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140112)]' (**arg(111, 1140112))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140113)]' (**arg(112, 1140113))
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140114)]' (**arg(113, 1140114))
hide p1
$ update_portrait('st039_01 2', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c33') '[convertstrid(1140115)]' (**arg(114, 1140115))
hide p3
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140116)]' (**arg(115, 1140116))
$ update_portrait('oc004_01 21', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140117)]' (**arg(116, 1140117))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140118)]' (**arg(117, 1140118))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p1101', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li20.ogg"
get_char('c11013') '[convertstrid(1140119)]' (**arg(118, 1140119))
hide p238
hide p1101
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1140120)]' (**arg(119, 1140120))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1140121)]' (**arg(120, 1140121))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140122)]' (**arg(121, 1140122))
hide p231
$ update_portrait('st038_01 1', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140123)]' (**arg(122, 1140123))
hide p1
$ update_portrait('st038_01 1', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140124)]' (**arg(123, 1140124))
$ update_portrait('oc004_01 9', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c11013') '[convertstrid(1140125)]' (**arg(124, 1140125))
hide p237
$ update_portrait('oc004_01 9', 'p1101', [r(-5), dark], 5)
$ update_portrait('st032_01 2', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140126)]' (**arg(125, 1140126))
hide p231
$ update_portrait('st039_01 1', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140127)]' (**arg(126, 1140127))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140128)]' (**arg(127, 1140128))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140129)]' (**arg(128, 1140129))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140130)]' (**arg(129, 1140130))
$ update_portrait('oc004_01 4', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140131)]' (**arg(130, 1140131))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140132)]' (**arg(131, 1140132))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 14', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140133)]' (**arg(132, 1140133))
$ update_portrait('oc004_01 10', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140134)]' (**arg(133, 1140134))
$ update_portrait('oc004_01 10', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140135)]' (**arg(134, 1140135))
$ update_portrait('oc004_01 10', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140136)]' (**arg(135, 1140136))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140137)]' (**arg(136, 1140137))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140138)]' (**arg(137, 1140138))
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140139)]' (**arg(138, 1140139))
$ update_portrait('st039_01 2', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p1101', [r(-5), r_shake, light], 6)
get_char('c11013') '[convertstrid(1140140)]' (**arg(139, 1140140))
$ update_portrait('oc004_01 13', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140141)]' (**arg(140, 1140141))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140142)]' (**arg(141, 1140142))
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140143)]' (**arg(142, 1140143))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140144)]' (**arg(143, 1140144))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c11013') '[convertstrid(1140145)]' (**arg(144, 1140145))
hide p1101
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140146)]' (**arg(145, 1140146, size=(0.9)))
hide p238
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch02.ogg"
get_char('c21') '[convertstrid(1140147)]' (**arg(146, 1140147, size=(0.9)))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1140148)]' (**arg(147, 1140148, size=(0.9)))
hide p3
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140149)]' (**arg(148, 1140149))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140150)]' (**arg(149, 1140150))
hide p1
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140151)]' (**arg(150, 1140151))
$ update_portrait('oc004_01 4', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 2', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140152)]' (**arg(151, 1140152))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140153)]' (**arg(152, 1140153))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 11', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140154)]' (**arg(153, 1140154))
$ update_portrait('oc004_01 11', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140155)]' (**arg(154, 1140155))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140156)]' (**arg(155, 1140156))
hide p238
$ update_portrait('st032_01 4', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140157)]' (**arg(156, 1140157))
hide p1101
$ update_portrait('st032_01 4', 'p231', [l(2), dark, flip], 5)
$ update_portrait('st040_01 3', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1140158)]' (**arg(157, 1140158))
hide p231
$ update_portrait('st040_01 3', 'p239', [r(-19), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140159)]' (**arg(158, 1140159))
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140160)]' (**arg(159, 1140160))
hide p239
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li20.ogg"
get_char('c11013') '[convertstrid(1140161)]' (**arg(160, 1140161)) with shake
$ update_portrait('oc004_01 16', 'p1101', [r(-5), dark], 5)
$ update_portrait('st039_01 4', 'p238', [l(-6), light, flip], 6)
get_char('c2381') '[convertstrid(1140162)]' (**arg(161, 1140162))
$ update_portrait('st039_01 4', 'p238', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
play sfxvoice "avg_vocal_li22.ogg"
get_char('c11013') '[convertstrid(1140163)]' (**arg(162, 1140163))
hide p238
$ update_portrait('oc004_01 21', 'p1101', [r(-5), dark], 5)
$ update_portrait('st038_01 1', 'p237', [l_entrance(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140164)]' (**arg(163, 1140164))
hide p1101
$ update_portrait('st038_01 1', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140165)]' (**arg(164, 1140165))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st038_01 4', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140166)]' (**arg(165, 1140166))
$ update_portrait('st038_01 4', 'p237', [l(-9), light, flip], 6)
get_char('c2371') '[convertstrid(1140167)]' (**arg(166, 1140167))
hide p2
$ update_portrait('st038_01 4', 'p237', [l(-9), dark, flip], 5)
$ update_portrait('st039_01 4', 'p238', [r(-6), light], 6)
get_char('c2383') '[convertstrid(1140168)]' (**arg(167, 1140168))
hide p237
hide p238
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
get_char('c31') '[convertstrid(1140169)]' (**arg(168, 1140169, size=(0.9)))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140170)]' (**arg(169, 1140170))
hide p3
$ update_portrait('oc004_01 21', 'p1101', [r(-5), dark], 5)
$ update_portrait('st032_01 2', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1140171)]' (**arg(170, 1140171))
$ update_portrait('st032_01 2', 'p231', [l(2), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p1101', [r(-5), light], 6)
get_char('c11013') '[convertstrid(1140172)]' (**arg(171, 1140172))
hide p231
hide p1101
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1140173)]' (**arg(172, 1140173, size=(0.9)))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1140174)]' (**arg(173, 1140174, size=(0.9)))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140175)]' (**arg(174, 1140175, size=(0.9)))
hide p3
hide p2
get_char('c0') '[convertstrid(1140176)]' (**arg(175, 1140176))
return