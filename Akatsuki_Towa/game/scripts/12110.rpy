label avg12110(trans=fade_in):

$ play_music("ed7116.ogg")
scene avg_bg_020
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "other_7020.ogg"
get_char('c11') '[convertstrid(1128090)]' (**arg(1, 1128090))
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c2323') '[convertstrid(1128091)]' (**arg(2, 1128091))
hide p1
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128092)]' (**arg(3, 1128092))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c11') '[convertstrid(1128093)]' (**arg(4, 1128093))
hide p1
hide p232
get_char('c0') '[convertstrid(1128094)]' (**arg(5, 1128094))
$ update_portrait('st033_01 4', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1128095)]' (**arg(6, 1128095))
$ update_portrait('st033_01 4', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128096)]' (**arg(7, 1128096))
hide p232
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c5383') '[convertstrid(1128097)]' (**arg(8, 1128097))
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1128098)]' (**arg(9, 1128098))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128099)]' (**arg(10, 1128099))
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128100)]' (**arg(11, 1128100))
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128101)]' (**arg(12, 1128101))
hide p232
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
get_char('c5383') '[convertstrid(1128102)]' (**arg(13, 1128102, size=(1.2))) with shake
$ update_portrait('st033_01 3', 'p232', [r(-7), light], 6)
get_char('c2323') '[convertstrid(1128103)]' (**arg(14, 1128103))
$ update_portrait('st033_01 3', 'p232', [r(-7), dark], 5)
$ update_portrait('oc003_01 14', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128104)]' (**arg(15, 1128104))
scene avg_bg_070
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
with fade
play sfx2 "other_7020.ogg"
get_char('c33') '[convertstrid(1128105)]' (**arg(16, 1128105))
scene avg_bg_020
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1128106)]' (**arg(17, 1128106))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128107)]' (**arg(18, 1128107))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128108)]' (**arg(19, 1128108))
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128109)]' (**arg(20, 1128109))
return "avg12110"