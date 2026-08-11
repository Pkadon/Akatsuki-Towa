label avg12342(trans=fade_in):

$ play_music("ed7120.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7021.ogg"
get_char('c0') '[convertstrid(1133506)]' (**arg(1, 1133506))
scene avg_bg_055
$ update_portrait('st053_01 1', 'p1007', [l(-12), light, flip], 6)
$ update_narrator('c10071')
with fade
get_char('c10071') '[convertstrid(1133507)]' (**arg(2, 1133507))
$ update_portrait('st053_01 1', 'p1007', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133508)]' (**arg(3, 1133508))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st053_01 5', 'p1007', [l(-12), light, flip], 6)
get_char('c10071') '[convertstrid(1133509)]' (**arg(4, 1133509))
hide p1007
play sfx2 "other_7021.ogg"
get_char('c10901') '[convertstrid(1133510)]' (**arg(5, 1133510))
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133511)]' (**arg(6, 1133511))
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
get_char('c10911') '[convertstrid(1133512)]' (**arg(7, 1133512))
hide p1
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 6)
get_char('c10073') '[convertstrid(1133513)]' (**arg(8, 1133513))
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
get_char('c10901') '[convertstrid(1133514)]' (**arg(9, 1133514))
get_char('c10911') '[convertstrid(1133515)]' (**arg(10, 1133515))
hide p1007
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c33') '[convertstrid(1133516)]' (**arg(11, 1133516))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133517)]' (**arg(12, 1133517))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133518)]' (**arg(13, 1133518))
hide p2
get_char('c10901') '[convertstrid(1133519)]' (**arg(14, 1133519))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133520)]' (**arg(15, 1133520))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c10911') '[convertstrid(1133521)]' (**arg(16, 1133521))
get_char('c10911') '[convertstrid(1133522)]' (**arg(17, 1133522))
stop music
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
get_char('c21') '[convertstrid(1133523)]' (**arg(18, 1133523))
$ play_music("ed7151.ogg")
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133524)]' (**arg(19, 1133524))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133525)]' (**arg(20, 1133525))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133526)]' (**arg(21, 1133526))
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c43') '[convertstrid(1133527)]' (**arg(22, 1133527))
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133528)]' (**arg(23, 1133528))
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133529)]' (**arg(24, 1133529))
$ update_portrait('oc004_01 5', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133530)]' (**arg(25, 1133530))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li30.ogg"
get_char('c43') '[convertstrid(1133531)]' (**arg(26, 1133531))
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_midback(-3), light, flip], 6)
play sfx2 "fight_6010.ogg"
get_char('c21') '[convertstrid(1133532)]' (**arg(27, 1133532, size=(1.4)))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 19', 'p4', [r(-5), light], 6)
play sfx2 "other_7057.ogg"
play sfxvoice "bcv_oc004_hurt_02.ogg"
get_char('c43') '[convertstrid(1133533)]' (**arg(28, 1133533, size=(1.2))) with shake
$ update_portrait('oc004_01 21', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c43') '[convertstrid(1133534)]' (**arg(29, 1133534))
$ update_portrait('oc004_01 21', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133535)]' (**arg(30, 1133535))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1133536)]' (**arg(31, 1133536))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133537)]' (**arg(32, 1133537))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133538)]' (**arg(33, 1133538))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133539)]' (**arg(34, 1133539))
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133540)]' (**arg(35, 1133540))
stop music
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7077.ogg"
get_char('c13') '[convertstrid(1133541)]' (**arg(36, 1133541))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1133542)]' (**arg(37, 1133542))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133543)]' (**arg(38, 1133543))
hide p3
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133544)]' (**arg(39, 1133544))
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133545)]' (**arg(40, 1133545))
$ play_music("ed7511.ogg")
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7080.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1133546)]' (**arg(41, 1133546))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 21', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133547)]' (**arg(42, 1133547))
hide p3
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133548)]' (**arg(43, 1133548))
hide p1
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1133549)]' (**arg(44, 1133549))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133550)]' (**arg(45, 1133550))
return "avg12342"