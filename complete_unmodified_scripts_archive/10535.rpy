label avg10535:

$ play_music("ED6102.ogg")
scene avg_bg_105
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1152500)]' (**arg(1, 1152500))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1152501)]' (**arg(2, 1152501))
hide p2
hide p1
$ update_narrator('c23')
with fade
$ update_portrait('oc002_01 1', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1152502)]' (**arg(3, 1152502))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c12361') '[convertstrid(1152503)]' (**arg(4, 1152503))
get_char('c12371') '[convertstrid(1152504)]' (**arg(5, 1152504))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152505)]' (**arg(6, 1152505))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152506)]' (**arg(7, 1152506))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12361') '[convertstrid(1152507)]' (**arg(8, 1152507))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152508)]' (**arg(9, 1152508))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12361') '[convertstrid(1152509)]' (**arg(10, 1152509))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152510)]' (**arg(11, 1152510))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12371') '[convertstrid(1152511)]' (**arg(12, 1152511))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152512)]' (**arg(13, 1152512))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12371') '[convertstrid(1152513)]' (**arg(14, 1152513))
get_char('c12371') '[convertstrid(1152514)]' (**arg(15, 1152514))
get_char('c12361') '[convertstrid(1152515)]' (**arg(16, 1152515))
hide p2
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152516)]' (**arg(17, 1152516))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
get_char('c12371') '[convertstrid(1152517)]' (**arg(18, 1152517))
get_char('c12361') '[convertstrid(1152518)]' (**arg(19, 1152518))
get_char('c12371') '[convertstrid(1152519)]' (**arg(20, 1152519))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152520)]' (**arg(21, 1152520))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c12371') '[convertstrid(1152521)]' (**arg(22, 1152521))
hide p1
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152522)]' (**arg(23, 1152522))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12361') '[convertstrid(1152523)]' (**arg(24, 1152523))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152524)]' (**arg(25, 1152524))
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
get_char('c12361') '[convertstrid(1152525)]' (**arg(26, 1152525))
get_char('c12371') '[convertstrid(1152526)]' (**arg(27, 1152526))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152527)]' (**arg(28, 1152527))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152528)]' (**arg(29, 1152528))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
get_char('c12361') '[convertstrid(1152529)]' (**arg(30, 1152529))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152530)]' (**arg(31, 1152530))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152531)]' (**arg(32, 1152531))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152532)]' (**arg(33, 1152532))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1152533)]' (**arg(34, 1152533))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152534)]' (**arg(35, 1152534))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152535)]' (**arg(36, 1152535))
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152536)]' (**arg(37, 1152536))
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152537)]' (**arg(38, 1152537))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152538)]' (**arg(39, 1152538))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152539)]' (**arg(40, 1152539))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152540)]' (**arg(41, 1152540))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152541)]' (**arg(42, 1152541))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1152542)]' (**arg(43, 1152542))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152543)]' (**arg(44, 1152543))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152544)]' (**arg(45, 1152544))
hide p4
hide p2
$ update_narrator('c291')
with fade
$ update_portrait('sc021_01 4', 'p29', [l_entrance(-17), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c291') '[convertstrid(1152545)]' (**arg(46, 1152545))
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1152546)]' (**arg(47, 1152546))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1152547)]' (**arg(48, 1152547))
hide p1
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152548)]' (**arg(49, 1152548))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1152549)]' (**arg(50, 1152549))
hide p2
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152550)]' (**arg(51, 1152550))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1152551)]' (**arg(52, 1152551))
hide p3
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152552)]' (**arg(53, 1152552))
hide p29
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1152553)]' (**arg(54, 1152553))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152554)]' (**arg(55, 1152554))
hide p2
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1152555)]' (**arg(56, 1152555))
hide p1
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152556)]' (**arg(57, 1152556))
hide p29
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152557)]' (**arg(58, 1152557))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152558)]' (**arg(59, 1152558))
return