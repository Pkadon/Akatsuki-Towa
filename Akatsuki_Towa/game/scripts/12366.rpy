label avg12366(trans=fade_in):

$ play_music("ed7124.ogg")
scene avg_bg_059
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "other_7021.ogg"
get_char('c23') '[convertstrid(1133805)]' (**arg(1, 1133805))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
get_char('c10961') '[convertstrid(1133806)]' (**arg(2, 1133806))
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1133807)]' (**arg(3, 1133807))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c10961') '[convertstrid(1133808)]' (**arg(4, 1133808))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1133809)]' (**arg(5, 1133809))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133810)]' (**arg(6, 1133810))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c10961') '[convertstrid(1133811)]' (**arg(7, 1133811))
get_char('c10961') '[convertstrid(1133812)]' (**arg(8, 1133812))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133813)]' (**arg(9, 1133813))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c10961') '[convertstrid(1133814)]' (**arg(10, 1133814))
get_char('c10961') '[convertstrid(1133815)]' (**arg(11, 1133815))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1133816)]' (**arg(12, 1133816))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10961') '[convertstrid(1133817)]' (**arg(13, 1133817))
get_char('c10961') '[convertstrid(1133818)]' (**arg(14, 1133818))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
play sfx2 "common_quest.ogg"
get_char('c23') '[convertstrid(1133819)]' (**arg(15, 1133819))
return "avg12366"