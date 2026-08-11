label avg20133(trans=fade_in):

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1006670)]' (**arg(1, 1006670))
$ update_portrait('sc051_01 4', 'p58', [r_entrance(-32), light], 6)
play sfx2 "other_7049.ogg"
get_char('c583') '[convertstrid(1006671)]' (**arg(2, 1006671))
$ update_portrait('sc051_01 4', 'p58', [r(-32), dark], 5)
$ update_portrait('sc050_01 4', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(1006672)]' (**arg(3, 1006672))
$ update_portrait('sc050_01 4', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('sc051_01 4', 'p58', [r(-32), light], 6)
get_char('c583') '[convertstrid(1006673)]' (**arg(4, 1006673))
hide p58
play sfx2 "elc_5005.ogg"
get_char('c6653') '[convertstrid(1004289)]' (**arg(5, 1004289))
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
get_char('c571') '[convertstrid(1006675)]' (**arg(6, 1006675))
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('sc051_01 2', 'p58', [r(-32), light], 6)
play sfx2 "fight_6003.ogg"
get_char('c583') '[convertstrid(1006676)]' (**arg(7, 1006676))
$ update_portrait('sc051_01 2', 'p58', [r(-32), dark], 5)
$ update_portrait('sc050_01 2', 'p57', [l(-19), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c571') '[convertstrid(1006677)]' (**arg(8, 1006677))
return "avg20133"