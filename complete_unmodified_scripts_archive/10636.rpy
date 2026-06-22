label avg10636:

$ play_music("ed6324.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1164098)]' (**arg(1, 1164098))
scene avg_bg_070
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1164099)]' (**arg(2, 1164099))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164100)]' (**arg(3, 1164100))
hide p2
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164101)]' (**arg(4, 1164101))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164102)]' (**arg(5, 1164102))
hide p1304
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164103)]' (**arg(6, 1164103))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164104)]' (**arg(7, 1164104))
hide p4
$ update_portrait('sc010_01 4', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1164105)]' (**arg(8, 1164105))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1164106)]' (**arg(9, 1164106))
hide p18
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164107)]' (**arg(10, 1164107))
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 5', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1164108)]' (**arg(11, 1164108))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164109)]' (**arg(12, 1164109))
return