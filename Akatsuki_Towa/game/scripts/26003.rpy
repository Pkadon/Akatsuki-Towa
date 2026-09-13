label avg26003(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c23')
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 9', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1215512)]' (**arg(1, 1215512))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215513)]' (**arg(2, 1215513))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1215514)]' (**arg(3, 1215514))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215737)]' (**arg(4, 1215737))
get_char('c0') '[convertstrid(1215515)]' (**arg(5, 1215515))
get_char('c0') '[convertstrid(1215516)]' (**arg(6, 1215516))
get_char('c0') '[convertstrid(1215517)]' (**arg(7, 1215517))
return "avg26003"