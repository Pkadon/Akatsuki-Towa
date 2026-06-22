label avg12183:

$ play_music("ED6104.ogg")
scene avg_bg_023
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
$ update_narrator('c2091')
window show
with fade_in
play sfx2 "other_7021.ogg"
get_char('c2091') '[convertstrid(1120645)]' (**arg(1, 1120645))
$ update_portrait('st009_01 1', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120646)]' (**arg(2, 1120646))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1120647)]' (**arg(3, 1120647))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('st009_01 2', 'p209', [l(-22), light, flip], 6)
get_char('c2091') '[convertstrid(1120648)]' (**arg(4, 1120648))
$ update_portrait('st009_01 2', 'p209', [l(-22), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120649)]' (**arg(5, 1120649))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120650)]' (**arg(6, 1120650))
hide p209
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120651)]' (**arg(7, 1120651))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120652)]' (**arg(8, 1120652))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120653)]' (**arg(9, 1120653))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120654)]' (**arg(10, 1120654))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120655)]' (**arg(11, 1120655))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1120656)]' (**arg(12, 1120656))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120657)]' (**arg(13, 1120657))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120658)]' (**arg(14, 1120658))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120659)]' (**arg(15, 1120659))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1120660)]' (**arg(16, 1120660))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1120661)]' (**arg(17, 1120661))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st009_01 1', 'p209', [l(-22), light, flip], 6)
get_char('c2091') '[convertstrid(1120662)]' (**arg(18, 1120662))
return