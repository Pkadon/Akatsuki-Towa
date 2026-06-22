label avg1008:

$ play_music("ed7106.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(2100109)]' (**arg(1, 2100109))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7037.ogg"
get_char('c561') '[convertstrid(2100110)]' (**arg(2, 2100110))
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100111)]' (**arg(3, 2100111))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100112)]' (**arg(4, 2100112))
$ update_portrait('sc049_01 7', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100113)]' (**arg(5, 2100113))
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(2100114)]' (**arg(6, 2100114))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100115)]' (**arg(7, 2100115))
return