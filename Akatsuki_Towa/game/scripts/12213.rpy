label avg12213:

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7042.ogg"
get_char('c11') '[convertstrid(1120860)]' (**arg(1, 1120860))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c10953') '[convertstrid(1120861)]' (**arg(2, 1120861))
hide p1
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121446)]' (**arg(3, 1121446))
$ update_portrait('oc002_01 15', 'p2', [l(-3), dark, flip], 5)
get_char('c10953') '[convertstrid(1120862)]' (**arg(4, 1120862))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1120863)]' (**arg(5, 1120863))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1120864)]' (**arg(6, 1120864))
hide p4
play sfx2 "other_7042.ogg"
get_char('c6483') '[convertstrid(1120865)]' (**arg(7, 1120865))
hide p3
get_char('c10951') '[convertstrid(1120866)]' (**arg(8, 1120866))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121447)]' (**arg(9, 1121447))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
get_char('c10951') '[convertstrid(1121448)]' (**arg(10, 1121448))
get_char('c10951') '[convertstrid(1120867)]' (**arg(11, 1120867))
hide p1
get_char('c0') '[convertstrid(1120868)]' (**arg(12, 1120868))
get_char('c9881') '[convertstrid(1120869)]' (**arg(13, 1120869))
get_char('c9881') '[convertstrid(1120870)]' (**arg(14, 1120870))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120871)]' (**arg(15, 1120871))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c9881') '[convertstrid(1120872)]' (**arg(16, 1120872))
get_char('c9881') '[convertstrid(1120873)]' (**arg(17, 1120873))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121449)]' (**arg(18, 1121449))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
get_char('c9881') '[convertstrid(1121450)]' (**arg(19, 1121450))
hide p2
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121451)]' (**arg(20, 1121451))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
get_char('c9881') '[convertstrid(1121452)]' (**arg(21, 1121452))
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121453)]' (**arg(22, 1121453))
$ update_portrait('oc004_01 8', 'p4', [r(-5), dark], 5)
get_char('c9881') '[convertstrid(1121454)]' (**arg(23, 1121454))
hide p4
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1121455)]' (**arg(24, 1121455))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121456)]' (**arg(25, 1121456))
hide p3
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121457)]' (**arg(26, 1121457))
return