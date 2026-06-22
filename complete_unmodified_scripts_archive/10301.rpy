label avg10301:

stop music
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1130001)]' (**arg(1, 1130001))
get_char('c0') '[convertstrid(1130002)]' (**arg(2, 1130002))
get_char('c0') '[convertstrid(1130003)]' (**arg(3, 1130003))
$ play_music("ed7111.ogg")
play sfx2 "other_7042.ogg"
get_char('c0') '[convertstrid(1130004)]' (**arg(4, 1130004))
scene avg_bg_012
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7046.ogg"
get_char('c13') '[convertstrid(1130005)]' (**arg(5, 1130005))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130006)]' (**arg(6, 1130006))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc005_01 2', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130007)]' (**arg(7, 1130007))
hide p2
$ update_portrait('oc005_01 2', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130008)]' (**arg(8, 1130008))
hide p5
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130009)]' (**arg(9, 1130009))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c41') '[convertstrid(1130010)]' (**arg(10, 1130010))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 8', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130011)]' (**arg(11, 1130011))
hide p4
$ update_portrait('oc005_01 8', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130012)]' (**arg(12, 1130012))
hide p5
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130013)]' (**arg(13, 1130013))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130014)]' (**arg(14, 1130014))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130015)]' (**arg(15, 1130015))
hide p2
hide p1
play sfx2 "other_7020.ogg"
get_char('c0') '[convertstrid(1130016)]' (**arg(16, 1130016))
scene avg_bg_047
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
play sfx2 "other_7044.ogg"
get_char('c33') '[convertstrid(1130017)]' (**arg(17, 1130017))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
get_char('c10011') '[convertstrid(1130018)]' (**arg(18, 1130018))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130019)]' (**arg(19, 1130019))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1130020)]' (**arg(20, 1130020))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130021)]' (**arg(21, 1130021))
hide p2
hide p1
$ update_portrait('sc046_01 2', 'p670', [l(-5), light, flip], 6)
$ update_narrator('c6701')
with fade
get_char('c6701') '[convertstrid(1130022)]' (**arg(22, 1130022))
$ update_portrait('sc046_01 2', 'p670', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130023)]' (**arg(23, 1130023))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc046_01 4', 'p670', [l(-5), light, flip], 6)
get_char('c6701') '[convertstrid(1130024)]' (**arg(24, 1130024))
$ update_portrait('sc046_01 4', 'p670', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130025)]' (**arg(25, 1130025))
hide p670
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1130026)]' (**arg(26, 1130026))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130027)]' (**arg(27, 1130027))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 21', 'p5', [r_entrance(-6), light], 6)
get_char('c53') '[convertstrid(1130028)]' (**arg(28, 1130028))
hide p3
$ update_portrait('oc005_01 21', 'p5', [r(-6), dark], 5)
$ update_portrait('st031_01 4', 'p230', [l_entrance(4), light, flip], 6)
get_char('c2301') '[convertstrid(1130029)]' (**arg(29, 1130029))
hide p5
$ update_portrait('st031_01 4', 'p230', [l(4), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c43') '[convertstrid(1130030)]' (**arg(30, 1130030))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130031)]' (**arg(31, 1130031))
hide p230
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130032)]' (**arg(32, 1130032))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1134110)]' (**arg(33, 1134110))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130033)]' (**arg(34, 1130033))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 5', 'p229', [l_entrance(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130034)]' (**arg(35, 1130034))
$ update_portrait('st030_01 5', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130035)]' (**arg(36, 1130035))
hide p1
$ update_portrait('st030_01 5', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c23') '[convertstrid(1130036)]' (**arg(37, 1130036))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130037)]' (**arg(38, 1130037))
hide p229
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st031_01 4', 'p230', [l(4), light, flip], 6)
get_char('c2301') '[convertstrid(1130038)]' (**arg(39, 1130038))
hide p1
$ update_portrait('st031_01 4', 'p230', [l(4), dark, flip], 5)
$ update_portrait('st030_01 4', 'p229', [r(-8), light], 6)
get_char('c2293') '[convertstrid(1130040)]' (**arg(40, 1130040))
$ update_portrait('st030_01 4', 'p229', [r(-8), dark], 5)
$ update_portrait('st031_01 3', 'p230', [l(4), light, flip], 6)
get_char('c2301') '[convertstrid(1130041)]' (**arg(41, 1130041))
$ update_portrait('st031_01 3', 'p230', [l(4), dark, flip], 5)
$ update_portrait('st030_01 5', 'p229', [r(-8), light], 6)
get_char('c2293') '[convertstrid(1130042)]' (**arg(42, 1130042))
hide p230
hide p229
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
$ update_narrator('c2291')
with fade
get_char('c2291') '[convertstrid(1130043)]' (**arg(43, 1130043))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130044)]' (**arg(44, 1130044))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130045)]' (**arg(45, 1130045))
$ play_music("ed7151.ogg")
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1130046)]' (**arg(46, 1130046))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130047)]' (**arg(47, 1130047))
hide p1
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130048)]' (**arg(48, 1130048))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130049)]' (**arg(49, 1130049))
hide p2
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130050)]' (**arg(50, 1130050))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130051)]' (**arg(51, 1130051))
hide p3
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1130052)]' (**arg(52, 1130052))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130053)]' (**arg(53, 1130053))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130054)]' (**arg(54, 1130054))
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130055)]' (**arg(55, 1130055))
hide p229
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130056)]' (**arg(56, 1130056))
hide p4
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130057)]' (**arg(57, 1130057))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130058)]' (**arg(58, 1130058))
hide p2
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130059)]' (**arg(59, 1130059))
hide p229
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130060)]' (**arg(60, 1130060))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130061)]' (**arg(61, 1130061))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l_entrance(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130062)]' (**arg(62, 1130062))
hide p1
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1130063)]' (**arg(63, 1130063))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130064)]' (**arg(64, 1130064))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130065)]' (**arg(65, 1130065))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130066)]' (**arg(66, 1130066))
hide p4
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c33') '[convertstrid(1130067)]' (**arg(67, 1130067))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130068)]' (**arg(68, 1130068))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130069)]' (**arg(69, 1130069))
hide p3
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1130070)]' (**arg(70, 1130070))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st030_01 5', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130071)]' (**arg(71, 1130071))
hide p2
$ update_portrait('st030_01 5', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130072)]' (**arg(72, 1130072))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130073)]' (**arg(73, 1130073))
hide p1
$ update_portrait('st030_01 4', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('sc046_01 4', 'p1004', [r(-5), light], 6)
get_char('c10043') '[convertstrid(1130074)]' (**arg(74, 1130074))
$ update_portrait('sc046_01 4', 'p1004', [r(-5), dark], 5)
$ update_portrait('st030_01 2', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130075)]' (**arg(75, 1130075))
$ update_portrait('st030_01 2', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('sc046_01 2', 'p1004', [r(-5), r_shake, light], 6)
get_char('c10043') '[convertstrid(1130076)]' (**arg(76, 1130076))
$ update_portrait('sc046_01 5', 'p1004', [r(-5), light], 6)
get_char('c10043') '[convertstrid(1130077)]' (**arg(77, 1130077))
hide p229
hide p1004
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1130078)]' (**arg(78, 1130078))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130079)]' (**arg(79, 1130079))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130080)]' (**arg(80, 1130080))
hide p2
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130081)]' (**arg(81, 1130081))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130082)]' (**arg(82, 1130082))
hide p1
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1130083)]' (**arg(83, 1130083))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('st030_01 5', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130084)]' (**arg(84, 1130084))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130085)]' (**arg(85, 1130085))
hide p2
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1130086)]' (**arg(86, 1130086))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130087)]' (**arg(87, 1130087))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130088)]' (**arg(88, 1130088))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130089)]' (**arg(89, 1130089))
hide p229
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c41') '[convertstrid(1130090)]' (**arg(90, 1130090))
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130091)]' (**arg(91, 1130091))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130092)]' (**arg(92, 1130092))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130093)]' (**arg(93, 1130093))
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130094)]' (**arg(94, 1130094))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130095)]' (**arg(95, 1130095))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st030_01 5', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130096)]' (**arg(96, 1130096))
$ update_portrait('st030_01 4', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130097)]' (**arg(97, 1130097))
$ update_portrait('st030_01 1', 'p229', [l(-8), light, flip], 6)
get_char('c2291') '[convertstrid(1130098)]' (**arg(98, 1130098))
$ update_portrait('st030_01 1', 'p229', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130099)]' (**arg(99, 1130099))
hide p229
hide p1
$ update_portrait('st030_01 4', 'p229', [r(-8), light], 6)
$ update_narrator('c2293')
with fade
get_char('c2293') '[convertstrid(1130100)]' (**arg(100, 1130100))
$ update_portrait('st030_01 4', 'p229', [r(-8), dark], 5)
$ update_portrait('st031_01 4', 'p230', [l(4), light, flip], 6)
get_char('c2301') '[convertstrid(1130101)]' (**arg(101, 1130101))
$ update_portrait('st031_01 4', 'p230', [l(4), dark, flip], 5)
$ update_portrait('st030_01 5', 'p229', [r(-8), light], 6)
get_char('c2293') '[convertstrid(1130102)]' (**arg(102, 1130102))
$ update_portrait('st030_01 4', 'p229', [r(-8), light], 6)
get_char('c2293') '[convertstrid(1130103)]' (**arg(103, 1130103))
hide p229
$ update_portrait('sc046_01 4', 'p53', [r(-5), light], 6)
get_char('c533') '[convertstrid(1130104)]' (**arg(104, 1130104))
$ play_music("ed7111.ogg")
hide p230
hide p53
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
get_char('c41') '[convertstrid(1130105)]' (**arg(105, 1130105))
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1130106)]' (**arg(106, 1130106))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130107)]' (**arg(107, 1130107))
hide p1
$ update_portrait('oc005_01 8', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130108)]' (**arg(108, 1130108))
$ update_portrait('oc005_01 12', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130109)]' (**arg(109, 1130109))
hide p4
$ update_portrait('oc005_01 12', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1130110)]' (**arg(110, 1130110))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130111)]' (**arg(111, 1130111))
hide p2
hide p5
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1130113)]' (**arg(112, 1130113))
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1130114)]' (**arg(113, 1130114))
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1130115)]' (**arg(114, 1130115))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130116)]' (**arg(115, 1130116))
$ update_portrait('oc005_01 22', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130118)]' (**arg(116, 1130118))
$ update_portrait('oc005_01 22', 'p5', [r(-6), dark], 5)
$ update_portrait('st031_01 4', 'p230', [l_entrance(4), light, flip], 6)
get_char('c2301') '[convertstrid(1130119)]' (**arg(117, 1130119))
$ update_portrait('st031_01 4', 'p230', [l(4), dark, flip], 5)
$ update_portrait('oc005_01 7', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1130120)]' (**arg(118, 1130120))
hide p5
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130121)]' (**arg(119, 1130121))
hide p230
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1130122)]' (**arg(120, 1130122))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130123)]' (**arg(121, 1130123))
return