label avg26011(trans=fade_in):

$ play_music("ed7304.ogg")
scene placeholderbackground
$ update_narrator('c11')
$ update_portrait('oc001_01 15', 'p1', [l(-2), light, flip], 6)
window show
with trans
$ update_portrait('oc001_01 15', 'p1', [l_midback(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215566)]' (**arg(1, 1215566))
$ update_portrait('oc001_01 15', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 19', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215567)]' (**arg(2, 1215567))
$ update_portrait('oc002_01 19', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215568)]' (**arg(3, 1215568))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215755)]' (**arg(4, 1215755))
get_char('c0') '[convertstrid(1215569)]' (**arg(5, 1215569))
get_char('c0') '[convertstrid(1215570)]' (**arg(6, 1215570))
get_char('c0') '[convertstrid(1215571)]' (**arg(7, 1215571))
return "avg26011"