label avg10567(trans=fade_in):

$ play_music("ed7564.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1154422)]' (**arg(1, 1154422))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154423)]' (**arg(2, 1154423))
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c33') '[convertstrid(1154424)]' (**arg(3, 1154424))
hide p3
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1154425)]' (**arg(4, 1154425))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154426)]' (**arg(5, 1154426))
hide p16
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154427)]' (**arg(6, 1154427))
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154428)]' (**arg(7, 1154428))
hide p2
$ update_portrait('oc008_01 2', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1154429)]' (**arg(8, 1154429))
hide p3
$ update_portrait('sc008_01 2', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1154430)]' (**arg(9, 1154430))
$ update_portrait('sc008_01 2', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154431)]' (**arg(10, 1154431))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154432)]' (**arg(11, 1154432))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154433)]' (**arg(12, 1154433))
hide p16
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154434)]' (**arg(13, 1154434))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_ai07.ogg"
get_char('c81') '[convertstrid(1154435)]' (**arg(14, 1154435))
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154436)]' (**arg(15, 1154436))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154437)]' (**arg(16, 1154437))
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154438)]' (**arg(17, 1154438))
$ update_portrait('oc008_01 6', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154439)]' (**arg(18, 1154439))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1154440)]' (**arg(19, 1154440))
hide p1
$ update_portrait('oc004_01 13', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li26.ogg"
get_char('c43') '[convertstrid(1154441)]' (**arg(20, 1154441))
hide p4
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1154442)]' (**arg(21, 1154442))
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
$ update_portrait('oc008_01 6', 'p8', [l_midback(-5), light, flip], 6)
play sfx2 "other_7088.ogg"
get_char('c81') '[convertstrid(1154443)]' (**arg(22, 1154443))
hide p8
hide p3
get_char('c0') '[convertstrid(1154444)]' (**arg(23, 1154444))
$ update_portrait('st056_01 2', 'p1212', [l(-6), light, flip], 6)
get_char('c12121') '[convertstrid(1154445)]' (**arg(24, 1154445))
$ update_portrait('st056_01 2', 'p1212', [l(-6), dark, flip], 5)
$ update_portrait('sc008_01 2', 'p16', [r(-18), r_shake, light], 6)
get_char('c163') '[convertstrid(1154446)]' (**arg(25, 1154446))
hide p1212
$ update_portrait('sc008_01 2', 'p16', [r(-18), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1154447)]' (**arg(26, 1154447))
hide p16
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 6)
play sfxvoice "avg_vocal_li11.ogg"
get_char('c43') '[convertstrid(1154448)]' (**arg(27, 1154448))
hide p4
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154449)]' (**arg(28, 1154449))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154450)]' (**arg(29, 1154450))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154451)]' (**arg(30, 1154451))
hide p3
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154452)]' (**arg(31, 1154452))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154453)]' (**arg(32, 1154453))
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154454)]' (**arg(33, 1154454))
hide p1
$ update_portrait('oc008_01 4', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('st056_01 2', 'p1212', [r(-6), light], 6)
get_char('c12123') '[convertstrid(1154455)]' (**arg(34, 1154455))
$ update_portrait('st056_01 2', 'p1212', [r(-6), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154456)]' (**arg(35, 1154456))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154457)]' (**arg(36, 1154457))
hide p1212
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154458)]' (**arg(37, 1154458))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1154459)]' (**arg(38, 1154459))
hide p8
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1154460)]' (**arg(39, 1154460))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154461)]' (**arg(40, 1154461))
hide p3
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154462)]' (**arg(41, 1154462))
hide p4
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154463)]' (**arg(42, 1154463))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154464)]' (**arg(43, 1154464))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154465)]' (**arg(44, 1154465))
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1154466)]' (**arg(45, 1154466))
hide p16
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1154467)]' (**arg(46, 1154467))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154468)]' (**arg(47, 1154468))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1154469)]' (**arg(48, 1154469))
hide p1
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154470)]' (**arg(49, 1154470))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154471)]' (**arg(50, 1154471))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154472)]' (**arg(51, 1154472))
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154473)]' (**arg(52, 1154473))
hide p4
$ update_portrait('oc008_01 6', 'p8', [l_entrance(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154474)]' (**arg(53, 1154474))
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154475)]' (**arg(54, 1154475))
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154476)]' (**arg(55, 1154476))
$ update_portrait('oc008_01 6', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154477)]' (**arg(56, 1154477))
hide p8
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154478)]' (**arg(57, 1154478))
hide p4
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154479)]' (**arg(58, 1154479))
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154480)]' (**arg(59, 1154480))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154481)]' (**arg(60, 1154481))
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154482)]' (**arg(61, 1154482))
hide p8
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154483)]' (**arg(62, 1154483))
hide p4
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
get_char('c31') '[convertstrid(1154484)]' (**arg(63, 1154484))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154485)]' (**arg(64, 1154485))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154486)]' (**arg(65, 1154486))
hide p4
$ update_portrait('oc008_01 5', 'p8', [l_entrance(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154487)]' (**arg(66, 1154487))
hide p2
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1154488)]' (**arg(67, 1154488))
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154489)]' (**arg(68, 1154489))
$ update_portrait('oc008_01 4', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1154490)]' (**arg(69, 1154490))
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154491)]' (**arg(70, 1154491))
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154492)]' (**arg(71, 1154492))
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154493)]' (**arg(72, 1154493))
stop music
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154494)]' (**arg(73, 1154494))
hide p16
$ update_portrait('oc008_01 6', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154495)]' (**arg(74, 1154495))
hide p2
$ update_portrait('oc001_01 13', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1154496)]' (**arg(75, 1154496))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154497)]' (**arg(76, 1154497))
$ play_music("ed7564.ogg")
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 6', 'p8', [l(-5), l_shake, light, flip], 6)
get_char('c81') '[convertstrid(1154498)]' (**arg(77, 1154498))
hide p1
$ update_portrait('oc008_01 6', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1154499)]' (**arg(78, 1154499))
hide p4
$ update_portrait('oc001_01 13', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1154500)]' (**arg(79, 1154500))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1154501)]' (**arg(80, 1154501))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154502)]' (**arg(81, 1154502))
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154503)]' (**arg(82, 1154503))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154504)]' (**arg(83, 1154504))
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154505)]' (**arg(84, 1154505))
hide p4
$ update_portrait('oc008_01 6', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154506)]' (**arg(85, 1154506))
$ update_portrait('oc002_01 20', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1154507)]' (**arg(86, 1154507)) with shake
hide p8
$ update_portrait('oc002_01 20', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154508)]' (**arg(87, 1154508))
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 3', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154509)]' (**arg(88, 1154509))
$ update_portrait('oc002_01 20', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch22.ogg"
get_char('c23') '[convertstrid(1154510)]' (**arg(89, 1154510))
hide p16
$ update_portrait('oc002_01 20', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154511)]' (**arg(90, 1154511))
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1154512)]' (**arg(91, 1154512))
hide p2
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1154513)]' (**arg(92, 1154513))
stop music
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "other_7007.ogg"
get_char('c13') '[convertstrid(1154514)]' (**arg(93, 1154514)) with shake
$ play_music("ed7580.ogg")
scene avg_bg_052
show memoryoverlay zorder 2
$ update_narrator('c10491')
with fade
get_char('c10491') '[convertstrid(1154515)]' (**arg(94, 1154515))
get_char('c5003') '[convertstrid(1154516)]' (**arg(95, 1154516))
get_char('c5003') '[convertstrid(1154517)]' (**arg(96, 1154517))
get_char('c10491') '[convertstrid(1154518)]' (**arg(97, 1154518))
get_char('c10491') '[convertstrid(1154519)]' (**arg(98, 1154519))
get_char('c5003') '[convertstrid(1154520)]' (**arg(99, 1154520))
get_char('c10491') '[convertstrid(1154521)]' (**arg(100, 1154521))
get_char('c5003') '[convertstrid(1154522)]' (**arg(101, 1154522))
get_char('c5003') '[convertstrid(1154523)]' (**arg(102, 1154523))
get_char('c5003') '[convertstrid(1154524)]' (**arg(103, 1154524))
$ play_music("ed7564.ogg")
scene placeholderbackground
$ update_narrator('c41')
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
with fade
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1154525)]' (**arg(104, 1154525))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 3', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1154526)]' (**arg(105, 1154526))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154527)]' (**arg(106, 1154527))
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1154528)]' (**arg(107, 1154528))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154529)]' (**arg(108, 1154529))
hide p2
hide p1
get_char('c0') '[convertstrid(1154530)]' (**arg(109, 1154530))
$ update_portrait('sc008_01 2', 'p16', [l(-18), light, flip], 6)
play sfx2 "other_7018.ogg"
get_char('c161') '[convertstrid(1154531)]' (**arg(110, 1154531))
$ update_portrait('sc008_01 2', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1154532)]' (**arg(111, 1154532))
hide p16
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro16.ogg"
get_char('c31') '[convertstrid(1154533)]' (**arg(112, 1154533))
hide p3
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154534)]' (**arg(113, 1154534))
hide p4
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r_entrance(-18), light], 6)
get_char('c163') '[convertstrid(1154535)]' (**arg(114, 1154535))
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154536)]' (**arg(115, 1154536))
hide p16
$ update_portrait('oc008_01 4', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('st057_01 4', 'p1211', [r(-16), light], 6)
get_char('c12113') '[convertstrid(1154537)]' (**arg(116, 1154537))
stop music
$ update_portrait('st057_01 2', 'p1211', [r(-16), light], 6)
play sfx2 "fight_6009.ogg"
get_char('c12113') '[convertstrid(1154538)]' (**arg(117, 1154538)) with shake
hide p1211
$ update_portrait('oc003_01 12', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1154539)]' (**arg(118, 1154539))
$ play_music("ed7571.ogg")
hide p8
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154540)]' (**arg(119, 1154540))
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1154541)]' (**arg(120, 1154541))
hide p4
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154542)]' (**arg(121, 1154542))
hide p16
hide p1
$ update_portrait('st056_01 1', 'p1212', [r(-6), light], 6)
$ update_narrator('c12123')
with fade
get_char('c12123') '[convertstrid(1154543)]' (**arg(122, 1154543))
$ update_portrait('st056_01 1', 'p1212', [r(-6), light], 6)
get_char('c12123') '[convertstrid(1154544)]' (**arg(123, 1154544))
$ update_portrait('st056_01 4', 'p1212', [r(-6), light], 6)
get_char('c12123') '[convertstrid(1154545)]' (**arg(124, 1154545))
$ update_portrait('st056_01 4', 'p1212', [r(-6), dark], 5)
$ update_portrait('st057_01 3', 'p1211', [l(-16), light, flip], 6)
get_char('c12111') '[convertstrid(1154546)]' (**arg(125, 1154546))
$ update_portrait('st057_01 3', 'p1211', [l(-16), dark, flip], 5)
$ update_portrait('st056_01 5', 'p1212', [r(-6), light], 6)
get_char('c12123') '[convertstrid(1154547)]' (**arg(126, 1154547))
hide p1212
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na09_b.ogg"
get_char('c13') '[convertstrid(1154548)]' (**arg(127, 1154548))
hide p1211
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154549)]' (**arg(128, 1154549))
hide p1
$ update_portrait('oc008_01 4', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('st056_01 1', 'p1212', [r(-6), light], 6)
get_char('c12123') '[convertstrid(1154550)]' (**arg(129, 1154550))
hide p1212
$ update_portrait('oc003_01 9', 'p3', [r_midback(-6), light], 6)
play sfx2 "other_7007.ogg"
get_char('c33') '[convertstrid(1154551)]' (**arg(130, 1154551))
hide p3
$ update_portrait('sc008_01 3', 'p16', [r_midback(-18), light], 6)
play sfx2 "fight_6003.ogg"
get_char('c163') '[convertstrid(1154552)]' (**arg(131, 1154552))
$ update_portrait('sc008_01 3', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154553)]' (**arg(132, 1154553))
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('sc008_01 3', 'p16', [r(-18), light], 6)
play sfx2 "other_7034.ogg"
get_char('c163') '[convertstrid(1154554)]' (**arg(133, 1154554))
$ update_portrait('sc008_01 3', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 6', 'p8', [l_exit(-5), light, flip], 6)
get_char('c81') '[convertstrid(1154555)]' (**arg(134, 1154555))
hide p8
hide p16
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1154556)]' (**arg(135, 1154556))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154557)]' (**arg(136, 1154557))
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1154558)]' (**arg(137, 1154558))
$ update_portrait('oc004_01 21', 'p4', [l_entrance(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(1154559)]' (**arg(138, 1154559))
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154560)]' (**arg(139, 1154560))
return "avg10567"