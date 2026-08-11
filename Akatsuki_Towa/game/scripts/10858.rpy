label avg10858(trans=fade_in):

$ play_music("ed7544.ogg")
scene avg_bg_222
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfx2 "other_7057.ogg"
get_char('c21') '[convertstrid(1190010)]' (**arg(1, 1190010))
stop music
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1190011)]' (**arg(2, 1190011))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1190012)]' (**arg(3, 1190012))
hide p2
$ update_portrait('oc008_02 3', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1190013)]' (**arg(4, 1190013))
$ update_portrait('oc008_02 3', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1190014)]' (**arg(5, 1190014))
hide p8
hide p1
play sfx2 "other_7057.ogg"
get_char('c0') '[convertstrid(1190015)]' (**arg(6, 1190015))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1190016)]' (**arg(7, 1190016))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1190017)]' (**arg(8, 1190017))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190018)]' (**arg(9, 1190018))
hide p2
hide p1
play sfx2 "fight_6008.ogg"
get_char('c0') '[convertstrid(1190019)]' (**arg(10, 1190019)) with shake
$ update_portrait('oc002_01 20', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190020)]' (**arg(11, 1190020))
$ play_music("ed7510.ogg")
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6027.ogg"
get_char('c13') '[convertstrid(1190021)]' (**arg(12, 1190021))
hide p2
hide p1
get_char('c0') '[convertstrid(1190022)]' (**arg(13, 1190022))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1190023)]' (**arg(14, 1190023)) with shake
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190024)]' (**arg(15, 1190024))
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190025)]' (**arg(16, 1190025))
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1190026)]' (**arg(17, 1190026))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190027)]' (**arg(18, 1190027))
hide p2
hide p1
play sfx2 "fight_6001.ogg"
get_char('c0') '[convertstrid(1190028)]' (**arg(19, 1190028)) with shake
$ update_portrait('oc002_01 20', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1190029)]' (**arg(20, 1190029))
$ update_portrait('oc002_01 20', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1190030)]' (**arg(21, 1190030))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190031)]' (**arg(22, 1190031))
hide p2
hide p1
get_char('c0') '[convertstrid(1190032)]' (**arg(23, 1190032))
play sfx2 "fight_6026.ogg"
get_char('c0') '[convertstrid(1190033)]' (**arg(24, 1190033))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1190034)]' (**arg(25, 1190034))
hide p2
play sfx2 "fight_6015.ogg"
get_char('c0') '[convertstrid(1190035)]' (**arg(26, 1190035)) with shake
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1190036)]' (**arg(27, 1190036))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1190037)]' (**arg(28, 1190037, size=(1.15))) with shake
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "fight_6015.ogg"
get_char('c0') '[convertstrid(1190038)]' (**arg(29, 1190038))
scene avg_bg_511
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1190039)]' (**arg(30, 1190039))
play sfx2 "fight_6001.ogg"
get_char('c13') '[convertstrid(1190040)]' (**arg(31, 1190040)) with shake
get_char('c21') '[convertstrid(1190041)]' (**arg(32, 1190041))
get_char('c13') '[convertstrid(1190042)]' (**arg(33, 1190042))
play sfx2 "fight_6027.ogg"
get_char('c21') '[convertstrid(1190043)]' (**arg(34, 1190043)) with shake
get_char('c21') '[convertstrid(1190044)]' (**arg(35, 1190044))
get_char('c13') '[convertstrid(1190045)]' (**arg(36, 1190045))
get_char('c21') '[convertstrid(1190046)]' (**arg(37, 1190046))
get_char('c13') '[convertstrid(1190047)]' (**arg(38, 1190047)) with shake
get_char('c13') '[convertstrid(1190048)]' (**arg(39, 1190048))
get_char('c13') '[convertstrid(1190049)]' (**arg(40, 1190049))
play sfx2 "fight_6015.ogg"
get_char('c13') '[convertstrid(1190050)]' (**arg(41, 1190050)) with shake
get_char('c21') '[convertstrid(1190051)]' (**arg(42, 1190051))
get_char('c13') '[convertstrid(1190052)]' (**arg(43, 1190052))
get_char('c21') '[convertstrid(1190053)]' (**arg(44, 1190053))
get_char('c13') '[convertstrid(1190054)]' (**arg(45, 1190054))
get_char('c21') '[convertstrid(1190055)]' (**arg(46, 1190055))
stop music
get_char('c21') '[convertstrid(1190056)]' (**arg(47, 1190056, size=(1.2))) with shake
get_char('c21') '[convertstrid(1190057)]' (**arg(48, 1190057))
$ play_music("ed7523.ogg")
get_char('c21') '[convertstrid(1190058)]' (**arg(49, 1190058))
get_char('c21') '[convertstrid(1190059)]' (**arg(50, 1190059))
get_char('c21') '[convertstrid(1190060)]' (**arg(51, 1190060))
get_char('c21') '[convertstrid(1190061)]' (**arg(52, 1190061))
get_char('c21') '[convertstrid(1190062)]' (**arg(53, 1190062))
get_char('c21') '[convertstrid(1190063)]' (**arg(54, 1190063))
get_char('c21') '[convertstrid(1190064)]' (**arg(55, 1190064))
get_char('c21') '[convertstrid(1190065)]' (**arg(56, 1190065))
get_char('c21') '[convertstrid(1190066)]' (**arg(57, 1190066))
get_char('c21') '[convertstrid(1190067)]' (**arg(58, 1190067))
get_char('c13') '[convertstrid(1190068)]' (**arg(59, 1190068))
get_char('c21') '[convertstrid(1190069)]' (**arg(60, 1190069))
get_char('c21') '[convertstrid(1190070)]' (**arg(61, 1190070))
get_char('c21') '[convertstrid(1190071)]' (**arg(62, 1190071))
get_char('c81') '[convertstrid(1190072)]' (**arg(63, 1190072))
scene avg_bg_512
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1190073)]' (**arg(64, 1190073))
get_char('c23') '[convertstrid(1190074)]' (**arg(65, 1190074))
get_char('c13') '[convertstrid(1190075)]' (**arg(66, 1190075))
get_char('c23') '[convertstrid(1190076)]' (**arg(67, 1190076))
get_char('c23') '[convertstrid(1190077)]' (**arg(68, 1190077))
get_char('c81') '[convertstrid(1190078)]' (**arg(69, 1190078))
get_char('c23') '[convertstrid(1190079)]' (**arg(70, 1190079))
get_char('c81') '[convertstrid(1190080)]' (**arg(71, 1190080))
get_char('c23') '[convertstrid(1190081)]' (**arg(72, 1190081))
get_char('c13') '[convertstrid(1190082)]' (**arg(73, 1190082))
get_char('c23') '[convertstrid(1190083)]' (**arg(74, 1190083))
get_char('c81') '[convertstrid(1190084)]' (**arg(75, 1190084))
get_char('c81') '[convertstrid(1190085)]' (**arg(76, 1190085))
get_char('c81') '[convertstrid(1190086)]' (**arg(77, 1190086))
get_char('c81') '[convertstrid(1190087)]' (**arg(78, 1190087))
get_char('c81') '[convertstrid(1190088)]' (**arg(79, 1190088))
get_char('c81') '[convertstrid(1190089)]' (**arg(80, 1190089))
get_char('c23') '[convertstrid(1190090)]' (**arg(81, 1190090))
get_char('c81') '[convertstrid(1190091)]' (**arg(82, 1190091))
get_char('c81') '[convertstrid(1190092)]' (**arg(83, 1190092))
get_char('c13') '[convertstrid(1190093)]' (**arg(84, 1190093))
get_char('c13') '[convertstrid(1190094)]' (**arg(85, 1190094))
get_char('c81') '[convertstrid(1190095)]' (**arg(86, 1190095))
get_char('c13') '[convertstrid(1190096)]' (**arg(87, 1190096))
get_char('c81') '[convertstrid(1190097)]' (**arg(88, 1190097))
get_char('c23') '[convertstrid(1190098)]' (**arg(89, 1190098))
get_char('c13') '[convertstrid(1190099)]' (**arg(90, 1190099))
get_char('c13') '[convertstrid(1190100)]' (**arg(91, 1190100))
get_char('c13') '[convertstrid(1190101)]' (**arg(92, 1190101))
get_char('c23') '[convertstrid(1190102)]' (**arg(93, 1190102))
get_char('c81') '[convertstrid(1190103)]' (**arg(94, 1190103))
play sfx2 "fight_6020.ogg"
get_char('c0') '[convertstrid(1190104)]' (**arg(95, 1190104))
get_char('c23') '[convertstrid(1190105)]' (**arg(96, 1190105))
get_char('c23') '[convertstrid(1190106)]' (**arg(97, 1190106))
get_char('c81') '[convertstrid(1190107)]' (**arg(98, 1190107))
get_char('c81') '[convertstrid(1190108)]' (**arg(99, 1190108))
scene avg_bg_222
$ update_portrait('oc008_02 1', 'p8', [l(-5), light, flip], 6)
$ update_narrator('c81')
with fade
play sfx2 "fight_6015.ogg"
get_char('c81') '[convertstrid(1190109)]' (**arg(100, 1190109))
$ update_portrait('oc008_02 5', 'p8', [l(-5), light, flip], 6)
play sfx2 "fight_6015.ogg"
get_char('c81') '[convertstrid(1190110)]' (**arg(101, 1190110))
stop music
scene avg_bg_070
$ update_narrator('c13')
with fade
play sfx2 "fight_6020.ogg"
get_char('c13') '[convertstrid(1190111)]' (**arg(102, 1190111, size=(1.25)))
scene avg_bg_204
$ update_narrator('c0')
with fade
play sfx2 "fight_6015.ogg"
get_char('c0') '[convertstrid(1190112)]' (**arg(103, 1190112)) with shake
scene avg_bg_218
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1190113)]' (**arg(104, 1190113))
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 18', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1190114)]' (**arg(105, 1190114))
hide p3
$ update_portrait('oc004_01 18', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1190115)]' (**arg(106, 1190115))
hide p4
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1190116)]' (**arg(107, 1190116))
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1190117)]' (**arg(108, 1190117))
hide p16
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1190118)]' (**arg(109, 1190118))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1190119)]' (**arg(110, 1190119))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st063_01 1', 'p1346', [r(-16), light], 6)
get_char('c13463') '[convertstrid(1190120)]' (**arg(111, 1190120))
$ update_portrait('st063_01 1', 'p1346', [r(-16), light], 6)
get_char('c13463') '[convertstrid(1190121)]' (**arg(112, 1190121))
hide p4
$ update_portrait('st063_01 1', 'p1346', [r(-16), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1190122)]' (**arg(113, 1190122))
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1190123)]' (**arg(114, 1190123))
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1190124)]' (**arg(115, 1190124))
hide p1346
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1190125)]' (**arg(116, 1190125))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1190126)]' (**arg(117, 1190126))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1190127)]' (**arg(118, 1190127))
get_char('c0') '[convertstrid(1190128)]' (**arg(119, 1190128))
get_char('c5001') '[convertstrid(1190129)]' (**arg(120, 1190129))
get_char('c5001') '[convertstrid(1190130)]' (**arg(121, 1190130))
scene avg_bg_515
$ update_narrator('c5001')
with fade
get_char('c5001') '[convertstrid(1190131)]' (**arg(122, 1190131))
get_char('c5001') '[convertstrid(1190132)]' (**arg(123, 1190132))
get_char('c5001') '[convertstrid(1190133)]' (**arg(124, 1190133))
get_char('c5001') '[convertstrid(1190134)]' (**arg(125, 1190134))
get_char('c5001') '[convertstrid(1190135)]' (**arg(126, 1190135))
return "avg10858"