label avg10536:

$ play_music("ED6105.ogg")
scene avg_bg_102
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(1152560)]' (**arg(1, 1152560))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152561)]' (**arg(2, 1152561))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1152562)]' (**arg(3, 1152562))
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
play sfx2 "other_7085.ogg"
get_char('c12381') '[convertstrid(1152563)]' (**arg(4, 1152563))
hide p2
$ update_portrait('sc021_01 4', 'p29', [r(-17), light], 6)
get_char('c293') '[convertstrid(1152564)]' (**arg(5, 1152564))
$ update_portrait('sc021_01 4', 'p29', [r(-17), dark], 5)
get_char('c12381') '[convertstrid(1152565)]' (**arg(6, 1152565))
hide p29
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152566)]' (**arg(7, 1152566))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
get_char('c12381') '[convertstrid(1152567)]' (**arg(8, 1152567))
hide p1
$ update_portrait('sc021_01 4', 'p29', [r(-17), light], 6)
get_char('c293') '[convertstrid(1152568)]' (**arg(9, 1152568))
$ update_portrait('sc021_01 4', 'p29', [r(-17), dark], 5)
get_char('c12381') '[convertstrid(1152569)]' (**arg(10, 1152569))
hide p29
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1152570)]' (**arg(11, 1152570))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1152571)]' (**arg(12, 1152571))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
get_char('c291') '[convertstrid(1152572)]' (**arg(13, 1152572))
return