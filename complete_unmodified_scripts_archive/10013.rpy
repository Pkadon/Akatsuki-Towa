label avg10013(trans=fade_in):

$ play_music("ED6517.ogg")
scene avg_bg_011
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
$ update_narrator('c213')
window show
with trans
get_char('c213') '[convertstrid(1001200)]' (**arg(1, 1001200))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001201)]' (**arg(2, 1001201))
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
$ update_portrait('uc002_03 1', 'p518', [l(-23), light, flip], 6)
get_char('c5181') '[convertstrid(1001202)]' (**arg(3, 1001202))
$ update_portrait('uc002_03 1', 'p518', [l(-23), dark, flip], 5)
$ update_portrait('sc013_01 5', 'p21', [r(-12), r_shake, light], 6)
get_char('c213') '[convertstrid(1001203)]' (**arg(4, 1001203))
$ update_portrait('sc013_01 5', 'p21', [r(-12), dark], 5)
$ update_portrait('uc002_03 1', 'p518', [l(-23), light, flip], 6)
get_char('c5181') '[convertstrid(1001204)]' (**arg(5, 1001204))
$ update_portrait('uc002_03 1', 'p518', [l(-23), dark, flip], 5)
$ update_portrait('sc013_01 5', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001205)]' (**arg(6, 1001205))
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001206)]' (**arg(7, 1001206))
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001207)]' (**arg(8, 1001207))
hide p518
$ update_portrait('sc013_01 1', 'p21', [r(-12), dark], 5)
$ update_portrait('uc002_03 1', 'p519', [l(-23), light, flip], 6)
get_char('c5191') '[convertstrid(1001208)]' (**arg(9, 1001208))
$ update_portrait('uc002_03 1', 'p519', [l(-23), light, flip], 6)
get_char('c5191') '[convertstrid(1001209)]' (**arg(10, 1001209))
$ update_portrait('uc002_03 1', 'p519', [l(-23), dark, flip], 5)
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001210)]' (**arg(11, 1001210))
hide p519
$ update_portrait('sc013_01 1', 'p21', [r(-12), dark], 5)
$ update_portrait('uc002_03 4', 'p520', [l(-23), light, flip], 6)
play sfx2 "other_7004.ogg"
get_char('c5201') '[convertstrid(1001211)]' (**arg(12, 1001211))
hide p520
get_char('c5271') '[convertstrid(1001212)]' (**arg(13, 1001212))
get_char('c5281') '[convertstrid(1001213)]' (**arg(14, 1001213))
$ update_portrait('sc013_01 5', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001214)]' (**arg(15, 1001214))
$ update_portrait('sc013_01 5', 'p21', [r(-12), dark], 5)
get_char('c5271') '[convertstrid(1001215)]' (**arg(16, 1001215))
$ update_portrait('uc002_03 1', 'p518', [l(-23), light, flip], 6)
get_char('c5181') '[convertstrid(1001216)]' (**arg(17, 1001216))
$ update_portrait('uc002_03 1', 'p518', [l(-23), light, flip], 6)
get_char('c5181') '[convertstrid(1001217)]' (**arg(18, 1001217))
$ update_portrait('uc002_03 1', 'p518', [l(-23), dark, flip], 5)
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
play sfx2 "other_7004.ogg"
get_char('c213') '[convertstrid(1001218)]' (**arg(19, 1001218))
$ play_music("ed7516.ogg")
hide p518
hide p21
$ update_narrator('c31')
with fade
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
play sfx2 "other_7045.ogg"
get_char('c31') '[convertstrid(1001219)]' (**arg(20, 1001219, size=(1.2)))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc013_01 2', 'p21', [r(-12), r_shake, light], 6)
play sfx2 "other_7020.ogg"
get_char('c213') '[convertstrid(1001220)]' (**arg(21, 1001220))
hide p3
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001221)]' (**arg(22, 1001221))
hide p2
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001222)]' (**arg(23, 1001222))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001223)]' (**arg(24, 1001223))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc013_01 2', 'p21', [r(-12), r_shake, light], 6)
get_char('c213') '[convertstrid(1001224)]' (**arg(25, 1001224))
hide p1
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('uc002_03 4', 'p518', [l(-23), l_shake, light, flip], 6)
get_char('c5181') '[convertstrid(1001225)]' (**arg(26, 1001225))
$ update_portrait('uc002_03 4', 'p518', [l(-23), dark, flip], 5)
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001226)]' (**arg(27, 1001226))
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001227)]' (**arg(28, 1001227))
hide p518
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001228)]' (**arg(29, 1001228))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001229)]' (**arg(30, 1001229))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001230)]' (**arg(31, 1001230))
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001231)]' (**arg(32, 1001231))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001232)]' (**arg(33, 1001232))
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001233)]' (**arg(34, 1001233))
hide p21
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_03 4', 'p518', [r(-23), light], 6)
get_char('c5183') '[convertstrid(1001234)]' (**arg(35, 1001234))
hide p518
$ update_portrait('uc002_03 2', 'p519', [r(-23), light], 6)
get_char('c5193') '[convertstrid(1001235)]' (**arg(36, 1001235))
hide p519
$ update_portrait('uc002_03 4', 'p520', [r(-23), light], 6)
get_char('c5203') '[convertstrid(1001236)]' (**arg(37, 1001236))
hide p1
$ update_portrait('uc002_03 4', 'p520', [r(-23), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001237)]' (**arg(38, 1001237))
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001238)]' (**arg(39, 1001238))
hide p1
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001239)]' (**arg(40, 1001239))
hide p520
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('uc002_03 3', 'p518', [r(-23), r_shake, light], 6)
get_char('c5183') '[convertstrid(1001240)]' (**arg(41, 1001240))
hide p2
$ update_portrait('uc002_03 3', 'p518', [r(-23), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001241)]' (**arg(42, 1001241))
hide p518
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001242)]' (**arg(43, 1001242))
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001243)]' (**arg(44, 1001243))
hide p3
$ update_portrait('sc013_01 1', 'p21', [r(-12), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001244)]' (**arg(45, 1001244))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc013_01 4', 'p21', [r(-12), r_shake, light], 6)
get_char('c213') '[convertstrid(1001245)]' (**arg(46, 1001245))
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001246)]' (**arg(47, 1001246))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001247)]' (**arg(48, 1001247))
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001248)]' (**arg(49, 1001248))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001249)]' (**arg(50, 1001249))
$ update_portrait('sc013_01 3', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001250)]' (**arg(51, 1001250))
$ update_portrait('sc013_01 3', 'p21', [r(-12), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001251)]' (**arg(52, 1001251))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1001252)]' (**arg(53, 1001252))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro08.ogg"
get_char('c31') '[convertstrid(1001253)]' (**arg(54, 1001253))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc013_01 4', 'p21', [r(-12), r_shake, light], 6)
get_char('c213') '[convertstrid(1001254)]' (**arg(55, 1001254))
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001255)]' (**arg(56, 1001255))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001256)]' (**arg(57, 1001256))
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001257)]' (**arg(58, 1001257))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc013_01 4', 'p21', [r(-12), r_shake, light], 6)
get_char('c213') '[convertstrid(1001258)]' (**arg(59, 1001258))
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001259)]' (**arg(60, 1001259))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001260)]' (**arg(61, 1001260))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001261)]' (**arg(62, 1001261))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001262)]' (**arg(63, 1001262))
hide p21
$ update_portrait('uc002_03 2', 'p518', [r(-23), light], 6)
get_char('c5183') '[convertstrid(1001263)]' (**arg(64, 1001263))
hide p518
$ update_portrait('uc002_03 4', 'p519', [r(-23), light], 6)
get_char('c5193') '[convertstrid(1001264)]' (**arg(65, 1001264))
$ update_portrait('uc002_03 4', 'p519', [r(-23), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001265)]' (**arg(66, 1001265))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001266)]' (**arg(67, 1001266))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001267)]' (**arg(68, 1001267))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001268)]' (**arg(69, 1001268))
hide p3
hide p519
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1001269)]' (**arg(70, 1001269))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001270)]' (**arg(71, 1001270))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001271)]' (**arg(72, 1001271))
hide p1
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc013_01 2', 'p21', [r(-12), r_shake, light], 6)
get_char('c213') '[convertstrid(1001272)]' (**arg(73, 1001272))
hide p2
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001273)]' (**arg(74, 1001273))
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001274)]' (**arg(75, 1001274))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001275)]' (**arg(76, 1001275))
hide p21
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001276)]' (**arg(77, 1001276))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001277)]' (**arg(78, 1001277))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001278)]' (**arg(79, 1001278))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1001279)]' (**arg(80, 1001279))
$ play_music("ed7511.ogg")
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1001280)]' (**arg(81, 1001280))
hide p2
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001281)]' (**arg(82, 1001281))
hide p3
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
$ update_portrait('uc002_03 3', 'p518', [l(-23), light, flip], 6)
get_char('c5181') '[convertstrid(1001282)]' (**arg(83, 1001282))
hide p518
$ update_portrait('uc002_03 4', 'p519', [l(-23), light, flip], 6)
get_char('c5191') '[convertstrid(1001283)]' (**arg(84, 1001283))
hide p21
$ update_portrait('uc002_03 4', 'p519', [l(-23), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1001284)]' (**arg(85, 1001284))
hide p519
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('uc002_03 2', 'p520', [l(-23), light, flip], 6)
get_char('c5201') '[convertstrid(1001285)]' (**arg(86, 1001285)) with shake
hide p2
$ update_portrait('uc002_03 2', 'p520', [l(-23), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6011.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1001286)]' (**arg(87, 1001286))
hide p520
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "fight_6012.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
get_char('c21') '[convertstrid(1001287)]' (**arg(88, 1001287))
hide p2
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7057.ogg"
get_char('c31') '[convertstrid(1001288)]' (**arg(89, 1001288))
hide p3
$ update_portrait('uc002_03 2', 'p518', [l(-23), light, flip], 6)
play sfx2 "fight_6012.ogg"
get_char('c5181') '[convertstrid(1001289)]' (**arg(90, 1001289))
hide p518
$ update_portrait('uc002_03 3', 'p519', [l_exit(-23), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c5191') '[convertstrid(1001290)]' (**arg(91, 1001290))
hide p519
$ play_music("ed7516.ogg")
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001291)]' (**arg(92, 1001291))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c21') '[convertstrid(1001292)]' (**arg(93, 1001292))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1001293)]' (**arg(94, 1001293)) with shake
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001294)]' (**arg(95, 1001294))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001295)]' (**arg(96, 1001295))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001296)]' (**arg(97, 1001296))
hide p2
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro15.ogg"
get_char('c31') '[convertstrid(1001297)]' (**arg(98, 1001297))
hide p3
get_char('c5271') '[convertstrid(1001298)]' (**arg(99, 1001298))
hide p1
get_char('c5283') '[convertstrid(1001299)]' (**arg(100, 1001299))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1001300)]' (**arg(101, 1001300))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1001301)]' (**arg(102, 1001301))
hide p1
get_char('c5283') '[convertstrid(1001302)]' (**arg(103, 1001302))
hide p2
get_char('c5271') '[convertstrid(1001303)]' (**arg(104, 1001303))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001304)]' (**arg(105, 1001304, size=(1.2))) with shake
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
get_char('c5271') '[convertstrid(1001305)]' (**arg(106, 1001305))
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001306)]' (**arg(107, 1001306))
$ update_portrait('sc013_01 2', 'p21', [r(-12), dark], 5)
get_char('c5271') '[convertstrid(1001307)]' (**arg(108, 1001307))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001308)]' (**arg(109, 1001308))
$ update_portrait('sc013_01 2', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001309)]' (**arg(110, 1001309))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001310)]' (**arg(111, 1001310))
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
get_char('c5271') '[convertstrid(1001311)]' (**arg(112, 1001311))
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001312)]' (**arg(113, 1001312))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001313)]' (**arg(114, 1001313))
$ update_portrait('sc013_01 1', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001314)]' (**arg(115, 1001314))
$ update_portrait('sc013_01 4', 'p21', [r(-12), light], 6)
get_char('c213') '[convertstrid(1001315)]' (**arg(116, 1001315))
$ update_portrait('sc013_01 4', 'p21', [r(-12), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch24.ogg"
get_char('c21') '[convertstrid(1001316)]' (**arg(117, 1001316))
hide p21
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(1001317)]' (**arg(118, 1001317))
return "avg10013"