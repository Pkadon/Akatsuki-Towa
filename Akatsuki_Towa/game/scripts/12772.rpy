label avg12772(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1175638)]' (**arg(1, 1175638))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1175639)]' (**arg(2, 1175639))
hide p1
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175640)]' (**arg(3, 1175640))
hide p4
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175641)]' (**arg(4, 1175641))
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175642)]' (**arg(5, 1175642))
hide p3
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1175643)]' (**arg(6, 1175643))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175644)]' (**arg(7, 1175644))
return "avg12772"