label avg24077(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_041
$ update_narrator('c7591')
window show
with trans
get_char('c7591') '[convertstrid(1200295)]' (**arg(1, 1200295))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200296)]' (**arg(2, 1200296))
return "avg24077"