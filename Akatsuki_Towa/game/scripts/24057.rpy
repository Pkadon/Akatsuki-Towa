label avg24057(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_narrator('c7583')
window show
with trans
get_char('c7583') '[convertstrid(1200238)]' (**arg(1, 1200238))
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200239)]' (**arg(2, 1200239))
return "avg24057"