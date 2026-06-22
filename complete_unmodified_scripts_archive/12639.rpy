label avg12639:

$ play_music("ed7203.ogg")
scene avg_bg_070
$ update_narrator('c13251')
window show
with fade_in
get_char('c13251') '[convertstrid(1162989)]' (**arg(1, 1162989))
get_char('c13251') '[convertstrid(1162990)]' (**arg(2, 1162990))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162991)]' (**arg(3, 1162991))
hide p1
get_char('c0') '[convertstrid(1162992)]' (**arg(4, 1162992))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1162993)]' (**arg(5, 1162993))
$ play_music("ed7511.ogg")
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1162994)]' (**arg(6, 1162994))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7034.ogg"
get_char('c5001') '[convertstrid(1162995)]' (**arg(7, 1162995)) with shake
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162996)]' (**arg(8, 1162996))
return