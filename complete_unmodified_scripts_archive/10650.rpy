label avg10650:

$ play_music("ed7111.ogg")
scene avg_bg_054
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1164734)]' (**arg(1, 1164734))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st027_01 1', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164735)]' (**arg(2, 1164735))
hide p2
$ update_portrait('st027_01 1', 'p226', [l(5), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164736)]' (**arg(3, 1164736))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st027_01 2', 'p226', [l(5), l_shake, light, flip], 6)
get_char('c2261') '[convertstrid(1164737)]' (**arg(4, 1164737))
hide p4
$ update_portrait('st027_01 2', 'p226', [l(5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164738)]' (**arg(5, 1164738))
hide p1
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164739)]' (**arg(6, 1164739))
hide p226
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1164740)]' (**arg(7, 1164740))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164741)]' (**arg(8, 1164741)) with shake
hide p2
hide p4
get_char('c0') '[convertstrid(1164742)]' (**arg(9, 1164742))
$ update_portrait('st027_01 1', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164743)]' (**arg(10, 1164743))
$ update_portrait('st027_01 1', 'p226', [l(5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164744)]' (**arg(11, 1164744))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st027_01 1', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164745)]' (**arg(12, 1164745))
hide p1
$ update_portrait('st027_01 1', 'p226', [l(5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1164746)]' (**arg(13, 1164746))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('st027_01 5', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164747)]' (**arg(14, 1164747))
hide p2
$ update_portrait('st027_01 5', 'p226', [l(5), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164748)]' (**arg(15, 1164748))
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st027_01 1', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164749)]' (**arg(16, 1164749))
$ update_portrait('st027_01 1', 'p226', [l(5), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1164750)]' (**arg(17, 1164750))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('st027_01 5', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164751)]' (**arg(18, 1164751))
$ update_portrait('st027_01 5', 'p226', [l(5), light, flip], 6)
get_char('c2261') '[convertstrid(1164752)]' (**arg(19, 1164752))
return