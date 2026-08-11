label avg10557(trans=fade_in):

$ play_music("ed7571.ogg")
scene avg_bg_078
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1153901)]' (**arg(1, 1153901))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153902)]' (**arg(2, 1153902))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153903)]' (**arg(3, 1153903))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 2', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153904)]' (**arg(4, 1153904))
$ update_portrait('oc008_01 6', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153905)]' (**arg(5, 1153905))
hide p1
$ update_portrait('oc008_01 6', 'p1265', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r_entrance(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1153906)]' (**arg(6, 1153906))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc008_01 2', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153907)]' (**arg(7, 1153907))
$ update_portrait('oc008_01 2', 'p1265', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1153908)]' (**arg(8, 1153908))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc008_01 2', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153909)]' (**arg(9, 1153909))
$ update_portrait('oc008_01 4', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153910)]' (**arg(10, 1153910))
hide p2
$ update_portrait('oc008_01 4', 'p1265', [l(-5), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), r_shake, light], 6)
get_char('c43') '[convertstrid(1153911)]' (**arg(11, 1153911))
$ update_portrait('oc004_01 16', 'p4', [r(-5), dark], 5)
$ update_portrait('oc008_01 5', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153912)]' (**arg(12, 1153912))
hide p4
$ update_portrait('oc008_01 5', 'p1265', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153913)]' (**arg(13, 1153913))
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc008_01 5', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153914)]' (**arg(14, 1153914))
$ update_portrait('oc008_01 4', 'p1265', [l(-5), light, flip], 6)
get_char('c12651') '[convertstrid(1153915)]' (**arg(15, 1153915))
hide p2
$ update_portrait('oc008_01 4', 'p1265', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1153916)]' (**arg(16, 1153916))
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153917)]' (**arg(17, 1153917))
hide p1265
hide p1
$ update_narrator('c12573')
with fade
play sfx2 "other_7088.ogg"
get_char('c12573') '[convertstrid(1153918)]' (**arg(18, 1153918))
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1153919)]' (**arg(19, 1153919))
$ update_portrait('oc008_01 2', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1153920)]' (**arg(20, 1153920))
hide p3
$ update_portrait('sc008_01 4', 'p16', [r_entrance(-18), light], 6)
get_char('c163') '[convertstrid(1153921)]' (**arg(21, 1153921))
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1153922)]' (**arg(22, 1153922))
$ update_portrait('oc008_01 2', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1153923)]' (**arg(23, 1153923))
$ update_portrait('oc008_01 2', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1153924)]' (**arg(24, 1153924))
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1153925)]' (**arg(25, 1153925))
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1153926)]' (**arg(26, 1153926))
hide p16
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153927)]' (**arg(27, 1153927))
hide p1
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1153928)]' (**arg(28, 1153928))
hide p16
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153929)]' (**arg(29, 1153929))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153930)]' (**arg(30, 1153930))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 2', 'p8', [l_exit(-5), light, flip], 6)
play sfx2 "other_7088.ogg"
get_char('c81') '[convertstrid(1153931)]' (**arg(31, 1153931))
hide p8
hide p1
$ update_portrait('oc003_01 9', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1153932)]' (**arg(32, 1153932))
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l_entrance(-18), light, flip], 6)
get_char('c161') '[convertstrid(1153933)]' (**arg(33, 1153933))
hide p16
hide p3
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
play sfx2 "other_7085.ogg"
get_char('c41') '[convertstrid(1153934)]' (**arg(34, 1153934))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1153935)]' (**arg(35, 1153935))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153936)]' (**arg(36, 1153936))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1153937)]' (**arg(37, 1153937))
return "avg10557"