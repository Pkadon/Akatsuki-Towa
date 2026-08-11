label avg12458(trans=fade_in):

$ play_music("ed7102.ogg")
scene avg_bg_022
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1143729)]' (**arg(1, 1143729))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143730)]' (**arg(2, 1143730))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143731)]' (**arg(3, 1143731))
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1143732)]' (**arg(4, 1143732))
hide p2
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1143733)]' (**arg(5, 1143733))
return "avg12458"