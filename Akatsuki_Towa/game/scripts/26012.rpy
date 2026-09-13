label avg26012(trans=fade_in):

$ play_music("ed7304.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1215572)]' (**arg(1, 1215572))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215573)]' (**arg(2, 1215573))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1215574)]' (**arg(3, 1215574))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215575)]' (**arg(4, 1215575))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215743)]' (**arg(5, 1215743))
get_char('c0') '[convertstrid(1215576)]' (**arg(6, 1215576))
get_char('c0') '[convertstrid(1215577)]' (**arg(7, 1215577))
get_char('c0') '[convertstrid(1215578)]' (**arg(8, 1215578))
get_char('c0') '[convertstrid(1215579)]' (**arg(9, 1215579))
return "avg26012"