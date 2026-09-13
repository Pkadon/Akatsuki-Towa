label avg26026(trans=fade_in):

$ play_music("ED6201.ogg")
scene avg_bg_004
$ update_narrator('c23')
window show
with trans
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1215669)]' (**arg(1, 1215669))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215670)]' (**arg(2, 1215670))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1215671)]' (**arg(3, 1215671))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1215672)]' (**arg(4, 1215672))
hide p1
hide p2
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1215750)]' (**arg(5, 1215750))
get_char('c0') '[convertstrid(1215673)]' (**arg(6, 1215673))
get_char('c0') '[convertstrid(1215674)]' (**arg(7, 1215674))
return "avg26026"