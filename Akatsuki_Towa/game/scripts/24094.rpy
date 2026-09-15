label avg24094(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_049
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200336)]' (**arg(1, 1200336))
return "avg24094"