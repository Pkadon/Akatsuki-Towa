label avg24044(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_021
$ update_narrator('c6541')
window show
with trans
get_char('c6541') '[convertstrid(1200176)]' (**arg(1, 1200176))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200177)]' (**arg(2, 1200177))
return "avg24044"