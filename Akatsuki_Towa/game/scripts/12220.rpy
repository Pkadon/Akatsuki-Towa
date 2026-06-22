label avg12220:

$ play_music("ed7569.ogg")
scene avg_bg_036
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1121571)]' (**arg(1, 1121571))
$ update_portrait('oc002_01 12', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120948)]' (**arg(2, 1120948))
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120949)]' (**arg(3, 1120949))
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120950)]' (**arg(4, 1120950))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1120951)]' (**arg(5, 1120951))
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc040_01 8', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1120952)]' (**arg(6, 1120952))
hide p4
$ update_portrait('sc040_01 8', 'p47', [r(-9), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1120953)]' (**arg(7, 1120953))
hide p46
hide p47
$ update_portrait('uc004_02 2', 'p991', [r(-6), light], 6)
$ update_narrator('c9913')
with fade
get_char('c9913') '[convertstrid(1120954)]' (**arg(8, 1120954))
$ update_portrait('uc004_02 2', 'p991', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120955)]' (**arg(9, 1120955))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p991', [r(-6), light], 6)
get_char('c9913') '[convertstrid(1120956)]' (**arg(10, 1120956))
hide p1
$ update_portrait('uc004_02 1', 'p991', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120957)]' (**arg(11, 1120957))
hide p991
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1120958)]' (**arg(12, 1120958))
hide p2
$ update_portrait('oc004_01 15', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121572)]' (**arg(13, 1121572))
return