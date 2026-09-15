label avg24062(trans=fade_in):

$ play_music("ed6323.ogg")
scene avg_bg_218
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200252)]' (**arg(1, 1200252))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200253)]' (**arg(2, 1200253))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200254)]' (**arg(3, 1200254))
return "avg24062"