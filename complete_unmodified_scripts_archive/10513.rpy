label avg10513:

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c12021')
window show
with fade_in
play sfx2 "other_7047.ogg"
get_char('c12021') '[convertstrid(1150533)]' (**arg(1, 1150533))
get_char('c12021') '[convertstrid(1150534)]' (**arg(2, 1150534))
$ update_portrait('oc007_01 1', 'p7', [r_entrance(-24), light], 6)
play sfxvoice "avg_vocal_ar05.ogg"
get_char('c73') '[convertstrid(1150535)]' (**arg(3, 1150535))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150536)]' (**arg(4, 1150536))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150537)]' (**arg(5, 1150537))
hide p7
$ update_portrait('st040_01 3', 'p239', [r_entrance(-19), light], 6)
get_char('c2393') '[convertstrid(1150538)]' (**arg(6, 1150538))
$ update_portrait('st040_01 3', 'p239', [r(-19), dark], 5)
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1150539)]' (**arg(7, 1150539)) with shake
hide p239
$ update_portrait('st041_01 4', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), r_shake, light], 6)
get_char('c73') '[convertstrid(1150540)]' (**arg(8, 1150540))
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('st041_01 4', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1150541)]' (**arg(9, 1150541))
hide p240
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1150542)]' (**arg(10, 1150542))
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150543)]' (**arg(11, 1150543))
hide p7
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150544)]' (**arg(12, 1150544))
hide p257
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c12021') '[convertstrid(1150545)]' (**arg(13, 1150545))
get_char('c12021') '[convertstrid(1150546)]' (**arg(14, 1150546))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150547)]' (**arg(15, 1150547))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st041_01 5', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1150548)]' (**arg(16, 1150548))
hide p1
$ update_portrait('st041_01 5', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150549)]' (**arg(17, 1150549))
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('st041_01 5', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1150550)]' (**arg(18, 1150550))
$ update_portrait('st041_01 5', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc007_01 5', 'p7', [r(-24), r_shake, light], 6)
get_char('c73') '[convertstrid(1150551)]' (**arg(19, 1150551))
hide p240
$ update_portrait('oc007_01 5', 'p7', [r(-24), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1150552)]' (**arg(20, 1150552))
hide p257
$ update_portrait('st041_01 2', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1150553)]' (**arg(21, 1150553))
hide p7
$ update_portrait('st041_01 2', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150554)]' (**arg(22, 1150554))
hide p240
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li15.ogg"
get_char('c41') '[convertstrid(1150555)]' (**arg(23, 1150555))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150556)]' (**arg(24, 1150556))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150557)]' (**arg(25, 1150557))
hide p3
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
get_char('c12021') '[convertstrid(1150558)]' (**arg(26, 1150558))
hide p15
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150559)]' (**arg(27, 1150559))
hide p1
$ update_portrait('oc007_01 1', 'p7', [r(-24), r_shake, light], 6)
get_char('c73') '[convertstrid(1150560)]' (**arg(28, 1150560))
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('st041_01 2', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1150561)]' (**arg(29, 1150561))
$ update_portrait('st041_01 2', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150562)]' (**arg(30, 1150562))
hide p7
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150563)]' (**arg(31, 1150563))
hide p240
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c12021') '[convertstrid(1150564)]' (**arg(32, 1150564))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1150565)]' (**arg(33, 1150565))
hide p4
get_char('c12021') '[convertstrid(1150566)]' (**arg(34, 1150566))
get_char('c12021') '[convertstrid(1150567)]' (**arg(35, 1150567))
get_char('c12021') '[convertstrid(1150568)]' (**arg(36, 1150568))
hide p3
$ update_portrait('oc007_01 1', 'p7', [r(-24), r_shake, light], 6)
get_char('c73') '[convertstrid(1150569)]' (**arg(37, 1150569))
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150570)]' (**arg(38, 1150570))
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150571)]' (**arg(39, 1150571))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li28.ogg"
get_char('c41') '[convertstrid(1150572)]' (**arg(40, 1150572))
hide p7
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st041_01 2', 'p240', [r(-1), r_shake, light], 6)
get_char('c2403') '[convertstrid(1150573)]' (**arg(41, 1150573))
hide p4
$ update_portrait('st041_01 2', 'p240', [r(-1), dark], 5)
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1150574)]' (**arg(42, 1150574))
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1150575)]' (**arg(43, 1150575))
hide p240
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150576)]' (**arg(44, 1150576))
hide p257
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('st041_01 3', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1150577)]' (**arg(45, 1150577))
hide p7
$ update_portrait('st041_01 3', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150578)]' (**arg(46, 1150578))
hide p240
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1150579)]' (**arg(47, 1150579))
hide p2
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150580)]' (**arg(48, 1150580))
hide p1
$ update_portrait('sc005_01 4', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('st041_01 2', 'p240', [r(-1), r_shake, light], 6)
get_char('c2403') '[convertstrid(1150581)]' (**arg(49, 1150581))
$ update_portrait('st041_01 1', 'p240', [r(-1), light], 6)
get_char('c2403') '[convertstrid(1150582)]' (**arg(50, 1150582))
hide p240
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150583)]' (**arg(51, 1150583))
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150584)]' (**arg(52, 1150584))
$ update_portrait('sc005_01 4', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150585)]' (**arg(53, 1150585))
hide p7
$ update_portrait('sc005_01 4', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('st041_01 2', 'p240', [r(-1), r_shake, light], 6)
get_char('c2403') '[convertstrid(1150586)]' (**arg(54, 1150586))
$ update_portrait('st041_01 2', 'p240', [r(-1), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150587)]' (**arg(55, 1150587))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150588)]' (**arg(56, 1150588))
hide p240
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1150589)]' (**arg(57, 1150589))
hide p15
$ update_portrait('oc007_01 1', 'p7', [r(-24), light], 6)
get_char('c73') '[convertstrid(1150590)]' (**arg(58, 1150590))
hide p13
$ update_portrait('oc007_01 1', 'p7', [r(-24), dark], 5)
$ update_portrait('st050_01 2', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1150591)]' (**arg(59, 1150591))
hide p7
$ update_portrait('st050_01 2', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('st041_01 4', 'p240', [r(-1), light], 6)
get_char('c2403') '[convertstrid(1150592)]' (**arg(60, 1150592))
$ update_portrait('st041_01 4', 'p240', [r(-1), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1150593)]' (**arg(61, 1150593))
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('st041_01 2', 'p240', [r(-1), light], 6)
get_char('c2403') '[convertstrid(1150594)]' (**arg(62, 1150594))
$ update_portrait('st041_01 4', 'p240', [r(-1), light], 6)
get_char('c2403') '[convertstrid(1150595)]' (**arg(63, 1150595))
hide p257
$ update_portrait('st041_01 4', 'p240', [r(-1), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150596)]' (**arg(64, 1150596))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1150597)]' (**arg(65, 1150597))
hide p13
hide p240
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1150598)]' (**arg(66, 1150598))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150599)]' (**arg(67, 1150599))
return