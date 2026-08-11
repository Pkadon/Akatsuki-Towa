label avg12202(trans=fade_in):

$ play_music("ed7104.ogg")
scene avg_bg_039
$ update_narrator('c2253')
window show
with trans
$ update_portrait('st026_01 1', 'p225', [r_entrance(-14), light], 6)
play sfx2 "other_7047.ogg"
get_char('c2253') '[convertstrid(1128668)]' (**arg(1, 1128668))
hide p225
$ update_portrait('oc001_01 21', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128669)]' (**arg(2, 1128669))
hide p1
$ update_portrait('st026_01 2', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1128670)]' (**arg(3, 1128670))
$ update_portrait('st026_01 2', 'p225', [r(-14), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128671)]' (**arg(4, 1128671))
hide p225
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1128672)]' (**arg(5, 1128672))
hide p1
$ update_portrait('st026_01 4', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1128673)]' (**arg(6, 1128673))
hide p2
$ update_portrait('st026_01 4', 'p225', [r(-14), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1128674)]' (**arg(7, 1128674))
$ update_portrait('sc039_01 2', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('st026_01 4', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1128675)]' (**arg(8, 1128675))
hide p46
$ update_portrait('st026_01 4', 'p225', [r(-14), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na16.ogg"
get_char('c11') '[convertstrid(1128676)]' (**arg(9, 1128676))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1128677)]' (**arg(10, 1128677))
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1128678)]' (**arg(11, 1128678))
hide p1
hide p225
get_char('c0') '[convertstrid(1128679)]' (**arg(12, 1128679))
return "avg12202"