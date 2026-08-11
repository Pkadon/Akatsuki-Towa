label avg10508(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_079
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150419)]' (**arg(1, 1150419))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c21') '[convertstrid(1150420)]' (**arg(2, 1150420))
hide p2
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150421)]' (**arg(3, 1150421))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1150422)]' (**arg(4, 1150422))
hide p3
hide p1
$ update_narrator('c2393')
with fade
$ update_portrait('st040_01 1', 'p239', [r_entrance(-19), light], 6)
get_char('c2393') '[convertstrid(1150423)]' (**arg(5, 1150423))
$ update_portrait('st040_01 1', 'p239', [r(-19), dark], 5)
get_char('c12031') '[convertstrid(1150424)]' (**arg(6, 1150424))
$ update_portrait('oc007_01 1', 'p7', [l_entrance(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150425)]' (**arg(7, 1150425))
hide p239
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150426)]' (**arg(8, 1150426))
hide p15
$ update_portrait('st040_01 2', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1150427)]' (**arg(9, 1150427))
$ update_portrait('st040_01 2', 'p239', [r(-19), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ar06.ogg"
get_char('c71') '[convertstrid(1150428)]' (**arg(10, 1150428))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150429)]' (**arg(11, 1150429))
hide p239
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150430)]' (**arg(12, 1150430))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150431)]' (**arg(13, 1150431))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150432)]' (**arg(14, 1150432))
$ update_portrait('oc007_01 1', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150433)]' (**arg(15, 1150433))
hide p1
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), r_shake, light], 6)
get_char('c153') '[convertstrid(1150434)]' (**arg(16, 1150434))
hide p15
$ update_portrait('st040_01 4', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1150435)]' (**arg(17, 1150435))
$ update_portrait('st040_01 4', 'p239', [r(-19), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150436)]' (**arg(18, 1150436))
hide p239
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1150437)]' (**arg(19, 1150437))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150438)]' (**arg(20, 1150438))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150439)]' (**arg(21, 1150439))
hide p7
get_char('c12031') '[convertstrid(1150440)]' (**arg(22, 1150440))
hide p3
$ update_portrait('oc007_01 2', 'p7', [r(-24), r_shake, light], 6)
get_char('c73') '[convertstrid(1150441)]' (**arg(23, 1150441))
$ update_portrait('oc007_01 2', 'p7', [r(-24), dark], 5)
get_char('c12031') '[convertstrid(1150442)]' (**arg(24, 1150442))
get_char('c12031') '[convertstrid(1150443)]' (**arg(25, 1150443))
get_char('c12031') '[convertstrid(1150444)]' (**arg(26, 1150444))
hide p7
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
$ update_narrator('c71')
with fade
play sfxvoice "avg_vocal_ar03.ogg"
get_char('c71') '[convertstrid(1150445)]' (**arg(27, 1150445))
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150446)]' (**arg(28, 1150446))
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150447)]' (**arg(29, 1150447))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150448)]' (**arg(30, 1150448))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc007_01 3', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150449)]' (**arg(31, 1150449))
hide p1
$ update_portrait('oc007_01 3', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('st040_01 1', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1150450)]' (**arg(32, 1150450))
$ update_portrait('st040_01 1', 'p239', [r(-19), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150451)]' (**arg(33, 1150451))
hide p239
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150452)]' (**arg(34, 1150452))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150453)]' (**arg(35, 1150453))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150454)]' (**arg(36, 1150454))
$ update_portrait('oc007_01 1', 'p7', [l(-24), light, flip], 6)
get_char('c71') '[convertstrid(1150455)]' (**arg(37, 1150455))
$ update_portrait('oc007_01 1', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c43') '[convertstrid(1150456)]' (**arg(38, 1150456))
hide p7
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150457)]' (**arg(39, 1150457))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150458)]' (**arg(40, 1150458))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150459)]' (**arg(41, 1150459))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150460)]' (**arg(42, 1150460))
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1150461)]' (**arg(43, 1150461))
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc007_01 2', 'p7', [l(-24), l_shake, light, flip], 6)
get_char('c71') '[convertstrid(1150462)]' (**arg(44, 1150462))
hide p4
$ update_portrait('oc007_01 2', 'p7', [l(-24), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150463)]' (**arg(45, 1150463))
hide p7
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150464)]' (**arg(46, 1150464))
hide p1
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150465)]' (**arg(47, 1150465))
stop music
hide p239
hide p15
play sfx2 "fight_6015.ogg"
get_char('c0') '[convertstrid(1150466)]' (**arg(48, 1150466)) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6016.ogg"
get_char('c13') '[convertstrid(1150467)]' (**arg(49, 1150467))
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150468)]' (**arg(50, 1150468))
hide p3
get_char('c12031') '[convertstrid(1150469)]' (**arg(51, 1150469))
hide p1
get_char('c12043') '[convertstrid(1150470)]' (**arg(52, 1150470))
get_char('c12031') '[convertstrid(1150471)]' (**arg(53, 1150471))
get_char('c12043') '[convertstrid(1150472)]' (**arg(54, 1150472))
get_char('c12043') '[convertstrid(1150473)]' (**arg(55, 1150473))
$ update_portrait('st040_01 4', 'p239', [r_entrance(-19), light], 6)
get_char('c2393') '[convertstrid(1150474)]' (**arg(56, 1150474))
$ update_portrait('st040_01 4', 'p239', [r(-19), dark], 5)
get_char('c12041') '[convertstrid(1150475)]' (**arg(57, 1150475))
hide p239
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150476)]' (**arg(58, 1150476))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 4', 'p239', [l_entrance(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1150477)]' (**arg(59, 1150477))
hide p239
get_char('c12031') '[convertstrid(1150478)]' (**arg(60, 1150478))
get_char('c12031') '[convertstrid(1150479)]' (**arg(61, 1150479))
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150480)]' (**arg(62, 1150480))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c41') '[convertstrid(1150481)]' (**arg(63, 1150481))
return "avg10508"