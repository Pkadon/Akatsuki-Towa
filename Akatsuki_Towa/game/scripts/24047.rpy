label avg24047(trans=fade_in):

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1200200)]' (**arg(1, 1200200))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200201)]' (**arg(2, 1200201))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10151') '[convertstrid(1200202)]' (**arg(3, 1200202))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200203)]' (**arg(4, 1200203))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200204)]' (**arg(5, 1200204))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c10151') '[convertstrid(1200205)]' (**arg(6, 1200205))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200206)]' (**arg(7, 1200206))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
get_char('c10151') '[convertstrid(1200207)]' (**arg(8, 1200207))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200208)]' (**arg(9, 1200208))
return "avg24047"