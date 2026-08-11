label avg12176(trans=fade_in):

$ play_music("ed7111.ogg")
scene avg_bg_003
$ update_portrait('oc005_01 2', 'p5', [l(-6), light, flip], 6)
$ update_narrator('c51')
window show
with trans
get_char('c51') '[convertstrid(1120530)]' (**arg(1, 1120530))
$ update_portrait('oc005_01 2', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120531)]' (**arg(2, 1120531))
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120532)]' (**arg(3, 1120532))
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120533)]' (**arg(4, 1120533))
$ update_portrait('oc005_01 14', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120534)]' (**arg(5, 1120534))
hide p1
$ update_portrait('oc005_01 14', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1120535)]' (**arg(6, 1120535))
hide p5
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120536)]' (**arg(7, 1120536))
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120537)]' (**arg(8, 1120537))
hide p2
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120538)]' (**arg(9, 1120538))
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
get_char('c51') '[convertstrid(1120539)]' (**arg(10, 1120539))
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
get_char('c51') '[convertstrid(1120540)]' (**arg(11, 1120540))
$ update_portrait('oc005_01 8', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120541)]' (**arg(12, 1120541))
hide p5
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120542)]' (**arg(13, 1120542))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1007705)]' (**arg(14, 1007705))
hide p2
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007706)]' (**arg(15, 1007706))
return "avg12176"