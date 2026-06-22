label avg10075:

$ play_music("ED6103.ogg")
scene avg_bg_037
$ update_narrator('c11')
window show
with fade_in
$ update_portrait('oc001_01 9', 'p1', [l_entrance(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005193)]' (**arg(1, 1005193))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 4', 'p46', [r_entrance(-13), light], 6)
get_char('c463') '[convertstrid(1005194)]' (**arg(2, 1005194))
$ update_portrait('sc039_01 4', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1005195)]' (**arg(3, 1005195))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005196)]' (**arg(4, 1005196))
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005197)]' (**arg(5, 1005197))
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005198)]' (**arg(6, 1005198))
$ update_portrait('oc001_01 17', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005199)]' (**arg(7, 1005199))
hide p46
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005202)]' (**arg(8, 1005202))
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005203)]' (**arg(9, 1005203))
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c11') '[convertstrid(1005204)]' (**arg(10, 1005204))
$ update_portrait('oc001_01 16', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005205)]' (**arg(11, 1005205))
hide p2
$ update_portrait('oc001_01 16', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 8', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005206)]' (**arg(12, 1005206))
hide p1
$ update_portrait('sc039_01 8', 'p46', [r(-13), dark], 5)
$ update_portrait('sc040_01 10', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005207)]' (**arg(13, 1005207))
hide p47
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005208)]' (**arg(14, 1005208))
$ update_portrait('oc001_01 5', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc039_01 8', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005209)]' (**arg(15, 1005209))
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005210)]' (**arg(16, 1005210))
hide p1
$ update_portrait('sc039_01 4', 'p46', [r(-13), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
get_char('c471') '[convertstrid(1005211)]' (**arg(17, 1005211))
$ update_portrait('sc040_01 1', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('sc039_01 5', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005212)]' (**arg(18, 1005212))
return