label avg24051(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_049
$ update_narrator('c7603')
window show
with trans
get_char('c7603') '[convertstrid(1200218)]' (**arg(1, 1200218))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200219)]' (**arg(2, 1200219))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c7313') '[convertstrid(1200220)]' (**arg(3, 1200220))
return "avg24051"