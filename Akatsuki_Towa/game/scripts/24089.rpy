label avg24089(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_narrator('c50123')
window show
with trans
get_char('c50123') '[convertstrid(1200324)]' (**arg(1, 1200324))
get_char('c50123') '[convertstrid(1200325)]' (**arg(2, 1200325))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200326)]' (**arg(3, 1200326))
return "avg24089"