label avg12369(trans=fade_in):

$ play_music("ed7124.ogg")
scene avg_bg_059
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1133845)]' (**arg(1, 1133845))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c10961') '[convertstrid(1133846)]' (**arg(2, 1133846))
hide p2
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133847)]' (**arg(3, 1133847))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1133848)]' (**arg(4, 1133848))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c10961') '[convertstrid(1133849)]' (**arg(5, 1133849))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133850)]' (**arg(6, 1133850))
return "avg12369"