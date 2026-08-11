label avg12246(trans=fade_in):

$ play_music("ed7111.ogg")
scene avg_bg_012
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121316)]' (**arg(1, 1121316))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c50113') '[convertstrid(1121317)]' (**arg(2, 1121317))
get_char('c50113') '[convertstrid(1121318)]' (**arg(3, 1121318))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121319)]' (**arg(4, 1121319))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c50113') '[convertstrid(1121320)]' (**arg(5, 1121320))
get_char('c50113') '[convertstrid(1121321)]' (**arg(6, 1121321))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121322)]' (**arg(7, 1121322))
hide p1
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121323)]' (**arg(8, 1121323))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
get_char('c50113') '[convertstrid(1121324)]' (**arg(9, 1121324))
return "avg12246"