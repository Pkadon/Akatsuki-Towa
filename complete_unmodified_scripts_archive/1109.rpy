label avg1109:

$ play_music("ed7106.ogg")
scene avg_bg_006
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(2102670)]' (**arg(1, 2102670))
$ update_portrait('st008_01 6', 'p208', [l(-19), light, flip], 6)
play sfx2 "other_7046.ogg"
get_char('c2081') '[convertstrid(2102671)]' (**arg(2, 2102671))
$ update_portrait('st008_01 1', 'p208', [l(-19), light, flip], 6)
get_char('c2081') '[convertstrid(2102672)]' (**arg(3, 2102672))
hide p208
$ update_portrait('st003_01 1', 'p203', [l(-7), light, flip], 6)
get_char('c2031') '[convertstrid(2102673)]' (**arg(4, 2102673))
$ update_portrait('st003_01 1', 'p203', [l(-7), dark, flip], 5)
get_char('c10893') '[convertstrid(2102674)]' (**arg(5, 2102674))
$ update_portrait('st003_01 5', 'p203', [l(-7), light, flip], 6)
get_char('c2031') '[convertstrid(2102675)]' (**arg(6, 2102675))
hide p203
$ update_portrait('st007_01 5', 'p207', [l(-6), light, flip], 6)
get_char('c2071') '[convertstrid(2102676)]' (**arg(7, 2102676))
$ update_portrait('st007_01 5', 'p207', [l(-6), light, flip], 6)
get_char('c2071') '[convertstrid(2102677)]' (**arg(8, 2102677))
hide p207
get_char('c0') '[convertstrid(2102678)]' (**arg(9, 2102678))
$ update_portrait('st004_01 5', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102679)]' (**arg(10, 2102679))
$ update_portrait('st004_01 5', 'p204', [l(4), dark, flip], 5)
get_char('c9773') '[convertstrid(2102680)]' (**arg(11, 2102680))
hide p204
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2102681)]' (**arg(12, 2102681))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102682)]' (**arg(13, 2102682))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2102683)]' (**arg(14, 2102683))
$ update_portrait('oc002_01 16', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102684)]' (**arg(15, 2102684))
hide p1
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2102685)]' (**arg(16, 2102685))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st003_01 1', 'p203', [l(-7), light, flip], 6)
get_char('c2031') '[convertstrid(2102686)]' (**arg(17, 2102686))
hide p4
$ update_portrait('st003_01 1', 'p203', [l(-7), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2102687)]' (**arg(18, 2102687))
hide p203
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st004_01 5', 'p204', [l(4), light, flip], 6)
get_char('c2041') '[convertstrid(2102688)]' (**arg(19, 2102688))
return