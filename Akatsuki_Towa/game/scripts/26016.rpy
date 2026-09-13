label avg26016(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 4', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1215604)]' (**arg(1, 1215604))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215605)]' (**arg(2, 1215605))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215606)]' (**arg(3, 1215606))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215607)]' (**arg(4, 1215607))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215608)]' (**arg(5, 1215608))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215609)]' (**arg(6, 1215609))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215610)]' (**arg(7, 1215610))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215746)]' (**arg(8, 1215746))
get_char('c0') '[convertstrid(1215611)]' (**arg(9, 1215611))
get_char('c0') '[convertstrid(1215612)]' (**arg(10, 1215612))
get_char('c0') '[convertstrid(1215613)]' (**arg(11, 1215613))
get_char('c0') '[convertstrid(1215614)]' (**arg(12, 1215614))
return "avg26016"