label avg10522:

$ play_music("ED6303.ogg")
scene avg_bg_107
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1152034)]' (**arg(1, 1152034))
get_char('c0') '[convertstrid(1152035)]' (**arg(2, 1152035))
get_char('c0') '[convertstrid(1152036)]' (**arg(3, 1152036))
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152037)]' (**arg(4, 1152037))
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152038)]' (**arg(5, 1152038))
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('st041_01 2', 'p240', [r(-1), r_shake, light], 6)
get_char('c2403') '[convertstrid(1152039)]' (**arg(6, 1152039))
$ update_portrait('st041_01 2', 'p240', [r(-1), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152040)]' (**arg(7, 1152040))
$ update_portrait('st050_01 1', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152041)]' (**arg(8, 1152041))
$ update_portrait('st050_01 4', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152042)]' (**arg(9, 1152042))
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
play sfx2 "other_7061.ogg"
get_char('c2571') '[convertstrid(1152043)]' (**arg(10, 1152043))
hide p240
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152044)]' (**arg(11, 1152044))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st050_01 3', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152045)]' (**arg(12, 1152045))
hide p257
hide p1
$ update_narrator('c41')
with fade
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152046)]' (**arg(13, 1152046))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152047)]' (**arg(14, 1152047))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l_entrance(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152048)]' (**arg(15, 1152048))
$ update_portrait('st050_01 1', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152049)]' (**arg(16, 1152049))
$ update_portrait('st050_01 1', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152050)]' (**arg(17, 1152050))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st050_01 1', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152051)]' (**arg(18, 1152051))
$ update_portrait('st050_01 1', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152052)]' (**arg(19, 1152052))
$ update_portrait('st050_01 1', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152053)]' (**arg(20, 1152053))
hide p257
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152054)]' (**arg(21, 1152054))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1152055)]' (**arg(22, 1152055))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152056)]' (**arg(23, 1152056))
hide p4
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l_entrance(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152057)]' (**arg(24, 1152057))
$ update_portrait('st050_01 5', 'p257', [l_exit(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1152058)]' (**arg(25, 1152058))
hide p257
$ update_portrait('oc003_01 17', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c31') '[convertstrid(1152059)]' (**arg(26, 1152059))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152060)]' (**arg(27, 1152060))
hide p3
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152061)]' (**arg(28, 1152061))
hide p2
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152062)]' (**arg(29, 1152062))
hide p4
hide p1
$ update_narrator('c12313')
with fade
get_char('c12313') '[convertstrid(1152063)]' (**arg(30, 1152063))
get_char('c12291') '[convertstrid(1152064)]' (**arg(31, 1152064))
get_char('c12291') '[convertstrid(1152065)]' (**arg(32, 1152065))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152066)]' (**arg(33, 1152066))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12311') '[convertstrid(1152067)]' (**arg(34, 1152067))
hide p1
$ update_portrait('oc002_01 22', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1152068)]' (**arg(35, 1152068))
$ update_portrait('oc002_01 22', 'p2', [r(-3), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152069)]' (**arg(36, 1152069))
$ update_portrait('st041_01 2', 'p240', [l(-1), l_shake, light, flip], 6)
get_char('c2401') '[convertstrid(1152070)]' (**arg(37, 1152070))
stop music
hide p240
hide p2
$ update_portrait('st050_01 3', 'p257', [l(-11), light, flip], 6)
$ update_narrator('c2571')
with fade
get_char('c2571') '[convertstrid(1152071)]' (**arg(38, 1152071, size=(1.2)))
$ update_portrait('st050_01 3', 'p257', [l(-11), dark, flip], 5)
get_char('c6883') '[convertstrid(1152072)]' (**arg(39, 1152072)) with shake
$ play_music("ed7511.ogg")
hide p257
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
get_char('c21') '[convertstrid(1152073)]' (**arg(40, 1152073))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152074)]' (**arg(41, 1152074))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152075)]' (**arg(42, 1152075))
hide p2
hide p1
$ update_portrait('oc007_01 3', 'p7', [r(-24), light], 6)
$ update_narrator('c73')
with fade
get_char('c73') '[convertstrid(1152076)]' (**arg(43, 1152076))
$ update_portrait('oc007_01 3', 'p7', [r(-24), dark], 5)
$ update_portrait('st050_01 3', 'p257', [l(-11), l_shake, light, flip], 6)
get_char('c2571') '[convertstrid(1152077)]' (**arg(44, 1152077))
hide p257
hide p7
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1152078)]' (**arg(45, 1152078))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1152079)]' (**arg(46, 1152079))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1152080)]' (**arg(47, 1152080))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1152081)]' (**arg(48, 1152081))
hide p3
$ update_portrait('st041_01 4', 'p240', [l_entrance(-1), light, flip], 6)
get_char('c2401') '[convertstrid(1152082)]' (**arg(49, 1152082))
$ update_portrait('st041_01 4', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152083)]' (**arg(50, 1152083))
return