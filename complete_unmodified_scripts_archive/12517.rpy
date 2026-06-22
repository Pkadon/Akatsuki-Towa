label avg12517:

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1151129)]' (**arg(1, 1151129))
get_char('c12021') '[convertstrid(1151130)]' (**arg(2, 1151130))
get_char('c12021') '[convertstrid(1151131)]' (**arg(3, 1151131))
get_char('c12021') '[convertstrid(1151132)]' (**arg(4, 1151132))
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1151133)]' (**arg(5, 1151133))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151134)]' (**arg(6, 1151134))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151135)]' (**arg(7, 1151135))
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r_entrance(-5), light], 6)
get_char('c43') '[convertstrid(1151136)]' (**arg(8, 1151136))
hide p4
$ update_portrait('st040_01 1', 'p239', [r_entrance(-19), light], 6)
get_char('c2393') '[convertstrid(1151137)]' (**arg(9, 1151137))
$ update_portrait('st040_01 1', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1151138)]' (**arg(10, 1151138))
hide p3
$ update_portrait('st040_01 1', 'p239', [r(-19), dark], 5)
get_char('c12021') '[convertstrid(1151139)]' (**arg(11, 1151139))
hide p239
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1151140)]' (**arg(12, 1151140))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro11.ogg"
get_char('c31') '[convertstrid(1151141)]' (**arg(13, 1151141))
hide p3
hide p1
$ update_narrator('c12021')
with fade
get_char('c12021') '[convertstrid(1151142)]' (**arg(14, 1151142))
get_char('c12021') '[convertstrid(1151143)]' (**arg(15, 1151143))
get_char('c12021') '[convertstrid(1151144)]' (**arg(16, 1151144))
get_char('c0') '[convertstrid(1151145)]' (**arg(17, 1151145))
get_char('c12021') '[convertstrid(1151146)]' (**arg(18, 1151146))
get_char('c12021') '[convertstrid(1151147)]' (**arg(19, 1151147))
get_char('c12021') '[convertstrid(1151148)]' (**arg(20, 1151148))
get_char('c12021') '[convertstrid(1151149)]' (**arg(21, 1151149))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151150)]' (**arg(22, 1151150))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151151)]' (**arg(23, 1151151))
hide p3
get_char('c12021') '[convertstrid(1151152)]' (**arg(24, 1151152))
hide p4
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151153)]' (**arg(25, 1151153))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151154)]' (**arg(26, 1151154))
hide p2
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151155)]' (**arg(27, 1151155))
hide p239
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1151156)]' (**arg(28, 1151156))
get_char('c12021') '[convertstrid(1151157)]' (**arg(29, 1151157))
get_char('c12021') '[convertstrid(1151158)]' (**arg(30, 1151158))
get_char('c12021') '[convertstrid(1151159)]' (**arg(31, 1151159))
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151160)]' (**arg(32, 1151160))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12021') '[convertstrid(1151161)]' (**arg(33, 1151161))
get_char('c12021') '[convertstrid(1151162)]' (**arg(34, 1151162))
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1151163)]' (**arg(35, 1151163))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1151164)]' (**arg(36, 1151164))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151165)]' (**arg(37, 1151165))
hide p1
$ update_portrait('st040_01 4', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1151166)]' (**arg(38, 1151166))
hide p2
$ update_portrait('st040_01 4', 'p239', [r(-19), dark], 5)
get_char('c12021') '[convertstrid(1151167)]' (**arg(39, 1151167))
$ update_portrait('st040_01 1', 'p239', [r(-19), light], 6)
get_char('c2393') '[convertstrid(1151168)]' (**arg(40, 1151168))
$ update_portrait('st040_01 1', 'p239', [r(-19), dark], 5)
get_char('c12021') '[convertstrid(1151169)]' (**arg(41, 1151169))
hide p239
play sfx2 "other_7047.ogg"
get_char('c12243') '[convertstrid(1151170)]' (**arg(42, 1151170))
get_char('c12021') '[convertstrid(1151171)]' (**arg(43, 1151171))
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c21') '[convertstrid(1151172)]' (**arg(44, 1151172))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc007_01 3', 'p15', [r_entrance(-17), light], 6)
get_char('c153') '[convertstrid(1151173)]' (**arg(45, 1151173))
hide p2
$ update_portrait('sc007_01 3', 'p15', [r(-17), dark], 5)
get_char('c12021') '[convertstrid(1151174)]' (**arg(46, 1151174))
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151175)]' (**arg(47, 1151175))
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151176)]' (**arg(48, 1151176))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151177)]' (**arg(49, 1151177))
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151178)]' (**arg(50, 1151178))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151179)]' (**arg(51, 1151179))
hide p239
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1151180)]' (**arg(52, 1151180))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151181)]' (**arg(53, 1151181))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151182)]' (**arg(54, 1151182))
hide p3
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151183)]' (**arg(55, 1151183))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151184)]' (**arg(56, 1151184))
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 3', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151185)]' (**arg(57, 1151185))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151186)]' (**arg(58, 1151186))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151187)]' (**arg(59, 1151187))
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151188)]' (**arg(60, 1151188))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151189)]' (**arg(61, 1151189))
hide p239
hide p15
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1151190)]' (**arg(62, 1151190))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151191)]' (**arg(63, 1151191))
hide p3
hide p4
$ update_narrator('c151')
with fade
$ update_portrait('sc007_01 1', 'p15', [l_entrance(-17), light, flip], 6)
get_char('c151') '[convertstrid(1151192)]' (**arg(64, 1151192))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151193)]' (**arg(65, 1151193))
hide p15
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151194)]' (**arg(66, 1151194))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1151195)]' (**arg(67, 1151195))
hide p1
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151196)]' (**arg(68, 1151196))
hide p239
hide p15
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151197)]' (**arg(69, 1151197))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151198)]' (**arg(70, 1151198))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151199)]' (**arg(71, 1151199))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151200)]' (**arg(72, 1151200))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1151201)]' (**arg(73, 1151201))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151202)]' (**arg(74, 1151202))
hide p2
play sfx2 "other_7020.ogg"
get_char('c0') '[convertstrid(1151203)]' (**arg(75, 1151203))
$ update_portrait('sc005_01 1', 'p1217', [l_entrance(-17), light, flip], 6)
get_char('c12171') '[convertstrid(1151204)]' (**arg(76, 1151204))
$ update_portrait('sc005_01 1', 'p1217', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151205)]' (**arg(77, 1151205))
hide p1217
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151206)]' (**arg(78, 1151206))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151207)]' (**arg(79, 1151207))
hide p1
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151208)]' (**arg(80, 1151208))
hide p4
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1151209)]' (**arg(81, 1151209))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151210)]' (**arg(82, 1151210))
hide p13
get_char('c12021') '[convertstrid(1151211)]' (**arg(83, 1151211))
$ update_portrait('oc002_01 14', 'p2', [l_entrance(-3), r_shake, light, flip], 6)
get_char('c21') '[convertstrid(1151212)]' (**arg(84, 1151212))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151213)]' (**arg(85, 1151213))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151214)]' (**arg(86, 1151214))
hide p1
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151215)]' (**arg(87, 1151215))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1151216)]' (**arg(88, 1151216))
hide p13
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
get_char('c12021') '[convertstrid(1151217)]' (**arg(89, 1151217))
hide p1
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151218)]' (**arg(90, 1151218))
return