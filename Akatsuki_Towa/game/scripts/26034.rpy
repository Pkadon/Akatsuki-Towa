label avg26034(trans=fade_in):

$ play_music("ed7302.ogg")
scene avg_bg_212
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1215726)]' (**arg(1, 1215726))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215731)]' (**arg(2, 1215731))
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215732)]' (**arg(3, 1215732))
return "avg26034"