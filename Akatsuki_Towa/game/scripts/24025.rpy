label avg24025(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_017
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200104)]' (**arg(1, 1200104))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c9571') '[convertstrid(1200105)]' (**arg(2, 1200105))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200106)]' (**arg(3, 1200106))
return "avg24025"