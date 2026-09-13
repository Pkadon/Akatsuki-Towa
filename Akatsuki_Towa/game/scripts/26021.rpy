label avg26021(trans=fade_in):

$ play_music("ed7305.ogg")
scene avg_bg_051
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215641)]' (**arg(1, 1215641))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215642)]' (**arg(2, 1215642))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215643)]' (**arg(3, 1215643))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215644)]' (**arg(4, 1215644))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215645)]' (**arg(5, 1215645))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215646)]' (**arg(6, 1215646))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215647)]' (**arg(7, 1215647))
return "avg26021"