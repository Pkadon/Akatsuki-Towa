label avg24049(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_049
$ update_narrator('c7603')
window show
with trans
get_char('c7603') '[convertstrid(1200212)]' (**arg(1, 1200212))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200213)]' (**arg(2, 1200213))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c7313') '[convertstrid(1200214)]' (**arg(3, 1200214))
return "avg24049"