label avg12370:

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c10741')
window show
with fade_in
play sfx2 "other_7043.ogg"
get_char('c10741') '[convertstrid(1133852)]' (**arg(1, 1133852))
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133853)]' (**arg(2, 1133853))
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7021.ogg"
get_char('c11') '[convertstrid(1133854)]' (**arg(3, 1133854))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c10743') '[convertstrid(1133855)]' (**arg(4, 1133855))
hide p1
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133856)]' (**arg(5, 1133856))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
get_char('c10743') '[convertstrid(1133857)]' (**arg(6, 1133857))
get_char('c10743') '[convertstrid(1133858)]' (**arg(7, 1133858))
hide p3
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133859)]' (**arg(8, 1133859))
hide p4
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133860)]' (**arg(9, 1133860))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
get_char('c10743') '[convertstrid(1133861)]' (**arg(10, 1133861))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133862)]' (**arg(11, 1133862))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133863)]' (**arg(12, 1133863))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133864)]' (**arg(13, 1133864))
hide p2
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133865)]' (**arg(14, 1133865))
hide p3
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1133866)]' (**arg(15, 1133866))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1133867)]' (**arg(16, 1133867))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
get_char('c10743') '[convertstrid(1133868)]' (**arg(17, 1133868))
get_char('c10743') '[convertstrid(1133869)]' (**arg(18, 1133869))
hide p1
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c41') '[convertstrid(1133870)]' (**arg(19, 1133870))
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 5)
get_char('c10743') '[convertstrid(1133871)]' (**arg(20, 1133871))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
get_char('c31') '[convertstrid(1133872)]' (**arg(21, 1133872))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
get_char('c10743') '[convertstrid(1133873)]' (**arg(22, 1133873)) with shake
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133874)]' (**arg(23, 1133874))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1133875)]' (**arg(24, 1133875))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133876)]' (**arg(25, 1133876))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133877)]' (**arg(26, 1133877))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133878)]' (**arg(27, 1133878))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1133879)]' (**arg(28, 1133879))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
play sfx2 "common_quest.ogg"
get_char('c10743') '[convertstrid(1133880)]' (**arg(29, 1133880))
return