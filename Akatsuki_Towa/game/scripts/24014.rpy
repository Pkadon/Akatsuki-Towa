label avg24014(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200061)]' (**arg(1, 1200061))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c7421') '[convertstrid(1200062)]' (**arg(2, 1200062))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200063)]' (**arg(3, 1200063))
return "avg24014"