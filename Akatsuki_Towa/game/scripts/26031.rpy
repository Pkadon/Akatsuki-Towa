label avg26031(trans=fade_in):

$ play_music("ed7302.ogg")
scene avg_bg_212
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1215708)]' (**arg(1, 1215708))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215710)]' (**arg(2, 1215710))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215711)]' (**arg(3, 1215711))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215712)]' (**arg(4, 1215712))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215713)]' (**arg(5, 1215713))
return "avg26031"