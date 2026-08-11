label avg20058(trans=fade_in):

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c4973')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c4973') '[convertstrid(1002982)]' (**arg(1, 1002982))
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1002983)]' (**arg(2, 1002983))
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1002984)]' (**arg(3, 1002984))
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1002985)]' (**arg(4, 1002985))
return "avg20058"