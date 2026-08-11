label avg10108(trans=fade_in):

$ play_music("ed7103.ogg")
scene avg_bg_007
$ update_narrator('c31')
window show
with trans
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1005965)]' (**arg(1, 1005965))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005966)]' (**arg(2, 1005966))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c41') '[convertstrid(1005967)]' (**arg(3, 1005967))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r_entrance(-5), light], 6)
play sfx2 "other_7047.ogg"
get_char('c63') '[convertstrid(1005968)]' (**arg(4, 1005968))
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005969)]' (**arg(5, 1005969))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1005970)]' (**arg(6, 1005970))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r_exit(-5), light], 6)
get_char('c63') '[convertstrid(1005971)]' (**arg(7, 1005971))
hide p6
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1005972)]' (**arg(8, 1005972))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005973)]' (**arg(9, 1005973))
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1005974)]' (**arg(10, 1005974))
hide p3
$ update_portrait('oc006_01 1', 'p6', [r_entrance(-5), light], 6)
play sfx2 "other_7047.ogg"
get_char('c63') '[convertstrid(1005975)]' (**arg(11, 1005975))
hide p2
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l_entrance(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1005976)]' (**arg(12, 1005976))
hide p6
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r_entrance(-14), light], 6)
get_char('c2413') '[convertstrid(1005977)]' (**arg(13, 1005977))
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1005978)]' (**arg(14, 1005978))
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1005979)]' (**arg(15, 1005979))
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1005980)]' (**arg(16, 1005980))
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1005981)]' (**arg(17, 1005981))
$ update_portrait('st043_01 1', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1005982)]' (**arg(18, 1005982))
$ update_portrait('st042_01 5', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1005983)]' (**arg(19, 1005983))
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1005984)]' (**arg(20, 1005984))
$ update_portrait('st042_01 2', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1001686)]' (**arg(21, 1001686))
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1005986)]' (**arg(22, 1005986))
$ update_portrait('st042_01 5', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), l_shake, light, flip], 6)
get_char('c2421') '[convertstrid(1005987)]' (**arg(23, 1005987))
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), r_shake, light], 6)
get_char('c2413') '[convertstrid(1005987)]' (**arg(24, 1005987))
hide p241
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1005988)]' (**arg(25, 1005988))
hide p242
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005989)]' (**arg(26, 1005989))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005990)]' (**arg(27, 1005990))
hide p3
$ update_portrait('st043_01 4', 'p242', [r(-17), light], 6)
get_char('c2423') '[convertstrid(1005991)]' (**arg(28, 1005991))
hide p1
$ update_portrait('st043_01 4', 'p242', [r(-17), dark], 5)
$ update_portrait('st042_01 2', 'p241', [l(-14), light, flip], 6)
get_char('c2411') '[convertstrid(1005992)]' (**arg(29, 1005992))
hide p242
$ update_portrait('st042_01 2', 'p241', [l(-14), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfx2 "other_7091.ogg"
play sfxvoice "avg_vocal_li18.ogg"
get_char('c43') '[convertstrid(1005993)]' (**arg(30, 1005993))
hide p241
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc006_01 1', 'p6', [l_midback(-5), light, flip], 6)
get_char('c61') '[convertstrid(1005994)]' (**arg(31, 1005994))
hide p4
$ update_portrait('oc006_01 1', 'p6', [l(-5), dark, flip], 5)
$ update_portrait('st043_01 2', 'p242', [r(-17), light], 6)
play sfx2 "other_7057.ogg"
get_char('c2423') '[convertstrid(1005995)]' (**arg(32, 1005995))
hide p6
$ update_portrait('st043_01 2', 'p242', [r(-17), dark], 5)
$ update_portrait('st042_01 2', 'p241', [l(-14), light, flip], 6)
get_char('c2411') '[convertstrid(1005996)]' (**arg(33, 1005996))
hide p242
$ update_portrait('st042_01 2', 'p241', [l(-14), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c43') '[convertstrid(1005997)]' (**arg(34, 1005997))
hide p241
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1005998)]' (**arg(35, 1005998))
hide p4
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1005999)]' (**arg(36, 1005999))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1006000)]' (**arg(37, 1006000))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006001)]' (**arg(38, 1006001))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006002)]' (**arg(39, 1006002))
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006003)]' (**arg(40, 1006003))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006004)]' (**arg(41, 1006004))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006005)]' (**arg(42, 1006005))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1006006)]' (**arg(43, 1006006))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006007)]' (**arg(44, 1006007))
$ update_portrait('st043_01 4', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006008)]' (**arg(45, 1006008))
$ update_portrait('st043_01 4', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006009)]' (**arg(46, 1006009))
hide p242
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c31') '[convertstrid(1006010)]' (**arg(47, 1006010))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006011)]' (**arg(48, 1006011))
$ update_portrait('st042_01 4', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006012)]' (**arg(49, 1006012))
hide p3
$ update_portrait('st042_01 4', 'p241', [r(-14), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006013)]' (**arg(50, 1006013))
hide p241
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1006014)]' (**arg(51, 1006014))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006015)]' (**arg(52, 1006015))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006016)]' (**arg(53, 1006016))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006017)]' (**arg(54, 1006017))
hide p4
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1006018)]' (**arg(55, 1006018))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1006019)]' (**arg(56, 1006019))
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006020)]' (**arg(57, 1006020))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c43') '[convertstrid(1006021)]' (**arg(58, 1006021))
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1006022)]' (**arg(59, 1006022))
$ update_portrait('oc004_01 23', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1006023)]' (**arg(60, 1006023))
hide p1
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006024)]' (**arg(61, 1006024))
hide p4
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1006025)]' (**arg(62, 1006025))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006026)]' (**arg(63, 1006026))
hide p1
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 4', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006027)]' (**arg(64, 1006027))
hide p242
$ update_portrait('st042_01 4', 'p241', [r(-14), dark], 5)
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006028)]' (**arg(65, 1006028))
hide p241
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_03 2', 'p543', [r(-23), light], 6)
get_char('c5433') '[convertstrid(1006029)]' (**arg(66, 1006029))
hide p1
$ update_portrait('uc002_03 2', 'p543', [r(-23), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006030)]' (**arg(67, 1006030))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc002_03 2', 'p543', [r_exit(-23), light], 6)
get_char('c5433') '[convertstrid(1006031)]' (**arg(68, 1006031))
hide p543
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1006032)]' (**arg(69, 1006032))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1006033)]' (**arg(70, 1006033))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1006034)]' (**arg(71, 1006034))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st043_01 2', 'p242', [r(-17), r_shake, light], 6)
get_char('c2423') '[convertstrid(1006035)]' (**arg(72, 1006035))
hide p3
$ update_portrait('st043_01 2', 'p242', [r(-17), dark], 5)
$ update_portrait('st042_01 2', 'p241', [l(-14), light, flip], 6)
get_char('c2411') '[convertstrid(1006036)]' (**arg(73, 1006036))
hide p241
hide p242
get_char('c0') '[convertstrid(1006037)]' (**arg(74, 1006037))
$ update_portrait('st043_01 2', 'p242', [r(-17), light], 6)
get_char('c2423') '[convertstrid(1006038)]' (**arg(75, 1006038))
$ update_portrait('st043_01 2', 'p242', [r(-17), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1006039)]' (**arg(76, 1006039))
hide p3
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006040)]' (**arg(77, 1006040))
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006041)]' (**arg(78, 1006041))
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006042)]' (**arg(79, 1006042))
hide p241
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro10.ogg"
get_char('c33') '[convertstrid(1006043)]' (**arg(80, 1006043))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006044)]' (**arg(81, 1006044))
hide p3
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006045)]' (**arg(82, 1006045))
hide p242
$ update_portrait('st042_01 5', 'p241', [r(-14), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7091.ogg"
get_char('c41') '[convertstrid(1005993)]' (**arg(83, 1005993))
hide p241
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc006_01 1', 'p6', [r(-5), light], 6)
get_char('c63') '[convertstrid(1005994)]' (**arg(84, 1005994))
hide p4
$ update_portrait('oc006_01 1', 'p6', [r(-5), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006048)]' (**arg(85, 1006048))
hide p6
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006049)]' (**arg(86, 1006049))
$ update_portrait('st042_01 2', 'p241', [r(-14), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006050)]' (**arg(87, 1006050))
hide p241
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1006051)]' (**arg(88, 1006051))
hide p242
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006052)]' (**arg(89, 1006052))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006053)]' (**arg(90, 1006053))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006054)]' (**arg(91, 1006054))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006055)]' (**arg(92, 1006055))
hide p3
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006056)]' (**arg(93, 1006056))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006057)]' (**arg(94, 1006057))
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006058)]' (**arg(95, 1006058))
hide p1
$ update_portrait('st043_01 1', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006059)]' (**arg(96, 1006059))
hide p241
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c33') '[convertstrid(1006060)]' (**arg(97, 1006060))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('st043_01 1', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006061)]' (**arg(98, 1006061))
hide p3
$ update_portrait('st043_01 1', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "bcv_oc002_die_01.ogg"
get_char('c23') '[convertstrid(1005841)]' (**arg(99, 1005841))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st043_01 5', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006063)]' (**arg(100, 1006063))
hide p2
$ update_portrait('st043_01 5', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 1', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006064)]' (**arg(101, 1006064))
hide p242
$ update_portrait('st042_01 1', 'p241', [r(-14), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006065)]' (**arg(102, 1006065))
hide p4
$ update_portrait('st043_01 2', 'p242', [l(-17), light, flip], 6)
get_char('c2421') '[convertstrid(1006066)]' (**arg(103, 1006066))
$ update_portrait('st043_01 2', 'p242', [l(-17), dark, flip], 5)
$ update_portrait('st042_01 2', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006067)]' (**arg(104, 1006067))
$ update_portrait('st042_01 5', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1001686)]' (**arg(105, 1001686))
hide p241
$ update_portrait('st043_01 5', 'p242', [r(-17), light], 6)
get_char('c2423') '[convertstrid(1001686)]' (**arg(106, 1001686))
$ update_portrait('st043_01 5', 'p242', [r(-17), dark], 5)
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006069)]' (**arg(107, 1006069))
hide p242
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st042_01 4', 'p241', [r(-14), light], 6)
get_char('c2413') '[convertstrid(1006070)]' (**arg(108, 1006070))
hide p241
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006071)]' (**arg(109, 1006071))
hide p4
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1006072)]' (**arg(110, 1006072))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006073)]' (**arg(111, 1006073))
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006074)]' (**arg(112, 1006074))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1006075)]' (**arg(113, 1006075))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006076)]' (**arg(114, 1006076))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c11') '[convertstrid(1006077)]' (**arg(115, 1006077))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c33') '[convertstrid(1006078)]' (**arg(116, 1006078))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006079)]' (**arg(117, 1006079))
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006080)]' (**arg(118, 1006080))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1006081)]' (**arg(119, 1006081))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li06.ogg"
get_char('c41') '[convertstrid(1006082)]' (**arg(120, 1006082))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006083)]' (**arg(121, 1006083))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006084)]' (**arg(122, 1006084))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1006085)]' (**arg(123, 1006085))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1006086)]' (**arg(124, 1006086))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 6', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c41') '[convertstrid(1006087)]' (**arg(125, 1006087))
hide p2
$ update_portrait('oc004_01 6', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006088)]' (**arg(126, 1006088))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1006089)]' (**arg(127, 1006089))
return "avg10108"