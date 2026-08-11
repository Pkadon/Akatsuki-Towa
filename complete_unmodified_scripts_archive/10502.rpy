label avg10502(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_narrator('c561')
window show
with trans
$ update_portrait('sc049_01 1', 'p56', [l_entrance(-8), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c561') '[convertstrid(1150042)]' (**arg(1, 1150042))
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150043)]' (**arg(2, 1150043))
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch23.ogg"
get_char('c23') '[convertstrid(1150044)]' (**arg(3, 1150044))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150045)]' (**arg(4, 1150045))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150046)]' (**arg(5, 1150046))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150047)]' (**arg(6, 1150047))
hide p56
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1150048)]' (**arg(7, 1150048))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150049)]' (**arg(8, 1150049))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1150050)]' (**arg(9, 1150050))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150051)]' (**arg(10, 1150051))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l_entrance(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150052)]' (**arg(11, 1150052))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150053)]' (**arg(12, 1150053))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150054)]' (**arg(13, 1150054))
hide p56
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
play sfx2 "other_7047.ogg"
get_char('c33') '[convertstrid(1150055)]' (**arg(14, 1150055))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
play sfx2 "other_7081.ogg"
get_char('c12011') '[convertstrid(1150056)]' (**arg(15, 1150056))
$ update_portrait('oc002_01 14', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150057)]' (**arg(16, 1150057))
$ update_portrait('oc002_01 14', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150058)]' (**arg(17, 1150058))
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150059)]' (**arg(18, 1150059))
hide p3
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150060)]' (**arg(19, 1150060))
hide p56
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150061)]' (**arg(20, 1150061))
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150062)]' (**arg(21, 1150062))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1150063)]' (**arg(22, 1150063))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l_exit(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150064)]' (**arg(23, 1150064))
hide p56
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150065)]' (**arg(24, 1150065))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150066)]' (**arg(25, 1150066))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150067)]' (**arg(26, 1150067))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150068)]' (**arg(27, 1150068))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150069)]' (**arg(28, 1150069))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150070)]' (**arg(29, 1150070))
hide p3
play sfx2 "other_7081.ogg"
get_char('c12011') '[convertstrid(1150071)]' (**arg(30, 1150071))
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1150072)]' (**arg(31, 1150072))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150073)]' (**arg(32, 1150073))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1150074)]' (**arg(33, 1150074))
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150075)]' (**arg(34, 1150075))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150076)]' (**arg(35, 1150076))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150077)]' (**arg(36, 1150077))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1150078)]' (**arg(37, 1150078))
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150079)]' (**arg(38, 1150079))
hide p56
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1150080)]' (**arg(39, 1150080))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150081)]' (**arg(40, 1150081))
hide p3
hide p2
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1150082)]' (**arg(41, 1150082))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l_entrance(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150083)]' (**arg(42, 1150083))
hide p3
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150084)]' (**arg(43, 1150084))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150085)]' (**arg(44, 1150085))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150086)]' (**arg(45, 1150086))
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1150087)]' (**arg(46, 1150087))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150088)]' (**arg(47, 1150088))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150089)]' (**arg(48, 1150089))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150090)]' (**arg(49, 1150090))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1150091)]' (**arg(50, 1150091))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1150092)]' (**arg(51, 1150092))
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150093)]' (**arg(52, 1150093))
hide p56
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l_entrance(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150094)]' (**arg(53, 1150094))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150095)]' (**arg(54, 1150095))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150096)]' (**arg(55, 1150096))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150097)]' (**arg(56, 1150097))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1150098)]' (**arg(57, 1150098))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1150099)]' (**arg(58, 1150099))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 11', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150100)]' (**arg(59, 1150100))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150101)]' (**arg(60, 1150101))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1150102)]' (**arg(61, 1150102))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150103)]' (**arg(62, 1150103))
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
play sfx2 "other_7081.ogg"
get_char('c12011') '[convertstrid(1150104)]' (**arg(63, 1150104))
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1150105)]' (**arg(64, 1150105))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150106)]' (**arg(65, 1150106))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro05.ogg"
get_char('c31') '[convertstrid(1150107)]' (**arg(66, 1150107))
hide p3
$ update_portrait('oc002_01 5', 'p2', [l_entrance(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1150108)]' (**arg(67, 1150108))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150109)]' (**arg(68, 1150109))
return "avg10502"