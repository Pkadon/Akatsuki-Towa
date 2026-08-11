label avg12728(trans=fade_in):

stop music
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1171904)]' (**arg(1, 1171904))
get_char('c0') '[convertstrid(1171905)]' (**arg(2, 1171905))
get_char('c0') '[convertstrid(1171906)]' (**arg(3, 1171906))
$ play_music("ed7516.ogg")
scene avg_bg_050
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1171907)]' (**arg(4, 1171907))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171908)]' (**arg(5, 1171908))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1171909)]' (**arg(6, 1171909))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171910)]' (**arg(7, 1171910))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1171911)]' (**arg(8, 1171911))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171912)]' (**arg(9, 1171912))
hide p3
hide p1
play sfx2 "other_7044.ogg"
get_char('c0') '[convertstrid(1171913)]' (**arg(10, 1171913))
play sfx2 "other_7047.ogg"
get_char('c14361') '[convertstrid(1171914)]' (**arg(11, 1171914))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171915)]' (**arg(12, 1171915))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c14361') '[convertstrid(1171916)]' (**arg(13, 1171916))
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1171917)]' (**arg(14, 1171917))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c14361') '[convertstrid(1171918)]' (**arg(15, 1171918))
get_char('c14351') '[convertstrid(1171919)]' (**arg(16, 1171919))
get_char('c14361') '[convertstrid(1171920)]' (**arg(17, 1171920))
get_char('c14371') '[convertstrid(1171921)]' (**arg(18, 1171921))
hide p3
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171922)]' (**arg(19, 1171922))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171923)]' (**arg(20, 1171923))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c14371') '[convertstrid(1171924)]' (**arg(21, 1171924))
get_char('c14371') '[convertstrid(1171925)]' (**arg(22, 1171925))
hide p1
$ update_portrait('oc003_01 16', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1171926)]' (**arg(23, 1171926))
$ update_portrait('oc003_01 16', 'p3', [r(-6), dark], 5)
get_char('c14371') '[convertstrid(1171927)]' (**arg(24, 1171927))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1171928)]' (**arg(25, 1171928))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
get_char('c14371') '[convertstrid(1171929)]' (**arg(26, 1171929))
get_char('c14371') '[convertstrid(1171930)]' (**arg(27, 1171930))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1171931)]' (**arg(28, 1171931))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
get_char('c14361') '[convertstrid(1171932)]' (**arg(29, 1171932))
hide p3
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171933)]' (**arg(30, 1171933))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171934)]' (**arg(31, 1171934))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
get_char('c14371') '[convertstrid(1171935)]' (**arg(32, 1171935))
get_char('c14371') '[convertstrid(1171936)]' (**arg(33, 1171936))
hide p1
get_char('c14363') '[convertstrid(1171937)]' (**arg(34, 1171937))
get_char('c14371') '[convertstrid(1171938)]' (**arg(35, 1171938))
get_char('c14363') '[convertstrid(1171939)]' (**arg(36, 1171939))
get_char('c14371') '[convertstrid(1171940)]' (**arg(37, 1171940))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171941)]' (**arg(38, 1171941))
return "avg12728"