label avg10563(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_107
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1154311)]' (**arg(1, 1154311))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1154312)]' (**arg(2, 1154312))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154313)]' (**arg(3, 1154313))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1154314)]' (**arg(4, 1154314))
return "avg10563"