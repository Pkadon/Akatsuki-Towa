label avg12732:

$ play_music("ed7117.ogg")
scene avg_bg_011
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1172099)]' (**arg(1, 1172099))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172100)]' (**arg(2, 1172100))
hide p3
get_char('c0') '[convertstrid(1172101)]' (**arg(3, 1172101))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172102)]' (**arg(4, 1172102))
hide p1
get_char('c7493') '[convertstrid(1172103)]' (**arg(5, 1172103))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172104)]' (**arg(6, 1172104))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
get_char('c7493') '[convertstrid(1172105)]' (**arg(7, 1172105))
hide p3
get_char('c0') '[convertstrid(1172106)]' (**arg(8, 1172106))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172107)]' (**arg(9, 1172107))
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172108)]' (**arg(10, 1172108))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172109)]' (**arg(11, 1172109))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172110)]' (**arg(12, 1172110))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172111)]' (**arg(13, 1172111))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c5001') '[convertstrid(1172112)]' (**arg(14, 1172112)) with shake
get_char('c7491') '[convertstrid(1172113)]' (**arg(15, 1172113))
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6022.ogg"
get_char('c13') '[convertstrid(1172114)]' (**arg(16, 1172114))
hide p1
play sfx2 "other_7052.ogg"
get_char('c0') '[convertstrid(1172115)]' (**arg(17, 1172115))
get_char('c7491') '[convertstrid(1172116)]' (**arg(18, 1172116))
get_char('c0') '[convertstrid(1172117)]' (**arg(19, 1172117))
get_char('c14381') '[convertstrid(1172118)]' (**arg(20, 1172118))
get_char('c14393') '[convertstrid(1172119)]' (**arg(21, 1172119))
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172120)]' (**arg(22, 1172120))
$ update_portrait('oc003_01 21', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172121)]' (**arg(23, 1172121))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172122)]' (**arg(24, 1172122))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c14401') '[convertstrid(1172123)]' (**arg(25, 1172123))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172124)]' (**arg(26, 1172124))
hide p3
hide p1
play sfx2 "fight_6024.ogg"
get_char('c0') '[convertstrid(1172125)]' (**arg(27, 1172125))
return