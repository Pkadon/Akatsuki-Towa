label avg24090(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_narrator('c50123')
window show
with trans
get_char('c50123') '[convertstrid(1200327)]' (**arg(1, 1200327))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200328)]' (**arg(2, 1200328))
return "avg24090"