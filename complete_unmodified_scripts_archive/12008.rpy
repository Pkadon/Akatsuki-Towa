label avg12008:

$ play_music("ed7150.ogg")
scene avg_bg_056
$ update_narrator('c7181')
window show
with fade_in
play sfx2 "other_7046.ogg"
get_char('c7181') '[convertstrid(1007181)]' (**arg(1, 1007181))
get_char('c7181') '[convertstrid(1007182)]' (**arg(2, 1007182))
get_char('c7181') '[convertstrid(1007183)]' (**arg(3, 1007183))
get_char('c7181') '[convertstrid(1007184)]' (**arg(4, 1007184))
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1007251)]' (**arg(5, 1007251))
scene avg_bg_018
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
with fade
get_char('c23') '[convertstrid(1007185)]' (**arg(6, 1007185))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007186)]' (**arg(7, 1007186))
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007187)]' (**arg(8, 1007187))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1007188)]' (**arg(9, 1007188))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007190)]' (**arg(10, 1007190))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 5', 'p72', [l(-17), l_shake, light, flip], 6)
get_char('c721') '[convertstrid(1007090)]' (**arg(11, 1007090))
$ update_portrait('sc068_01 5', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1007192)]' (**arg(12, 1007192))
hide p72
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1007193)]' (**arg(13, 1007193))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c21') '[convertstrid(1007194)]' (**arg(14, 1007194))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007195)]' (**arg(15, 1007195))
hide p2
hide p1
get_char('c0') '[convertstrid(1007196)]' (**arg(16, 1007196))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007197)]' (**arg(17, 1007197))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007198)]' (**arg(18, 1007198))
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007199)]' (**arg(19, 1007199))
$ update_portrait('sc068_01 5', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007200)]' (**arg(20, 1007200))
$ update_portrait('sc068_01 6', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007201)]' (**arg(21, 1007201))
$ play_music("ed7561.ogg")
$ update_portrait('sc068_01 6', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1007202)]' (**arg(22, 1007202))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007203)]' (**arg(23, 1007203))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007204)]' (**arg(24, 1007204))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007205)]' (**arg(25, 1007205))
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007206)]' (**arg(26, 1007206))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007207)]' (**arg(27, 1007207))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007208)]' (**arg(28, 1007208))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 6', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007209)]' (**arg(29, 1007209))
$ update_portrait('sc068_01 2', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007210)]' (**arg(30, 1007210))
$ update_portrait('sc068_01 5', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007211)]' (**arg(31, 1007211))
$ update_portrait('sc068_01 5', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007212)]' (**arg(32, 1007212))
stop music
hide p72
$ update_portrait('oc001_01 15', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
get_char('c21') '[convertstrid(1007213)]' (**arg(33, 1007213))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1007214)]' (**arg(34, 1007214))
$ play_music("ed7150.ogg")
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007215)]' (**arg(35, 1007215))
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007216)]' (**arg(36, 1007216))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007217)]' (**arg(37, 1007217))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 6', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007218)]' (**arg(38, 1007218))
hide p2
$ update_portrait('sc068_01 6', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007219)]' (**arg(39, 1007219))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 2', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007220)]' (**arg(40, 1007220))
hide p1
$ update_portrait('sc068_01 2', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007221)]' (**arg(41, 1007221))
hide p2
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na03_b.ogg"
get_char('c13') '[convertstrid(1007222)]' (**arg(42, 1007222))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 5', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007223)]' (**arg(43, 1007223))
hide p1
$ update_portrait('sc068_01 5', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007224)]' (**arg(44, 1007224))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007225)]' (**arg(45, 1007225))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007226)]' (**arg(46, 1007226))
hide p1
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1007227)]' (**arg(47, 1007227))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007228)]' (**arg(48, 1007228))
return