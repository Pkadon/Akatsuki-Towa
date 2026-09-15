label avg24001(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_011
$ update_narrator('c9641')
window show
with trans
get_char('c9641') '[convertstrid(1200000)]' (**arg(1, 1200000))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200001)]' (**arg(2, 1200001))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
get_char('c9641') '[convertstrid(1200002)]' (**arg(3, 1200002))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200003)]' (**arg(4, 1200003))
return "avg24001"