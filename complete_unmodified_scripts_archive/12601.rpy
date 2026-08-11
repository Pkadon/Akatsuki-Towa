label avg12601(trans=fade_in):

$ play_music("ED6102.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1161118)]' (**arg(1, 1161118))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161119)]' (**arg(2, 1161119))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c12321') '[convertstrid(1161120)]' (**arg(3, 1161120))
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1161121)]' (**arg(4, 1161121))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161122)]' (**arg(5, 1161122))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c12321') '[convertstrid(1161123)]' (**arg(6, 1161123))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161124)]' (**arg(7, 1161124))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
get_char('c12321') '[convertstrid(1161125)]' (**arg(8, 1161125))
get_char('c12321') '[convertstrid(1161126)]' (**arg(9, 1161126))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161127)]' (**arg(10, 1161127))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161128)]' (**arg(11, 1161128))
hide p3
get_char('c12321') '[convertstrid(1161129)]' (**arg(12, 1161129))
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1161130)]' (**arg(13, 1161130))
return "avg12601"