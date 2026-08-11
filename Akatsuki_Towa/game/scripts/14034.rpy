label avg14034(trans=fade_in):

$ play_music("ed7110.ogg")
scene avg_bg_019
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1202667)]' (**arg(1, 1202667))
get_char('c0') '[convertstrid(1202668)]' (**arg(2, 1202668))
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202669)]' (**arg(3, 1202669))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st023_01 5', 'p222', [l(-12), light, flip], 6)
get_char('c2221') '[convertstrid(1202670)]' (**arg(4, 1202670))
hide p222
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202671)]' (**arg(5, 1202671))
hide p2
$ update_portrait('st023_01 1', 'p222', [l(-12), light, flip], 6)
get_char('c2221') '[convertstrid(1202672)]' (**arg(6, 1202672))
$ update_portrait('st023_01 1', 'p222', [l(-12), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202673)]' (**arg(7, 1202673))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202674)]' (**arg(8, 1202674))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202675)]' (**arg(9, 1202675))
hide p1
$ update_portrait('oc002_01 20', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202676)]' (**arg(10, 1202676))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202677)]' (**arg(11, 1202677))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st023_01 1', 'p222', [l(-12), light, flip], 6)
get_char('c2221') '[convertstrid(1202678)]' (**arg(12, 1202678))
$ update_portrait('st023_01 6', 'p222', [l(-12), light, flip], 6)
get_char('c2221') '[convertstrid(1202679)]' (**arg(13, 1202679))
hide p222
hide p1
get_char('c0') '[convertstrid(1202680)]' (**arg(14, 1202680))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202681)]' (**arg(15, 1202681))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202682)]' (**arg(16, 1202682))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202683)]' (**arg(17, 1202683))
return "avg14034"