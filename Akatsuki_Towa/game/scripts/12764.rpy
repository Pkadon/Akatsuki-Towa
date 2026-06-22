label avg12764:

$ play_music("ed7511.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1174636)]' (**arg(1, 1174636))
$ update_portrait('st061_01 3', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174637)]' (**arg(2, 1174637))
$ update_portrait('st061_01 3', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174638)]' (**arg(3, 1174638))
$ update_portrait('st061_01 3', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174639)]' (**arg(4, 1174639))
hide p1304
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174640)]' (**arg(5, 1174640))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174641)]' (**arg(6, 1174641))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1174642)]' (**arg(7, 1174642))
hide p1
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174643)]' (**arg(8, 1174643))
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1174644)]' (**arg(9, 1174644))
hide p1304
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174645)]' (**arg(10, 1174645))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174646)]' (**arg(11, 1174646))
hide p3
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1174647)]' (**arg(12, 1174647))
return