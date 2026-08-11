label avg12838(trans=fade_in):

$ play_music("ED6301.ogg")
scene avg_bg_218
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1186131)]' (**arg(1, 1186131))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1186132)]' (**arg(2, 1186132))
hide p2
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1186133)]' (**arg(3, 1186133))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1186134)]' (**arg(4, 1186134))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1186135)]' (**arg(5, 1186135))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1186136)]' (**arg(6, 1186136))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1186137)]' (**arg(7, 1186137))
hide p3
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1186138)]' (**arg(8, 1186138))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1186139)]' (**arg(9, 1186139))
return "avg12838"