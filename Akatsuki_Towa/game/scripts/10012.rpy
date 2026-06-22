label avg10012:

$ play_music("ed7151.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6022.ogg"
play sfxvoice "bcv_oc002_atk_03.ogg"
get_char('c23') '[convertstrid(1001089)]' (**arg(1, 1001089))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 10', 'p719', [l(-6), l_shake, light, flip], 6)
play sfxvoice "bcv_oc003_hurt_01.ogg"
get_char('c7191') '[convertstrid(1001090)]' (**arg(2, 1001090))
hide p2
$ update_portrait('oc003_01 10', 'p719', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001091)]' (**arg(3, 1001091))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001092)]' (**arg(4, 1001092))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001093)]' (**arg(5, 1001093))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001094)]' (**arg(6, 1001094))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p719', [l(-6), light, flip], 6)
get_char('c7191') '[convertstrid(1001095)]' (**arg(7, 1001095))
$ update_portrait('oc003_01 16', 'p719', [l(-6), light, flip], 6)
get_char('c7191') '[convertstrid(1001096)]' (**arg(8, 1001096))
$ update_portrait('oc003_01 16', 'p719', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1001097)]' (**arg(9, 1001097))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p719', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c7191') '[convertstrid(1001098)]' (**arg(10, 1001098))
$ update_portrait('oc003_01 12', 'p719', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6020.ogg"
get_char('c13') '[convertstrid(1001099)]' (**arg(11, 1001099))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p719', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c7191') '[convertstrid(1001100)]' (**arg(12, 1001100))
$ update_portrait('oc003_01 1', 'p719', [l(-6), light, flip], 6)
get_char('c7191') '[convertstrid(1001101)]' (**arg(13, 1001101))
$ update_portrait('oc003_01 1', 'p719', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001102)]' (**arg(14, 1001102))
hide p719
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro01.ogg"
get_char('c31') '[convertstrid(1001103)]' (**arg(15, 1001103))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1001104)]' (**arg(16, 1001104))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001105)]' (**arg(17, 1001105))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001106)]' (**arg(18, 1001106))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001107)]' (**arg(19, 1001107))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001108)]' (**arg(20, 1001108))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001109)]' (**arg(21, 1001109))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r_midback(-3), light], 6)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c23') '[convertstrid(1001110)]' (**arg(22, 1001110))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1001111)]' (**arg(23, 1001111))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1001112)]' (**arg(24, 1001112))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001113)]' (**arg(25, 1001113))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001114)]' (**arg(26, 1001114))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001115)]' (**arg(27, 1001115))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001116)]' (**arg(28, 1001116))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001117)]' (**arg(29, 1001117))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), l_shake, light, flip], 6)
get_char('c31') '[convertstrid(1001118)]' (**arg(30, 1001118))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001119)]' (**arg(31, 1001119))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001120)]' (**arg(32, 1001120))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001121)]' (**arg(33, 1001121))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001122)]' (**arg(34, 1001122))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001123)]' (**arg(35, 1001123))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001124)]' (**arg(36, 1001124))
hide p2
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001125)]' (**arg(37, 1001125))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001126)]' (**arg(38, 1001126))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001127)]' (**arg(39, 1001127))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001128)]' (**arg(40, 1001128))
hide p1
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 11', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001129)]' (**arg(41, 1001129))
$ update_portrait('oc002_01 11', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001130)]' (**arg(42, 1001130))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro19.ogg"
get_char('c31') '[convertstrid(1001131)]' (**arg(43, 1001131))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1001132)]' (**arg(44, 1001132))
hide p3
hide p2
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
with fade
get_char('c11') '[convertstrid(1001133)]' (**arg(45, 1001133))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001134)]' (**arg(46, 1001134))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001135)]' (**arg(47, 1001135))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001136)]' (**arg(48, 1001136))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001137)]' (**arg(49, 1001137))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1001138)]' (**arg(50, 1001138))
show Image1 zorder 4
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1001139)]' (**arg(51, 1001139))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001140)]' (**arg(52, 1001140))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001141)]' (**arg(53, 1001141))
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001142)]' (**arg(54, 1001142))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001143)]' (**arg(55, 1001143))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfx2 "other_7075.ogg"
get_char('c23') '[convertstrid(1001144)]' (**arg(56, 1001144))
hide p1
hide p2
play sfx2 "other_7071.ogg"
get_char('c0') '[convertstrid(1001145)]' (**arg(57, 1001145))
hide Image1
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "other_7073.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1001146)]' (**arg(58, 1001146))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001147)]' (**arg(59, 1001147))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001148)]' (**arg(60, 1001148))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001149)]' (**arg(61, 1001149))
hide p2
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001150)]' (**arg(62, 1001150))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001151)]' (**arg(63, 1001151))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001152)]' (**arg(64, 1001152))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001153)]' (**arg(65, 1001153))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001154)]' (**arg(66, 1001154))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001155)]' (**arg(67, 1001155))
$ play_music("ED6518.ogg")
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1001156)]' (**arg(68, 1001156))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001157)]' (**arg(69, 1001157))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001158)]' (**arg(70, 1001158))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001159)]' (**arg(71, 1001159))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001160)]' (**arg(72, 1001160))
hide p2
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001161)]' (**arg(73, 1001161))
$ update_portrait('oc003_01 14', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001162)]' (**arg(74, 1001162))
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001163)]' (**arg(75, 1001163))
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001164)]' (**arg(76, 1001164))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001165)]' (**arg(77, 1001165))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001166)]' (**arg(78, 1001166))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001167)]' (**arg(79, 1001167))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001168)]' (**arg(80, 1001168))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1001169)]' (**arg(81, 1001169))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c21') '[convertstrid(1001170)]' (**arg(82, 1001170))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001171)]' (**arg(83, 1001171))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001172)]' (**arg(84, 1001172))
return