label avg12245(trans=fade_in):

$ play_music("ed7102.ogg")
scene avg_bg_015
$ update_narrator('c9963')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c9963') '[convertstrid(1121302)]' (**arg(1, 1121302))
$ update_portrait('oc004_01 9', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1121303)]' (**arg(2, 1121303))
hide p4
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121304)]' (**arg(3, 1121304))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c9963') '[convertstrid(1121305)]' (**arg(4, 1121305))
get_char('c9963') '[convertstrid(1121306)]' (**arg(5, 1121306))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121307)]' (**arg(6, 1121307))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1121308)]' (**arg(7, 1121308))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
get_char('c9963') '[convertstrid(1121309)]' (**arg(8, 1121309))
get_char('c9963') '[convertstrid(1121310)]' (**arg(9, 1121310))
hide p4
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121311)]' (**arg(10, 1121311))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121312)]' (**arg(11, 1121312))
return "avg12245"