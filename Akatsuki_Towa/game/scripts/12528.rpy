label avg12528(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1151522)]' (**arg(1, 1151522))
$ update_portrait('sc008_01 1', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1151523)]' (**arg(2, 1151523))
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1151524)]' (**arg(3, 1151524))
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151525)]' (**arg(4, 1151525))
hide p16
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li15.ogg"
get_char('c41') '[convertstrid(1151526)]' (**arg(5, 1151526))
hide p1
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1151527)]' (**arg(6, 1151527))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151528)]' (**arg(7, 1151528))
hide p2
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1151529)]' (**arg(8, 1151529))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
get_char('c131') '[convertstrid(1151530)]' (**arg(9, 1151530))
hide p13
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1151531)]' (**arg(10, 1151531))
hide p3
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1151532)]' (**arg(11, 1151532))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1151533)]' (**arg(12, 1151533))
return "avg12528"