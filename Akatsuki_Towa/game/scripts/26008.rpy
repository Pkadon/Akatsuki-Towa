label avg26008(trans=fade_in):

$ play_music("ed7304.ogg")
scene placeholderbackground
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215553)]' (**arg(1, 1215553))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215554)]' (**arg(2, 1215554))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215555)]' (**arg(3, 1215555))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215556)]' (**arg(4, 1215556))
return "avg26008"