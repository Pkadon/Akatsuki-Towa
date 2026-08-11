label avg12219(trans=fade_in):

$ play_music("ed7569.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1121486)]' (**arg(1, 1121486))
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1120938)]' (**arg(2, 1120938))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120939)]' (**arg(3, 1120939))
hide p1
hide p2
$ update_portrait('uc004_02 1', 'p993', [r(-6), light], 6)
$ update_narrator('c9933')
with fade
get_char('c9933') '[convertstrid(1120940)]' (**arg(4, 1120940))
$ update_portrait('uc004_02 1', 'p993', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1120941)]' (**arg(5, 1120941))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p993', [r(-6), light], 6)
get_char('c9933') '[convertstrid(1120942)]' (**arg(6, 1120942))
hide p4
$ update_portrait('uc004_02 1', 'p993', [r(-6), dark], 5)
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1120943)]' (**arg(7, 1120943))
$ update_portrait('sc039_01 8', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1120944)]' (**arg(8, 1120944))
$ update_portrait('sc039_01 8', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p993', [r(-6), light], 6)
get_char('c9933') '[convertstrid(1120945)]' (**arg(9, 1120945))
$ update_portrait('uc004_02 1', 'p993', [r(-6), dark], 5)
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1120946)]' (**arg(10, 1120946))
hide p993
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121570)]' (**arg(11, 1121570))
return "avg12219"