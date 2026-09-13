label avg24506(trans=fade_in):

$ play_music("ed7301.ogg")
scene avg_bg_218
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1206012)]' (**arg(1, 1206012))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1206013)]' (**arg(2, 1206013))
return "avg24506"