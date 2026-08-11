label avg12722(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1171747)]' (**arg(1, 1171747))
get_char('c0') '[convertstrid(1171748)]' (**arg(2, 1171748))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171749)]' (**arg(3, 1171749))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171750)]' (**arg(4, 1171750))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171751)]' (**arg(5, 1171751))
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171752)]' (**arg(6, 1171752))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171753)]' (**arg(7, 1171753))
return "avg12722"