label avg1085:

$ play_music("ed7202.ogg")
scene avg_bg_079
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
get_char('c41') '[convertstrid(2101857)]' (**arg(1, 2101857))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101858)]' (**arg(2, 2101858))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101859)]' (**arg(3, 2101859))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101860)]' (**arg(4, 2101860))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101861)]' (**arg(5, 2101861))
hide p4
hide p1
get_char('c0') '[convertstrid(2101862)]' (**arg(6, 2101862))
$ update_portrait('oc004_01 7', 'p4', [l_midback(-5), light, flip], 6)
play sfx2 "other_7007.ogg"
play sfxvoice "avg_vocal_li26.ogg"
get_char('c41') '[convertstrid(2101863)]' (**arg(7, 2101863))
stop music
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101864)]' (**arg(8, 2101864))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101865)]' (**arg(9, 2101865))
$ play_music("ed7511.ogg")
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101866)]' (**arg(10, 2101866))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101867)]' (**arg(11, 2101867))
hide p4
play sfx2 "fight_6002.ogg"
get_char('c10871') '[convertstrid(2101868)]' (**arg(12, 2101868)) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c13') '[convertstrid(2101869)]' (**arg(13, 2101869))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li23.ogg"
get_char('c41') '[convertstrid(2101870)]' (**arg(14, 2101870))
return