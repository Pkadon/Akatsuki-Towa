label avg10407(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_portrait('oc004_01 22', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c41') '[convertstrid(1140448)]' (**arg(1, 1140448))
$ update_portrait('oc004_01 22', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140449)]' (**arg(2, 1140449))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7072.ogg"
get_char('c41') '[convertstrid(1140450)]' (**arg(3, 1140450))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140451)]' (**arg(4, 1140451))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
get_char('c11593') '[convertstrid(1140452)]' (**arg(5, 1140452))
get_char('c11593') '[convertstrid(1140453)]' (**arg(6, 1140453))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140454)]' (**arg(7, 1140454))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
get_char('c11593') '[convertstrid(1140455)]' (**arg(8, 1140455))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c41') '[convertstrid(1140456)]' (**arg(9, 1140456))
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140457)]' (**arg(10, 1140457))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
get_char('c11593') '[convertstrid(1140458)]' (**arg(11, 1140458))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c41') '[convertstrid(1140459)]' (**arg(12, 1140459))
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140460)]' (**arg(13, 1140460))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1140461)]' (**arg(14, 1140461))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140462)]' (**arg(15, 1140462))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1140463)]' (**arg(16, 1140463))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140464)]' (**arg(17, 1140464))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140465)]' (**arg(18, 1140465))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140466)]' (**arg(19, 1140466))
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140467)]' (**arg(20, 1140467))
$ update_portrait('oc004_01 1', 'p4', [l_exit(-5), light, flip], 6)
get_char('c41') '[convertstrid(1140468)]' (**arg(21, 1140468))
hide p4
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140469)]' (**arg(22, 1140469))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140470)]' (**arg(23, 1140470))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1140471)]' (**arg(24, 1140471))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1140472)]' (**arg(25, 1140472))
return "avg10407"