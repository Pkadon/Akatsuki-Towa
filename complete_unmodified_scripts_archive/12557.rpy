label avg12557(trans=fade_in):

$ play_music("ED6102.ogg")
scene avg_bg_023
$ update_narrator('c12321')
window show
with trans
get_char('c12321') '[convertstrid(1153295)]' (**arg(1, 1153295))
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1153296)]' (**arg(2, 1153296))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c12321') '[convertstrid(1153297)]' (**arg(3, 1153297))
$ update_portrait('oc002_01 12', 'p2', [r_exit(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1153298)]' (**arg(4, 1153298))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1153299)]' (**arg(5, 1153299))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1153300)]' (**arg(6, 1153300))
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153301)]' (**arg(7, 1153301))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153302)]' (**arg(8, 1153302))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153303)]' (**arg(9, 1153303))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1153304)]' (**arg(10, 1153304))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1153305)]' (**arg(11, 1153305))
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c12321') '[convertstrid(1153306)]' (**arg(12, 1153306))
get_char('c12321') '[convertstrid(1153307)]' (**arg(13, 1153307))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1153308)]' (**arg(14, 1153308))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153309)]' (**arg(15, 1153309))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1153310)]' (**arg(16, 1153310))
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1153311)]' (**arg(17, 1153311))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1153312)]' (**arg(18, 1153312))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c12321') '[convertstrid(1153313)]' (**arg(19, 1153313))
return "avg12557"