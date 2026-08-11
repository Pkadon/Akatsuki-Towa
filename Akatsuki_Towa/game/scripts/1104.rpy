label avg1104(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_075
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2102527)]' (**arg(1, 2102527))
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102528)]' (**arg(2, 2102528))
$ update_portrait('st037_01 1', 'p236', [l(-10), dark, flip], 5)
get_char('c10893') '[convertstrid(2102529)]' (**arg(3, 2102529))
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102530)]' (**arg(4, 2102530))
$ update_portrait('st037_01 4', 'p236', [l(-10), l_shake, light, flip], 6)
get_char('c2361') '[convertstrid(2102531)]' (**arg(5, 2102531))
$ update_portrait('st037_01 4', 'p236', [l(-10), dark, flip], 5)
get_char('c10893') '[convertstrid(2102532)]' (**arg(6, 2102532)) with shake
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(2102533)]' (**arg(7, 2102533))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('st037_01 6', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102534)]' (**arg(8, 2102534))
hide p3
$ update_portrait('st037_01 6', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(2102535)]' (**arg(9, 2102535))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2102536)]' (**arg(10, 2102536))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 6', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102537)]' (**arg(11, 2102537))
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102538)]' (**arg(12, 2102538))
$ update_portrait('st037_01 1', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2102539)]' (**arg(13, 2102539))
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2102540)]' (**arg(14, 2102540))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 6', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102541)]' (**arg(15, 2102541))
hide p2
$ update_portrait('st037_01 6', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('st004_01 5', 'p204', [r(4), r_shake, light], 6)
get_char('c2043') '[convertstrid(2102542)]' (**arg(16, 2102542))
hide p204
get_char('c5113') '[convertstrid(2102543)]' (**arg(17, 2102543))
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(2102544)]' (**arg(18, 2102544))
hide p236
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2102545)]' (**arg(19, 2102545))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2102546)]' (**arg(20, 2102546))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102547)]' (**arg(21, 2102547))
hide p236
hide p2
get_char('c0') '[convertstrid(2102548)]' (**arg(22, 2102548))
$ update_portrait('st037_01 6', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102549)]' (**arg(23, 2102549))
$ update_portrait('st037_01 6', 'p236', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_exit(-2), light], 6)
get_char('c13') '[convertstrid(2102550)]' (**arg(24, 2102550))
hide p1
hide p236
get_char('c0') '[convertstrid(2102551)]' (**arg(25, 2102551))
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
get_char('c2361') '[convertstrid(2102552)]' (**arg(26, 2102552))
return "avg1104"