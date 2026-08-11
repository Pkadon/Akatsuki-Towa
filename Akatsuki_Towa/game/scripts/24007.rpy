label avg24007(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_064
$ update_narrator('c7431')
window show
with trans
get_char('c7431') '[convertstrid(1200023)]' (**arg(1, 1200023))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200024)]' (**arg(2, 1200024))
return "avg24007"