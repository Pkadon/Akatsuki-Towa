label avg24054(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1200227)]' (**arg(1, 1200227))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c7613') '[convertstrid(1200228)]' (**arg(2, 1200228))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200229)]' (**arg(3, 1200229))
return "avg24054"