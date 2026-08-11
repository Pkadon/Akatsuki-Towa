label avg10412(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with trans
play sfx2 "other_7047.ogg"
get_char('c561') '[convertstrid(1140664)]' (**arg(1, 1140664))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1140665)]' (**arg(2, 1140665))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1140666)]' (**arg(3, 1140666))
hide p2
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140667)]' (**arg(4, 1140667))
hide p56
hide p1
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1140668)]' (**arg(5, 1140668))
$ update_portrait('sc049_01 11', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1140669)]' (**arg(6, 1140669))
$ update_portrait('sc049_01 11', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140670)]' (**arg(7, 1140670))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1140671)]' (**arg(8, 1140671))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140672)]' (**arg(9, 1140672))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140673)]' (**arg(10, 1140673))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1140674)]' (**arg(11, 1140674))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140675)]' (**arg(12, 1140675))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c23') '[convertstrid(1140676)]' (**arg(13, 1140676))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140677)]' (**arg(14, 1140677))
hide p2
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140678)]' (**arg(15, 1140678))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1140679)]' (**arg(16, 1140679))
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140680)]' (**arg(17, 1140680))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1140681)]' (**arg(18, 1140681))
return "avg10412"