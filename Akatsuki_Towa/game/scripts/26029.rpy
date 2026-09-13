label avg26029(trans=fade_in):

$ play_music("ed7200.ogg")
scene avg_bg_026
$ update_narrator('c23')
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215695)]' (**arg(1, 1215695))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215696)]' (**arg(2, 1215696))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215697)]' (**arg(3, 1215697))
return "avg26029"