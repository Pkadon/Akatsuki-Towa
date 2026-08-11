label avg1032(trans=fade_in):

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(2100562)]' (**arg(1, 2100562))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100563)]' (**arg(2, 2100563))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l_entrance(-25), light, flip], 6)
get_char('c591') '[convertstrid(2100564)]' (**arg(3, 2100564))
hide p1
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100565)]' (**arg(4, 2100565))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100566)]' (**arg(5, 2100566))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(2100567)]' (**arg(6, 2100567))
hide p2
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100568)]' (**arg(7, 2100568))
hide p59
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100569)]' (**arg(8, 2100569))
return "avg1032"