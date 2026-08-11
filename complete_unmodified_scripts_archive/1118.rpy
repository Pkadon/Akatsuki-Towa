label avg1118(trans=fade_in):

$ play_music("ed7124.ogg")
scene avg_bg_059
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2102908)]' (**arg(1, 2102908))
$ update_portrait('oc001_01 1', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2102909)]' (**arg(2, 2102909))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(2102910)]' (**arg(3, 2102910))
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(2102911)]' (**arg(4, 2102911))
hide p3
get_char('c10061') '[convertstrid(2102912)]' (**arg(5, 2102912))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2102913)]' (**arg(6, 2102913))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c31') '[convertstrid(2102914)]' (**arg(7, 2102914))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102915)]' (**arg(8, 2102915))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(2102916)]' (**arg(9, 2102916))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102917)]' (**arg(10, 2102917))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2102918)]' (**arg(11, 2102918))
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2102919)]' (**arg(12, 2102919))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2102920)]' (**arg(13, 2102920))
scene avg_bg_070
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(2102921)]' (**arg(14, 2102921))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2102922)]' (**arg(15, 2102922))
return "avg1118"