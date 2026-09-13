label avg26022(trans=fade_in):

$ play_music("ED6201.ogg")
scene avg_bg_004
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 12', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215648)]' (**arg(1, 1215648))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1215649)]' (**arg(2, 1215649))
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215650)]' (**arg(3, 1215650))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215651)]' (**arg(4, 1215651))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215652)]' (**arg(5, 1215652))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215653)]' (**arg(6, 1215653))
return "avg26022"