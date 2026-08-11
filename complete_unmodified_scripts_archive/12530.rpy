label avg12530(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('sc008_01 2', 'p16', [r(-18), light], 6)
$ update_narrator('c163')
window show
with trans
get_char('c163') '[convertstrid(1151622)]' (**arg(1, 1151622))
$ update_portrait('sc008_01 1', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1151623)]' (**arg(2, 1151623))
$ update_portrait('sc008_01 1', 'p16', [r(-18), dark], 5)
$ update_portrait('sc028_01 4', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151624)]' (**arg(3, 1151624))
hide p16
$ update_portrait('sc028_01 4', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1151625)]' (**arg(4, 1151625))
hide p36
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151626)]' (**arg(5, 1151626))
hide p2
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1151627)]' (**arg(6, 1151627))
hide p15
hide p1
$ update_narrator('c163')
$ update_portrait('sc008_01 3', 'p16', [r(-18), light], 6)
with fade
$ update_portrait('sc008_01 3', 'p16', [r(-18), r_shake, light], 6)
get_char('c163') '[convertstrid(1151628)]' (**arg(7, 1151628))
$ update_portrait('sc008_01 3', 'p16', [r(-18), dark], 5)
$ update_portrait('sc028_01 1', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151629)]' (**arg(8, 1151629))
$ update_portrait('sc028_01 1', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151630)]' (**arg(9, 1151630))
$ update_portrait('sc028_01 1', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1151631)]' (**arg(10, 1151631))
hide p36
hide p16
play sfx2 "other_7007.ogg"
get_char('c0') '[convertstrid(1151632)]' (**arg(11, 1151632)) with shake
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1151633)]' (**arg(12, 1151633))
hide p1
$ update_portrait('sc007_01 2', 'p15', [r_entrance(-17), light], 6)
get_char('c153') '[convertstrid(1151634)]' (**arg(13, 1151634))
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('sc008_01 3', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1151635)]' (**arg(14, 1151635))
$ update_portrait('sc008_01 3', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1151636)]' (**arg(15, 1151636))
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1151637)]' (**arg(16, 1151637))
hide p16
$ update_portrait('sc028_01 1', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151638)]' (**arg(17, 1151638))
hide p15
$ update_portrait('sc028_01 1', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('sc008_01 2', 'p16', [r(-18), r_shake, light], 6)
get_char('c163') '[convertstrid(1151639)]' (**arg(18, 1151639))
hide p36
hide p16
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
get_char('c33') '[convertstrid(1151640)]' (**arg(19, 1151640))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151641)]' (**arg(20, 1151641))
hide p13
$ update_portrait('sc028_01 2', 'p36', [l_entrance(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151642)]' (**arg(21, 1151642))
hide p3
$ update_portrait('sc028_01 2', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151643)]' (**arg(22, 1151643))
hide p1
$ update_portrait('sc005_01 1', 'p13', [r(-17), light], 6)
get_char('c133') '[convertstrid(1151644)]' (**arg(23, 1151644))
$ update_portrait('sc005_01 1', 'p13', [r(-17), dark], 5)
$ update_portrait('sc028_01 4', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151645)]' (**arg(24, 1151645))
hide p13
$ update_portrait('sc028_01 4', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1151646)]' (**arg(25, 1151646))
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('sc028_01 1', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151647)]' (**arg(26, 1151647))
hide p16
$ update_portrait('sc028_01 1', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c33') '[convertstrid(1151648)]' (**arg(27, 1151648))
hide p3
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151649)]' (**arg(28, 1151649))
hide p36
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('st050_01 5', 'p257', [l_entrance(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151650)]' (**arg(29, 1151650))
$ update_portrait('st050_01 5', 'p257', [l(-11), light, flip], 6)
get_char('c2571') '[convertstrid(1151651)]' (**arg(30, 1151651))
hide p2
$ update_portrait('st050_01 5', 'p257', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151652)]' (**arg(31, 1151652))
hide p257
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc028_01 1', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151653)]' (**arg(32, 1151653))
$ update_portrait('sc028_01 4', 'p36', [l(-7), light, flip], 6)
get_char('c361') '[convertstrid(1151654)]' (**arg(33, 1151654))
$ update_portrait('sc028_01 4', 'p36', [l(-7), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151655)]' (**arg(34, 1151655))
hide p36
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151656)]' (**arg(35, 1151656))
return "avg12530"