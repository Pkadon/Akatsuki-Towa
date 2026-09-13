label avg26002(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c23')
$ update_portrait('oc002_01 3', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 3', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215510)]' (**arg(1, 1215510))
$ update_portrait('oc002_01 3', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215511)]' (**arg(2, 1215511))
return "avg26002"