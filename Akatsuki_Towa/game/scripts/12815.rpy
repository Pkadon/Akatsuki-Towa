label avg12815(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1183001)]' (**arg(1, 1183001))
$ update_portrait('st061_01 1', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1183002)]' (**arg(2, 1183002))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183003)]' (**arg(3, 1183003))
hide p1304
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1183004)]' (**arg(4, 1183004))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183005)]' (**arg(5, 1183005))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183006)]' (**arg(6, 1183006))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1183007)]' (**arg(7, 1183007))
hide p1304
hide p1
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1183008)]' (**arg(8, 1183008))
hide p2
get_char('c0') '[convertstrid(1183009)]' (**arg(9, 1183009))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1183010)]' (**arg(10, 1183010))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1183011)]' (**arg(11, 1183011))
hide p1304
hide p2
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1183012)]' (**arg(12, 1183012))
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1183013)]' (**arg(13, 1183013))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183014)]' (**arg(14, 1183014))
hide p3
hide p1
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1183015)]' (**arg(15, 1183015))
scene avg_bg_011
$ update_narrator('c13043')
with fade
$ update_portrait('st061_01 1', 'p1304', [r_entrance(-2), light], 6)
get_char('c13043') '[convertstrid(1183016)]' (**arg(16, 1183016))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c7511') '[convertstrid(1183017)]' (**arg(17, 1183017))
hide p1304
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1183018)]' (**arg(18, 1183018))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183019)]' (**arg(19, 1183019))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c7511') '[convertstrid(1183020)]' (**arg(20, 1183020))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183021)]' (**arg(21, 1183021))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183022)]' (**arg(22, 1183022))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c25461') '[convertstrid(1183023)]' (**arg(23, 1183023))
hide p1
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183024)]' (**arg(24, 1183024))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
get_char('c25461') '[convertstrid(1183025)]' (**arg(25, 1183025))
get_char('c25461') '[convertstrid(1183026)]' (**arg(26, 1183026))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183027)]' (**arg(27, 1183027))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c25461') '[convertstrid(1183028)]' (**arg(28, 1183028))
get_char('c25461') '[convertstrid(1183029)]' (**arg(29, 1183029))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183030)]' (**arg(30, 1183030))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1183031)]' (**arg(31, 1183031))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c25461') '[convertstrid(1183032)]' (**arg(32, 1183032))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183033)]' (**arg(33, 1183033))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183034)]' (**arg(34, 1183034))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c25461') '[convertstrid(1183035)]' (**arg(35, 1183035))
get_char('c25461') '[convertstrid(1183036)]' (**arg(36, 1183036))
get_char('c25471') '[convertstrid(1183037)]' (**arg(37, 1183037))
get_char('c25461') '[convertstrid(1183038)]' (**arg(38, 1183038))
get_char('c25471') '[convertstrid(1183039)]' (**arg(39, 1183039))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183040)]' (**arg(40, 1183040))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183041)]' (**arg(41, 1183041))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
get_char('c25471') '[convertstrid(1183042)]' (**arg(42, 1183042))
get_char('c25471') '[convertstrid(1183043)]' (**arg(43, 1183043))
get_char('c25471') '[convertstrid(1183044)]' (**arg(44, 1183044))
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1183045)]' (**arg(45, 1183045))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
get_char('c25471') '[convertstrid(1183046)]' (**arg(46, 1183046))
hide p3
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183047)]' (**arg(47, 1183047))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
get_char('c25471') '[convertstrid(1183048)]' (**arg(48, 1183048))
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183049)]' (**arg(49, 1183049))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c25461') '[convertstrid(1183050)]' (**arg(50, 1183050))
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1183051)]' (**arg(51, 1183051))
hide p2
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1183052)]' (**arg(52, 1183052))
hide p1304
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c25471') '[convertstrid(1183053)]' (**arg(53, 1183053))
get_char('c25461') '[convertstrid(1183054)]' (**arg(54, 1183054))
get_char('c25471') '[convertstrid(1183055)]' (**arg(55, 1183055))
get_char('c25471') '[convertstrid(1183056)]' (**arg(56, 1183056))
get_char('c25471') '[convertstrid(1183057)]' (**arg(57, 1183057))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1183058)]' (**arg(58, 1183058))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1183059)]' (**arg(59, 1183059))
hide p3
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183060)]' (**arg(60, 1183060))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183061)]' (**arg(61, 1183061))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c25471') '[convertstrid(1183062)]' (**arg(62, 1183062))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183063)]' (**arg(63, 1183063))
hide p1
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183064)]' (**arg(64, 1183064))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
get_char('c25461') '[convertstrid(1183065)]' (**arg(65, 1183065))
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1183066)]' (**arg(66, 1183066))
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
get_char('c25461') '[convertstrid(1183067)]' (**arg(67, 1183067))
get_char('c25471') '[convertstrid(1183068)]' (**arg(68, 1183068))
get_char('c25461') '[convertstrid(1183069)]' (**arg(69, 1183069))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1183070)]' (**arg(70, 1183070))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c25471') '[convertstrid(1183071)]' (**arg(71, 1183071))
hide p3
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183072)]' (**arg(72, 1183072))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
get_char('c25461') '[convertstrid(1183073)]' (**arg(73, 1183073))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183074)]' (**arg(74, 1183074))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183075)]' (**arg(75, 1183075))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 3', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1183076)]' (**arg(76, 1183076))
hide p1
$ update_portrait('st061_01 3', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183077)]' (**arg(77, 1183077))
hide p1304
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
get_char('c25461') '[convertstrid(1183078)]' (**arg(78, 1183078))
hide p2
get_char('c0') '[convertstrid(1183079)]' (**arg(79, 1183079))
get_char('c25471') '[convertstrid(1183080)]' (**arg(80, 1183080))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1183081)]' (**arg(81, 1183081))
hide p2
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1183082)]' (**arg(82, 1183082))
scene avg_bg_050
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 23', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1183083)]' (**arg(83, 1183083))
$ update_portrait('oc002_01 23', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183084)]' (**arg(84, 1183084))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1183085)]' (**arg(85, 1183085))
hide p1304
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1183086)]' (**arg(86, 1183086))
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1183087)]' (**arg(87, 1183087))
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183088)]' (**arg(88, 1183088))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1183089)]' (**arg(89, 1183089))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183090)]' (**arg(90, 1183090))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1183091)]' (**arg(91, 1183091))
return "avg12815"