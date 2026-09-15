label avg24035(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_014
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200143)]' (**arg(1, 1200143))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
get_char('c7621') '[convertstrid(1200144)]' (**arg(2, 1200144))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200145)]' (**arg(3, 1200145))
return "avg24035"