label avg12217:

$ play_music("ED6103.ogg")
scene avg_bg_072
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7047.ogg"
get_char('c13') '[convertstrid(1120914)]' (**arg(1, 1120914))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6871') '[convertstrid(1120915)]' (**arg(2, 1120915))
play sfx2 "other_7004.ogg"
get_char('c6871') '[convertstrid(1120916)]' (**arg(3, 1120916))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120917)]' (**arg(4, 1120917))
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121479)]' (**arg(5, 1121479))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
get_char('c6871') '[convertstrid(1121480)]' (**arg(6, 1121480))
hide p2
$ update_portrait('oc004_01 12', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121481)]' (**arg(7, 1121481))
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1121482)]' (**arg(8, 1121482))
hide p4
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc040_01 1', 'p47', [r(-9), light], 6)
get_char('c473') '[convertstrid(1120918)]' (**arg(9, 1120918))
hide p46
$ update_portrait('sc040_01 1', 'p47', [r(-9), dark], 5)
get_char('c6871') '[convertstrid(1121483)]' (**arg(10, 1121483))
get_char('c6871') '[convertstrid(1120919)]' (**arg(11, 1120919))
get_char('c6871') '[convertstrid(1120920)]' (**arg(12, 1120920))
hide p47
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120921)]' (**arg(13, 1120921))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120922)]' (**arg(14, 1120922))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121562)]' (**arg(15, 1121562))
hide p1
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121563)]' (**arg(16, 1121563))
hide p2
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1121564)]' (**arg(17, 1121564))
hide p46
$ update_portrait('sc040_01 4', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1121565)]' (**arg(18, 1121565))
hide p4
$ update_portrait('sc040_01 4', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121566)]' (**arg(19, 1121566))
hide p47
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c6871') '[convertstrid(1121567)]' (**arg(20, 1121567))
get_char('c6871') '[convertstrid(1121568)]' (**arg(21, 1121568))
get_char('c6871') '[convertstrid(1121569)]' (**arg(22, 1121569))
return