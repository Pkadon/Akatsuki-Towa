label avg12614:

$ play_music("ed7150.ogg")
scene avg_bg_015
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1161507)]' (**arg(1, 1161507))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161508)]' (**arg(2, 1161508))
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7087.ogg"
get_char('c41') '[convertstrid(1161509)]' (**arg(3, 1161509)) with shake
hide p1
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161510)]' (**arg(4, 1161510))
hide p4
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161511)]' (**arg(5, 1161511))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161512)]' (**arg(6, 1161512))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161513)]' (**arg(7, 1161513))
hide p1312
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161514)]' (**arg(8, 1161514))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161515)]' (**arg(9, 1161515))
hide p2
hide p1
get_char('c0') '[convertstrid(1161516)]' (**arg(10, 1161516))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161517)]' (**arg(11, 1161517))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161518)]' (**arg(12, 1161518))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161519)]' (**arg(13, 1161519))
hide p2
$ update_portrait('sc029_01 2', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161520)]' (**arg(14, 1161520))
hide p4
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161521)]' (**arg(15, 1161521))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc029_01 5', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161522)]' (**arg(16, 1161522))
hide p1312
hide p3
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
$ update_narrator('c13121')
with fade
get_char('c13121') '[convertstrid(1161523)]' (**arg(17, 1161523))
hide p1312
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1161524)]' (**arg(18, 1161524))
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161525)]' (**arg(19, 1161525))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161526)]' (**arg(20, 1161526))
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161527)]' (**arg(21, 1161527))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161528)]' (**arg(22, 1161528))
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161529)]' (**arg(23, 1161529))
hide p2
$ update_portrait('sc029_01 2', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161530)]' (**arg(24, 1161530))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161531)]' (**arg(25, 1161531))
hide p3
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161532)]' (**arg(26, 1161532))
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161533)]' (**arg(27, 1161533))
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161534)]' (**arg(28, 1161534))
hide p3
$ update_portrait('sc029_01 2', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161535)]' (**arg(29, 1161535))
hide p1312
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161536)]' (**arg(30, 1161536))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161537)]' (**arg(31, 1161537))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161538)]' (**arg(32, 1161538))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161539)]' (**arg(33, 1161539))
$ update_portrait('sc029_01 5', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161540)]' (**arg(34, 1161540))
$ update_portrait('sc029_01 5', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161541)]' (**arg(35, 1161541))
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161542)]' (**arg(36, 1161542))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161543)]' (**arg(37, 1161543))
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161544)]' (**arg(38, 1161544))
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161545)]' (**arg(39, 1161545))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 5', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161546)]' (**arg(40, 1161546))
hide p2
$ update_portrait('sc029_01 5', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161547)]' (**arg(41, 1161547))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161548)]' (**arg(42, 1161548))
hide p3
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161549)]' (**arg(43, 1161549))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161550)]' (**arg(44, 1161550))
hide p2
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161551)]' (**arg(45, 1161551))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161552)]' (**arg(46, 1161552))
hide p1
$ update_portrait('sc029_01 2', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161553)]' (**arg(47, 1161553))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161554)]' (**arg(48, 1161554))
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161555)]' (**arg(49, 1161555))
hide p4
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161556)]' (**arg(50, 1161556))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161557)]' (**arg(51, 1161557))
$ update_portrait('sc029_01 2', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1161558)]' (**arg(52, 1161558))
hide p1312
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161559)]' (**arg(53, 1161559))
hide p2
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161560)]' (**arg(54, 1161560))
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161561)]' (**arg(55, 1161561))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('sc029_01 1', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161562)]' (**arg(56, 1161562))
$ update_portrait('sc029_01 1', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161563)]' (**arg(57, 1161563))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('sc029_01 2', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161564)]' (**arg(58, 1161564))
$ update_portrait('sc029_01 2', 'p1312', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1161565)]' (**arg(59, 1161565))
hide p1312
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1161566)]' (**arg(60, 1161566))
hide p4
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161567)]' (**arg(61, 1161567))
$ update_portrait('oc003_01 13', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 24', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161568)]' (**arg(62, 1161568))
hide p3
$ update_portrait('oc001_01 24', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1161569)]' (**arg(63, 1161569))
hide p2
$ update_portrait('sc029_01 6', 'p1312', [l(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161570)]' (**arg(64, 1161570))
$ update_portrait('sc029_01 5', 'p1312', [l_exit(-13), light, flip], 6)
get_char('c13121') '[convertstrid(1161571)]' (**arg(65, 1161571))
hide p1312
$ update_portrait('oc002_01 6', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161572)]' (**arg(66, 1161572))
hide p2
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1161573)]' (**arg(67, 1161573))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161574)]' (**arg(68, 1161574))
hide p2
$ update_portrait('oc004_01 17', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161575)]' (**arg(69, 1161575))
hide p4
$ update_portrait('oc003_01 13', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161576)]' (**arg(70, 1161576))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 15', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro05.ogg"
get_char('c31') '[convertstrid(1161577)]' (**arg(71, 1161577))
hide p1
$ update_portrait('oc003_01 15', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161578)]' (**arg(72, 1161578))
$ update_portrait('oc004_01 10', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161579)]' (**arg(73, 1161579))
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161580)]' (**arg(74, 1161580))
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161581)]' (**arg(75, 1161581))
hide p3
$ update_portrait('oc001_01 23', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1161582)]' (**arg(76, 1161582))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161583)]' (**arg(77, 1161583))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161584)]' (**arg(78, 1161584))
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 24', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1161585)]' (**arg(79, 1161585))
hide p4
$ update_portrait('oc001_01 24', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161586)]' (**arg(80, 1161586))
hide p3
$ update_portrait('oc004_01 14', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161587)]' (**arg(81, 1161587))
$ update_portrait('oc004_01 14', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161588)]' (**arg(82, 1161588))
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161589)]' (**arg(83, 1161589))
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1161590)]' (**arg(84, 1161590))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161591)]' (**arg(85, 1161591))
hide p4
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 6', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161592)]' (**arg(86, 1161592))
$ update_portrait('oc003_01 6', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 23', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1161593)]' (**arg(87, 1161593))
return