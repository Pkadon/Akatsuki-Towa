label avg10521:

$ play_music("ED6202.ogg")
scene avg_bg_107
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1151973)]' (**arg(1, 1151973))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151974)]' (**arg(2, 1151974))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151975)]' (**arg(3, 1151975))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1151976)]' (**arg(4, 1151976))
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1151977)]' (**arg(5, 1151977))
hide p240
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151978)]' (**arg(6, 1151978))
hide p1
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1151979)]' (**arg(7, 1151979))
hide p3
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l(-11), l_shake, light, flip], 6)
get_char('c2571') '[convertstrid(1151980)]' (**arg(8, 1151980))
$ update_portrait('st050_01 1', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151981)]' (**arg(9, 1151981))
hide p2
$ update_portrait('st050_01 1', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('st041_01 1', 'p240', [r_entrance(-1), light], 6)
get_char('c2403') '[convertstrid(1151982)]' (**arg(10, 1151982))
$ update_portrait('st041_01 1', 'p240', [r(-1), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l(-11), l_shake, light, flip], 6)
get_char('c2571') '[convertstrid(1151983)]' (**arg(11, 1151983, size=(1.2)))
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151984)]' (**arg(12, 1151984))
hide p257
hide p240
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1151985)]' (**arg(13, 1151985))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151986)]' (**arg(14, 1151986))
hide p2
hide p1
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
$ update_narrator('c2571')
with fade
get_char('c2571') '[convertstrid(1151987)]' (**arg(15, 1151987))
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151988)]' (**arg(16, 1151988))
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151989)]' (**arg(17, 1151989))
$ update_portrait('st050_01 6', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151990)]' (**arg(18, 1151990))
$ update_portrait('st050_01 6', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151991)]' (**arg(19, 1151991))
$ update_portrait('st050_01 6', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151992)]' (**arg(20, 1151992))
$ update_portrait('st050_01 6', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r_entrance(-5), light], 6)
play sfxvoice "avg_vocal_li13.ogg"
get_char('c43') '[convertstrid(1151993)]' (**arg(21, 1151993))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151994)]' (**arg(22, 1151994))
hide p1
$ update_portrait('st041_01 2', 'p240', [r_entrance(-1), light], 6)
play sfx2 "fight_6010.ogg"
get_char('c2403') '[convertstrid(1151995)]' (**arg(23, 1151995)) with shake
$ update_portrait('st041_01 2', 'p240', [r(-1), light], 6)
get_char('c2403') '[convertstrid(1151996)]' (**arg(24, 1151996))
$ update_portrait('st041_01 2', 'p240', [r(-1), dark], 5)
$ update_portrait('st050_01 3', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151997)]' (**arg(25, 1151997))
$ update_portrait('st050_01 3', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151998)]' (**arg(26, 1151998))
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151999)]' (**arg(27, 1151999))
hide p257
hide p240
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
$ update_narrator('c2571')
with fade
get_char('c2571') '[convertstrid(1152000)]' (**arg(28, 1152000))
$ update_portrait('st050_01 1', 'p257', [l(-11), l_shake, light, flip], 6)
play sfx2 "other_7061.ogg"
get_char('c2571') '[convertstrid(1152001)]' (**arg(29, 1152001))
$ update_portrait('st050_01 5', 'p257', [l_midback(-11), light, flip], 6)
play sfx2 "other_7061.ogg"
get_char('c2571') '[convertstrid(1152002)]' (**arg(30, 1152002))
$ update_portrait('st050_01 5', 'p257', [l_midback(-11), light, flip], 6)
play sfx2 "other_7061.ogg"
get_char('c2571') '[convertstrid(1152003)]' (**arg(31, 1152003))
hide p257
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1152004)]' (**arg(32, 1152004))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('st041_01 5', 'p240', [l_entrance(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152005)]' (**arg(33, 1152005))
hide p3
$ update_portrait('st041_01 5', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152006)]' (**arg(34, 1152006))
hide p240
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152007)]' (**arg(35, 1152007))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152008)]' (**arg(36, 1152008))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c21') '[convertstrid(1152009)]' (**arg(37, 1152009))
hide p2
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152010)]' (**arg(38, 1152010))
hide p4
$ update_portrait('st041_01 1', 'p240', [l_entrance(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152011)]' (**arg(39, 1152011))
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152012)]' (**arg(40, 1152012))
$ update_portrait('st041_01 5', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152013)]' (**arg(41, 1152013))
hide p1
$ update_portrait('st041_01 5', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152014)]' (**arg(42, 1152014))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152015)]' (**arg(43, 1152015))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7017.ogg"
get_char('c13') '[convertstrid(1152016)]' (**arg(44, 1152016))
hide p240
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152017)]' (**arg(45, 1152017))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152018)]' (**arg(46, 1152018))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152019)]' (**arg(47, 1152019))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152020)]' (**arg(48, 1152020))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152021)]' (**arg(49, 1152021))
hide p4
hide p1
$ update_narrator('c12311')
with fade
get_char('c12311') '[convertstrid(1152022)]' (**arg(50, 1152022))
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152023)]' (**arg(51, 1152023))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
get_char('c12311') '[convertstrid(1152024)]' (**arg(52, 1152024))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152025)]' (**arg(53, 1152025))
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152026)]' (**arg(54, 1152026))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1152027)]' (**arg(55, 1152027))
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152028)]' (**arg(56, 1152028))
hide p240
hide p3
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
$ update_narrator('c2571')
with fade
play sfx2 "other_7061.ogg"
get_char('c2571') '[convertstrid(1152029)]' (**arg(57, 1152029))
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1152030)]' (**arg(58, 1152030))
hide p257
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('st041_01 2', 'p240', [l_exit(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152031)]' (**arg(59, 1152031))
hide p240
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152032)]' (**arg(60, 1152032))
return