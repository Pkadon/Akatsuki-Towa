label avg10527(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_035
$ update_narrator('c151')
window show
with trans
$ update_portrait('sc007_01 1', 'p15', [l_entrance(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152197)]' (**arg(1, 1152197))
$ update_portrait('sc007_01 6', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152198)]' (**arg(2, 1152198))
$ update_portrait('sc007_01 6', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1152199)]' (**arg(3, 1152199))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152200)]' (**arg(4, 1152200))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152201)]' (**arg(5, 1152201))
hide p4
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152202)]' (**arg(6, 1152202))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152203)]' (**arg(7, 1152203))
hide p3
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1152204)]' (**arg(8, 1152204))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152205)]' (**arg(9, 1152205))
hide p2
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c43') '[convertstrid(1152206)]' (**arg(10, 1152206))
hide p4
$ update_portrait('oc003_01 17', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1152207)]' (**arg(11, 1152207))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152208)]' (**arg(12, 1152208))
hide p3
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152209)]' (**arg(13, 1152209))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152210)]' (**arg(14, 1152210))
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152211)]' (**arg(15, 1152211))
hide p1
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1152212)]' (**arg(16, 1152212))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152213)]' (**arg(17, 1152213))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1152214)]' (**arg(18, 1152214))
hide p2
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152215)]' (**arg(19, 1152215))
hide p15
hide p3
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
get_char('c41') '[convertstrid(1152216)]' (**arg(20, 1152216))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1152217)]' (**arg(21, 1152217))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152218)]' (**arg(22, 1152218))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro15.ogg"
get_char('c31') '[convertstrid(1152219)]' (**arg(23, 1152219))
return "avg10527"