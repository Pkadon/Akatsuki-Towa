label avg1161(trans=fade_in):

$ play_music("ed7100.ogg")
scene avg_bg_070
$ update_narrator('c5001')
window show
with trans
play sfx2 "other_7060.ogg"
get_char('c5001') '[convertstrid(2104461)]' (**arg(1, 2104461))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
play sfx2 "other_7060.ogg"
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(2104462)]' (**arg(2, 2104462))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
play sfx2 "other_7060.ogg"
get_char('c5001') '[convertstrid(2104463)]' (**arg(3, 2104463))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104464)]' (**arg(4, 2104464))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
get_char('c5001') '[convertstrid(2104465)]' (**arg(5, 2104465)) with shake
scene avg_bg_038
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(2104466)]' (**arg(6, 2104466))
hide p1
get_char('c0') '[convertstrid(2104467)]' (**arg(7, 2104467))
$ update_portrait('oc002_01 22', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104468)]' (**arg(8, 2104468))
$ update_portrait('oc002_01 22', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104469)]' (**arg(9, 2104469))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104470)]' (**arg(10, 2104470))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104471)]' (**arg(11, 2104471))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104472)]' (**arg(12, 2104472))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104473)]' (**arg(13, 2104473))
hide p2
hide p1
get_char('c0') '[convertstrid(2104474)]' (**arg(14, 2104474))
$ update_portrait('oc002_01 21', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(2104475)]' (**arg(15, 2104475))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(2104476)]' (**arg(16, 2104476))
hide p2
hide p1
get_char('c0') '[convertstrid(2104477)]' (**arg(17, 2104477))
$ play_music("ed7150.ogg")
scene avg_bg_013
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2104478)]' (**arg(18, 2104478))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104479)]' (**arg(19, 2104479))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch29.ogg"
get_char('c21') '[convertstrid(2104480)]' (**arg(20, 2104480))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104481)]' (**arg(21, 2104481))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104482)]' (**arg(22, 2104482))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104483)]' (**arg(23, 2104483))
hide p2
hide p1
get_char('c0') '[convertstrid(2104484)]' (**arg(24, 2104484))
scene avg_bg_023
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(2104485)]' (**arg(25, 2104485))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(2104486)]' (**arg(26, 2104486))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104487)]' (**arg(27, 2104487))
hide p4
hide p3
get_char('c0') '[convertstrid(2104488)]' (**arg(28, 2104488))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104489)]' (**arg(29, 2104489))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104490)]' (**arg(30, 2104490))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104491)]' (**arg(31, 2104491))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104492)]' (**arg(32, 2104492))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104493)]' (**arg(33, 2104493))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104494)]' (**arg(34, 2104494))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104495)]' (**arg(35, 2104495))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104496)]' (**arg(36, 2104496))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104497)]' (**arg(37, 2104497))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104498)]' (**arg(38, 2104498))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 6)
get_char('c233') '[convertstrid(2104499)]' (**arg(39, 2104499))
hide p23
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2104500)]' (**arg(40, 2104500))
hide p56
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2104501)]' (**arg(41, 2104501))
hide p2
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104502)]' (**arg(42, 2104502))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2104503)]' (**arg(43, 2104503))
hide p23
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(2104504)]' (**arg(44, 2104504))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2104505)]' (**arg(45, 2104505))
$ update_portrait('sc015_01 3', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2104506)]' (**arg(46, 2104506))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2104507)]' (**arg(47, 2104507))
hide p23
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104508)]' (**arg(48, 2104508))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104509)]' (**arg(49, 2104509))
hide p56
get_char('c25311') '[convertstrid(2104510)]' (**arg(50, 2104510)) with shake
$ play_music("ed7516.ogg")
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2104511)]' (**arg(51, 2104511))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2104512)]' (**arg(52, 2104512))
hide p3
hide p4
get_char('c0') '[convertstrid(2104513)]' (**arg(53, 2104513))
get_char('c0') '[convertstrid(2104514)]' (**arg(54, 2104514))
get_char('c0') '[convertstrid(2104515)]' (**arg(55, 2104515))
get_char('c0') '[convertstrid(2104516)]' (**arg(56, 2104516))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104517)]' (**arg(57, 2104517))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104518)]' (**arg(58, 2104518))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(2104519)]' (**arg(59, 2104519))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104520)]' (**arg(60, 2104520))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104521)]' (**arg(61, 2104521))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104522)]' (**arg(62, 2104522))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l_exit(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104523)]' (**arg(63, 2104523))
hide p4
hide p1
play sfx2 "other_7085.ogg"
get_char('c0') '[convertstrid(2104524)]' (**arg(64, 2104524))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104525)]' (**arg(65, 2104525))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104526)]' (**arg(66, 2104526))
hide p2
hide p1
get_char('c0') '[convertstrid(2104527)]' (**arg(67, 2104527))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104528)]' (**arg(68, 2104528))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104529)]' (**arg(69, 2104529))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104530)]' (**arg(70, 2104530))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104531)]' (**arg(71, 2104531))
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104532)]' (**arg(72, 2104532))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104533)]' (**arg(73, 2104533))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104534)]' (**arg(74, 2104534))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104535)]' (**arg(75, 2104535))
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 6', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro05.ogg"
get_char('c33') '[convertstrid(2104536)]' (**arg(76, 2104536))
$ update_portrait('oc003_01 6', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(2104537)]' (**arg(77, 2104537))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(2104538)]' (**arg(78, 2104538))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104539)]' (**arg(79, 2104539))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104540)]' (**arg(80, 2104540))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104541)]' (**arg(81, 2104541))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104542)]' (**arg(82, 2104542))
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104543)]' (**arg(83, 2104543))
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104544)]' (**arg(84, 2104544))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104545)]' (**arg(85, 2104545))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104546)]' (**arg(86, 2104546))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(2104547)]' (**arg(87, 2104547))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2104548)]' (**arg(88, 2104548))
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104549)]' (**arg(89, 2104549))
$ play_music("ed7202.ogg")
scene avg_bg_036
$ update_narrator('c0')
with fade
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(2104550)]' (**arg(90, 2104550))
get_char('c0') '[convertstrid(2104551)]' (**arg(91, 2104551))
get_char('c0') '[convertstrid(2104552)]' (**arg(92, 2104552))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(2104553)]' (**arg(93, 2104553))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104554)]' (**arg(94, 2104554))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104555)]' (**arg(95, 2104555))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c33') '[convertstrid(2104556)]' (**arg(96, 2104556))
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104557)]' (**arg(97, 2104557))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104558)]' (**arg(98, 2104558))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104559)]' (**arg(99, 2104559))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104560)]' (**arg(100, 2104560))
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104561)]' (**arg(101, 2104561))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104562)]' (**arg(102, 2104562))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104563)]' (**arg(103, 2104563))
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104564)]' (**arg(104, 2104564))
$ play_music("ed7111.ogg")
scene avg_bg_054
$ update_narrator('c0')
with fade
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(2104565)]' (**arg(105, 2104565))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c41') '[convertstrid(2104566)]' (**arg(106, 2104566))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104567)]' (**arg(107, 2104567))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104568)]' (**arg(108, 2104568))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(2104569)]' (**arg(109, 2104569))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104570)]' (**arg(110, 2104570))
hide p2
hide p1
get_char('c0') '[convertstrid(2104571)]' (**arg(111, 2104571))
get_char('c0') '[convertstrid(2104572)]' (**arg(112, 2104572))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104573)]' (**arg(113, 2104573))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2104574)]' (**arg(114, 2104574))
hide p4
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104575)]' (**arg(115, 2104575))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(2104576)]' (**arg(116, 2104576))
hide p1
hide p2
get_char('c11551') '[convertstrid(2104577)]' (**arg(117, 2104577))
$ play_music("ed7511.ogg")
scene avg_bg_071
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2104578)]' (**arg(118, 2104578))
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2104579)]' (**arg(119, 2104579))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104580)]' (**arg(120, 2104580))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104581)]' (**arg(121, 2104581))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2104582)]' (**arg(122, 2104582))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na10_b.ogg"
get_char('c13') '[convertstrid(2104583)]' (**arg(123, 2104583))
hide p3
hide p1
get_char('c0') '[convertstrid(2104584)]' (**arg(124, 2104584))
get_char('c0') '[convertstrid(2104585)]' (**arg(125, 2104585))
get_char('c0') '[convertstrid(2104586)]' (**arg(126, 2104586))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104587)]' (**arg(127, 2104587))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104588)]' (**arg(128, 2104588))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6009.ogg"
play sfxvoice "avg_vocal_na12.ogg"
get_char('c13') '[convertstrid(2104589)]' (**arg(129, 2104589))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6017.ogg"
play sfxvoice "avg_vocal_ch26.ogg"
get_char('c21') '[convertstrid(2104590)]' (**arg(130, 2104590))
hide p2
hide p1
get_char('c0') '[convertstrid(2104591)]' (**arg(131, 2104591))
$ play_music("ed7300.ogg")
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104592)]' (**arg(132, 2104592))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104593)]' (**arg(133, 2104593))
hide p2
hide p1
get_char('c0') '[convertstrid(2104594)]' (**arg(134, 2104594))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104595)]' (**arg(135, 2104595))
hide p1
get_char('c0') '[convertstrid(2104596)]' (**arg(136, 2104596))
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2104597)]' (**arg(137, 2104597))
hide p3
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(2104598)]' (**arg(138, 2104598))
get_char('c0') '[convertstrid(2104599)]' (**arg(139, 2104599))
get_char('c0') '[convertstrid(2104600)]' (**arg(140, 2104600))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c31') '[convertstrid(2104601)]' (**arg(141, 2104601))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104602)]' (**arg(142, 2104602))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l_exit(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104603)]' (**arg(143, 2104603))
hide p2
hide p1
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2104604)]' (**arg(144, 2104604))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104605)]' (**arg(145, 2104605))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r_exit(-5), light], 6)
get_char('c43') '[convertstrid(2104606)]' (**arg(146, 2104606))
hide p4
hide p2
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(2104607)]' (**arg(147, 2104607))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2104608)]' (**arg(148, 2104608))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2104609)]' (**arg(149, 2104609))
$ play_music("ed7514.ogg")
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(2104610)]' (**arg(150, 2104610))
get_char('c0') '[convertstrid(2104611)]' (**arg(151, 2104611))
get_char('c0') '[convertstrid(2104612)]' (**arg(152, 2104612))
get_char('c0') '[convertstrid(2104613)]' (**arg(153, 2104613))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104614)]' (**arg(154, 2104614))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2104615)]' (**arg(155, 2104615))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2104616)]' (**arg(156, 2104616))
hide p56
hide p1
get_char('c0') '[convertstrid(2104617)]' (**arg(157, 2104617))
return "avg1161"