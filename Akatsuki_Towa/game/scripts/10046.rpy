label avg10046:

$ play_music("ed7150.ogg")
scene avg_bg_003
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7046.ogg"
get_char('c13') '[convertstrid(1004017)]' (**arg(1, 1004017))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1004018)]' (**arg(2, 1004018))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004019)]' (**arg(3, 1004019))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004020)]' (**arg(4, 1004020))
hide p4
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1004021)]' (**arg(5, 1004021))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004022)]' (**arg(6, 1004022))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
play sfx2 "other_7023.ogg"
get_char('c53') '[convertstrid(1004023)]' (**arg(7, 1004023))
$ update_portrait('oc005_01 5', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004024)]' (**arg(8, 1004024))
hide p3
$ update_portrait('oc005_01 5', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004025)]' (**arg(9, 1004025))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li02.ogg"
get_char('c41') '[convertstrid(1004026)]' (**arg(10, 1004026))
hide p4
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004027)]' (**arg(11, 1004027))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 10', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004028)]' (**arg(12, 1004028))
$ update_portrait('oc005_01 10', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004029)]' (**arg(13, 1004029))
hide p5
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c43') '[convertstrid(1004030)]' (**arg(14, 1004030))
hide p3
$ update_portrait('oc004_01 5', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c21') '[convertstrid(1004031)]' (**arg(15, 1004031))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004032)]' (**arg(16, 1004032))
hide p2
$ update_portrait('oc004_01 13', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004033)]' (**arg(17, 1004033))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004034)]' (**arg(18, 1004034))
hide p4
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
play sfxvoice "avg_vocal_ji10.ogg"
get_char('c53') '[convertstrid(1004035)]' (**arg(19, 1004035))
$ update_portrait('oc005_01 2', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004036)]' (**arg(20, 1004036))
hide p1
$ update_portrait('oc005_01 2', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002182)]' (**arg(21, 1002182))
hide p2
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004038)]' (**arg(22, 1004038))
hide p1
hide p5
get_char('c0') '[convertstrid(1004039)]' (**arg(23, 1004039))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
play sfx2 "other_7022.ogg"
get_char('c53') '[convertstrid(1004040)]' (**arg(24, 1004040))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004041)]' (**arg(25, 1004041))
hide p5
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004042)]' (**arg(26, 1004042))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004043)]' (**arg(27, 1004043))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004044)]' (**arg(28, 1004044))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003250)]' (**arg(29, 1003250))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004046)]' (**arg(30, 1004046))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1004047)]' (**arg(31, 1004047))
hide p1
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c33') '[convertstrid(1004048)]' (**arg(32, 1004048))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1004049)]' (**arg(33, 1004049))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004050)]' (**arg(34, 1004050))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004051)]' (**arg(35, 1004051))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004052)]' (**arg(36, 1004052))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004053)]' (**arg(37, 1004053))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004054)]' (**arg(38, 1004054))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004055)]' (**arg(39, 1004055))
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004056)]' (**arg(40, 1004056))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004057)]' (**arg(41, 1004057))
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1004058)]' (**arg(42, 1004058))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1004059)]' (**arg(43, 1004059))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1004060)]' (**arg(44, 1004060))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c11') '[convertstrid(1004061)]' (**arg(45, 1004061))
hide p3
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004062)]' (**arg(46, 1004062))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
play sfx2 "other_7024.ogg"
get_char('c53') '[convertstrid(1004063)]' (**arg(47, 1004063))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004064)]' (**arg(48, 1004064))
hide p5
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1004065)]' (**arg(49, 1004065))
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004066)]' (**arg(50, 1004066))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004067)]' (**arg(51, 1004067))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004068)]' (**arg(52, 1004068))
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004069)]' (**arg(53, 1004069))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1004070)]' (**arg(54, 1004070))
hide p4
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004071)]' (**arg(55, 1004071))
hide p5
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1004072)]' (**arg(56, 1004072))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1004073)]' (**arg(57, 1004073))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc005_01 8', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1004074)]' (**arg(58, 1004074))
hide p3
$ update_portrait('oc005_01 8', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004075)]' (**arg(59, 1004075))
hide p5
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004076)]' (**arg(60, 1004076))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004077)]' (**arg(61, 1004077))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro04.ogg"
get_char('c31') '[convertstrid(1004078)]' (**arg(62, 1004078))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1004079)]' (**arg(63, 1004079))
return