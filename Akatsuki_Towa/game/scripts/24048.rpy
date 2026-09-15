label avg24048(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_049
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200209)]' (**arg(1, 1200209))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7603') '[convertstrid(1200210)]' (**arg(2, 1200210))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200211)]' (**arg(3, 1200211))
return "avg24048"