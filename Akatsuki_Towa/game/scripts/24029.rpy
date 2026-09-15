label avg24029(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_046
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200120)]' (**arg(1, 1200120))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c10151') '[convertstrid(1200121)]' (**arg(2, 1200121))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200122)]' (**arg(3, 1200122))
return "avg24029"