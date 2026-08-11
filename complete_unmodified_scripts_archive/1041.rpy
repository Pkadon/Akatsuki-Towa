label avg1041(trans=fade_in):

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(2100641)]' (**arg(1, 2100641))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100642)]' (**arg(2, 2100642))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100643)]' (**arg(3, 2100643))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100644)]' (**arg(4, 2100644))
hide p56
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100645)]' (**arg(5, 2100645))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100646)]' (**arg(6, 2100646))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100647)]' (**arg(7, 2100647))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100648)]' (**arg(8, 2100648))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100649)]' (**arg(9, 2100649))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100650)]' (**arg(10, 2100650))
hide p56
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100651)]' (**arg(11, 2100651))
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100652)]' (**arg(12, 2100652))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100653)]' (**arg(13, 2100653))
return "avg1041"