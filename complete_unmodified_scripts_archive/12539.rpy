label avg12539(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_077
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1152901)]' (**arg(1, 1152901))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c471') '[convertstrid(1152902)]' (**arg(2, 1152902))
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152903)]' (**arg(3, 1152903))
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1152904)]' (**arg(4, 1152904))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
get_char('c471') '[convertstrid(1152905)]' (**arg(5, 1152905))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r_entrance(-6), light], 6)
get_char('c33') '[convertstrid(1152906)]' (**arg(6, 1152906))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c471') '[convertstrid(1152907)]' (**arg(7, 1152907))
get_char('c471') '[convertstrid(1152908)]' (**arg(8, 1152908))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152909)]' (**arg(9, 1152909))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c471') '[convertstrid(1152910)]' (**arg(10, 1152910))
return "avg12539"