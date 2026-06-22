label avg12177:

$ play_music("ED6104.ogg")
scene avg_bg_038
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1120544)]' (**arg(1, 1120544))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120545)]' (**arg(2, 1120545))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1120546)]' (**arg(3, 1120546))
hide p1
$ update_portrait('oc003_01 7', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1120547)]' (**arg(4, 1120547))
hide p2
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120548)]' (**arg(5, 1120548))
hide p3
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120549)]' (**arg(6, 1120549))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120550)]' (**arg(7, 1120550))
hide p1
hide p2
play sfx2 "common_remind.ogg"
get_char('c0') '[convertstrid(1120551)]' (**arg(8, 1120551))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120552)]' (**arg(9, 1120552))
return