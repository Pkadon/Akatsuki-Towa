label avg12518(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1151220)]' (**arg(1, 1151220))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151221)]' (**arg(2, 1151221))
hide p2
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151222)]' (**arg(3, 1151222))
hide p13
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151223)]' (**arg(4, 1151223))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151224)]' (**arg(5, 1151224))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151225)]' (**arg(6, 1151225))
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151226)]' (**arg(7, 1151226))
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1151227)]' (**arg(8, 1151227))
hide p13
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151228)]' (**arg(9, 1151228))
hide p3
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151229)]' (**arg(10, 1151229))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151230)]' (**arg(11, 1151230))
hide p2
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151231)]' (**arg(12, 1151231))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151232)]' (**arg(13, 1151232))
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151233)]' (**arg(14, 1151233))
hide p1
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151234)]' (**arg(15, 1151234))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151235)]' (**arg(16, 1151235))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151236)]' (**arg(17, 1151236))
return "avg12518"