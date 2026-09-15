label avg24037(trans=fade_in):

$ play_music("ed7200.ogg")
scene avg_bg_026
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200148)]' (**arg(1, 1200148))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200149)]' (**arg(2, 1200149))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200150)]' (**arg(3, 1200150))
return "avg24037"