label avg24042(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_055
$ update_narrator('c10921')
window show
with trans
get_char('c10921') '[convertstrid(1200170)]' (**arg(1, 1200170))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200171)]' (**arg(2, 1200171))
return "avg24042"