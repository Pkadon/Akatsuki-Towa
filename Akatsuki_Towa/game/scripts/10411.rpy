label avg10411(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_054
$ update_portrait('st034_01 2', 'p233', [l(12), light, flip], 6)
$ update_narrator('c2331')
window show
with trans
play sfx2 "other_7046.ogg"
get_char('c2331') '[convertstrid(1140649)]' (**arg(1, 1140649))
$ update_portrait('st034_01 2', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1140650)]' (**arg(2, 1140650))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st034_01 1', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1140651)]' (**arg(3, 1140651))
$ update_portrait('st034_01 4', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1140652)]' (**arg(4, 1140652))
hide p1
$ update_portrait('st034_01 4', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140653)]' (**arg(5, 1140653))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st034_01 4', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1140654)]' (**arg(6, 1140654))
$ update_portrait('st034_01 4', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1140655)]' (**arg(7, 1140655))
hide p2
$ update_portrait('st034_01 4', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140656)]' (**arg(8, 1140656))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140657)]' (**arg(9, 1140657))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1140658)]' (**arg(10, 1140658))
hide p2
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c33') '[convertstrid(1140659)]' (**arg(11, 1140659))
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('st034_01 4', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1140660)]' (**arg(12, 1140660))
$ update_portrait('st034_01 1', 'p233', [l(12), light, flip], 6)
get_char('c2331') '[convertstrid(1140661)]' (**arg(13, 1140661))
$ update_portrait('st034_01 1', 'p233', [l(12), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c33') '[convertstrid(1140662)]' (**arg(14, 1140662))
return "avg10411"