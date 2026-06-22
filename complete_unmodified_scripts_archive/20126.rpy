label avg20126:

$ play_music("ed7103.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
play sfx2 "other_7047.ogg"
get_char('c561') '[convertstrid(1006575)]' (**arg(1, 1006575))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006576)]' (**arg(2, 1006576))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1006577)]' (**arg(3, 1006577))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006578)]' (**arg(4, 1006578))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006579)]' (**arg(5, 1006579))
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006580)]' (**arg(6, 1006580))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1006581)]' (**arg(7, 1006581))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1006582)]' (**arg(8, 1006582))
return