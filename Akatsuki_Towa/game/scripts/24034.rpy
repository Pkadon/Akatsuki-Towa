label avg24034(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1200138)]' (**arg(1, 1200138))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c10151') '[convertstrid(1200139)]' (**arg(2, 1200139))
get_char('c10151') '[convertstrid(1200140)]' (**arg(3, 1200140))
get_char('c7641') '[convertstrid(1200141)]' (**arg(4, 1200141))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200142)]' (**arg(5, 1200142))
return "avg24034"