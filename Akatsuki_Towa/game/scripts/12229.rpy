label avg12229(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_072
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1121093)]' (**arg(1, 1121093))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1121094)]' (**arg(2, 1121094))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121095)]' (**arg(3, 1121095))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121096)]' (**arg(4, 1121096))
hide p1
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121097)]' (**arg(5, 1121097))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121098)]' (**arg(6, 1121098))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121099)]' (**arg(7, 1121099))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121100)]' (**arg(8, 1121100))
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121581)]' (**arg(9, 1121581))
hide p2
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121101)]' (**arg(10, 1121101))
return "avg12229"