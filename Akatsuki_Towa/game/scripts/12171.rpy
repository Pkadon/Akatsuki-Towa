label avg12171:

$ play_music("ED6505.ogg")
scene avg_bg_028
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7018.ogg"
get_char('c13') '[convertstrid(1128504)]' (**arg(1, 1128504))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128505)]' (**arg(2, 1128505))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128506)]' (**arg(3, 1128506))
get_char('c9651') '[convertstrid(1128507)]' (**arg(4, 1128507))
get_char('c9651') '[convertstrid(1128508)]' (**arg(5, 1128508))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfx2 "other_7004.ogg"
get_char('c13') '[convertstrid(1128509)]' (**arg(6, 1128509))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128510)]' (**arg(7, 1128510))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128511)]' (**arg(8, 1128511))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128512)]' (**arg(9, 1128512))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128513)]' (**arg(10, 1128513))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128514)]' (**arg(11, 1128514))
get_char('c9651') '[convertstrid(1128515)]' (**arg(12, 1128515))
hide p1
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128516)]' (**arg(13, 1128516))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
get_char('c9651') '[convertstrid(1128517)]' (**arg(14, 1128517))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128518)]' (**arg(15, 1128518))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c9651') '[convertstrid(1128519)]' (**arg(16, 1128519))
get_char('c9651') '[convertstrid(1128520)]' (**arg(17, 1128520))
get_char('c9651') '[convertstrid(1128521)]' (**arg(18, 1128521))
get_char('c9651') '[convertstrid(1128522)]' (**arg(19, 1128522))
get_char('c9651') '[convertstrid(1128523)]' (**arg(20, 1128523))
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1128526)]' (**arg(21, 1128526))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128527)]' (**arg(22, 1128527))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128528)]' (**arg(23, 1128528))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128529)]' (**arg(24, 1128529))
get_char('c9651') '[convertstrid(1128530)]' (**arg(25, 1128530))
play sfx2 "other_7008.ogg"
get_char('c9651') '[convertstrid(1128531)]' (**arg(26, 1128531))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128532)]' (**arg(27, 1128532))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1128533)]' (**arg(28, 1128533))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128534)]' (**arg(29, 1128534))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
play sfx2 "other_7034.ogg"
get_char('c5691') '[convertstrid(1128535)]' (**arg(30, 1128535))
$ play_music("ed7511.ogg")
play sfx2 "other_7066.ogg"
get_char('c5691') '[convertstrid(1128536)]' (**arg(31, 1128536, size=(1.2))) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1128537)]' (**arg(32, 1128537, size=(1.2)))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128538)]' (**arg(33, 1128538, size=(1.2)))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128539)]' (**arg(34, 1128539))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128540)]' (**arg(35, 1128540))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128541)]' (**arg(36, 1128541))
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1128542)]' (**arg(37, 1128542, size=(1.2)))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128543)]' (**arg(38, 1128543))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128544)]' (**arg(39, 1128544))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128545)]' (**arg(40, 1128545))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
get_char('c9651') '[convertstrid(1128546)]' (**arg(41, 1128546))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1128547)]' (**arg(42, 1128547))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c9651') '[convertstrid(1128548)]' (**arg(43, 1128548))
hide p2
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128549)]' (**arg(44, 1128549))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128550)]' (**arg(45, 1128550))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7028.ogg"
get_char('c31') '[convertstrid(1128551)]' (**arg(46, 1128551))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7029.ogg"
get_char('c13') '[convertstrid(1128552)]' (**arg(47, 1128552))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128553)]' (**arg(48, 1128553))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfx2 "common_sephi2.ogg"
get_char('c23') '[convertstrid(1128554)]' (**arg(49, 1128554))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l_midback(-6), light, flip], 6)
play sfx2 "common_sephi.ogg"
play sfxvoice "bcv_oc003_atk_01.ogg"
get_char('c31') '[convertstrid(1128555)]' (**arg(50, 1128555))
hide p2
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
play sfx2 "common_sephi2.ogg"
play sfxvoice "avg_vocal_li20.ogg"
get_char('c43') '[convertstrid(1128556)]' (**arg(51, 1128556))
hide p3
$ update_portrait('oc004_01 21', 'p4', [r(-5), dark], 5)
get_char('c9651') '[convertstrid(1128557)]' (**arg(52, 1128557))
hide p4
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128558)]' (**arg(53, 1128558))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128559)]' (**arg(54, 1128559))
return