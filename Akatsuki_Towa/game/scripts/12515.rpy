label avg12515(trans=fade_in):

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_narrator('c10901')
window show
with trans
get_char('c10901') '[convertstrid(1151069)]' (**arg(1, 1151069))
get_char('c10901') '[convertstrid(1151070)]' (**arg(2, 1151070))
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151071)]' (**arg(3, 1151071))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
get_char('c10901') '[convertstrid(1151072)]' (**arg(4, 1151072))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151073)]' (**arg(5, 1151073))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151074)]' (**arg(6, 1151074))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c10901') '[convertstrid(1151075)]' (**arg(7, 1151075))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1151076)]' (**arg(8, 1151076))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151077)]' (**arg(9, 1151077))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151078)]' (**arg(10, 1151078))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c10901') '[convertstrid(1151079)]' (**arg(11, 1151079))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151080)]' (**arg(12, 1151080))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151081)]' (**arg(13, 1151081))
hide p3
get_char('c10901') '[convertstrid(1151082)]' (**arg(14, 1151082))
hide p2
play sfx2 "other_7010.ogg"
get_char('c0') '[convertstrid(1151083)]' (**arg(15, 1151083))
play sfx2 "other_7046.ogg"
get_char('c11501') '[convertstrid(1151084)]' (**arg(16, 1151084))
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151085)]' (**arg(17, 1151085))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151086)]' (**arg(18, 1151086))
hide p3
get_char('c11501') '[convertstrid(1151087)]' (**arg(19, 1151087))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151088)]' (**arg(20, 1151088))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c11501') '[convertstrid(1151089)]' (**arg(21, 1151089))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151090)]' (**arg(22, 1151090))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c11501') '[convertstrid(1151091)]' (**arg(23, 1151091))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151092)]' (**arg(24, 1151092))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1151093)]' (**arg(25, 1151093))
hide p2
get_char('c11501') '[convertstrid(1151094)]' (**arg(26, 1151094))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151095)]' (**arg(27, 1151095))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1151096)]' (**arg(28, 1151096))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151097)]' (**arg(29, 1151097))
return "avg12515"