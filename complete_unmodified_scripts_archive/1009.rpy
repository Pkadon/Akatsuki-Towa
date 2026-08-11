label avg1009(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(2100117)]' (**arg(1, 2100117))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100118)]' (**arg(2, 2100118))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7036.ogg"
get_char('c561') '[convertstrid(2100119)]' (**arg(3, 2100119))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100120)]' (**arg(4, 2100120))
$ update_portrait('sc049_01 7', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100121)]' (**arg(5, 2100121))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100122)]' (**arg(6, 2100122))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100123)]' (**arg(7, 2100123))
return "avg1009"