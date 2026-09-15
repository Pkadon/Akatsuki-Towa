label avg24040(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_055
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200161)]' (**arg(1, 1200161))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c10921') '[convertstrid(1200162)]' (**arg(2, 1200162))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200163)]' (**arg(3, 1200163))
return "avg24040"