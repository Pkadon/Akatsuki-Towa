label avg26007(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1215548)]' (**arg(1, 1215548))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215549)]' (**arg(2, 1215549))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215741)]' (**arg(3, 1215741))
get_char('c0') '[convertstrid(1215550)]' (**arg(4, 1215550))
get_char('c0') '[convertstrid(1215551)]' (**arg(5, 1215551))
get_char('c0') '[convertstrid(1215552)]' (**arg(6, 1215552))
return "avg26007"