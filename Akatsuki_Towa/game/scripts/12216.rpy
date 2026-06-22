label avg12216:

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7042.ogg"
get_char('c11') '[convertstrid(1120901)]' (**arg(1, 1120901))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
get_char('c9893') '[convertstrid(1120902)]' (**arg(2, 1120902))
get_char('c9883') '[convertstrid(1121477)]' (**arg(3, 1121477))
hide p1
get_char('c9881') '[convertstrid(1121478)]' (**arg(4, 1121478))
get_char('c9893') '[convertstrid(1120903)]' (**arg(5, 1120903))
get_char('c9881') '[convertstrid(1120904)]' (**arg(6, 1120904))
get_char('c9893') '[convertstrid(1120905)]' (**arg(7, 1120905))
get_char('c9893') '[convertstrid(1120906)]' (**arg(8, 1120906))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120907)]' (**arg(9, 1120907))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c9883') '[convertstrid(1120908)]' (**arg(10, 1120908))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120909)]' (**arg(11, 1120909))
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1120910)]' (**arg(12, 1120910))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120911)]' (**arg(13, 1120911))
return