label avg12239:

$ play_music("ed7103.ogg")
scene avg_bg_018
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
get_char('c11') '[convertstrid(1121498)]' (**arg(1, 1121498))
$ update_portrait('oc001_01 17', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121201)]' (**arg(2, 1121201))
$ update_portrait('oc001_01 17', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
play sfx2 "other_7071.ogg"
get_char('c23') '[convertstrid(1121202)]' (**arg(3, 1121202))
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1121203)]' (**arg(4, 1121203))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfx2 "other_7072.ogg"
get_char('c23') '[convertstrid(1121204)]' (**arg(5, 1121204))
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121205)]' (**arg(6, 1121205))
hide p2
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c5243') '[convertstrid(1121499)]' (**arg(7, 1121499))
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121206)]' (**arg(8, 1121206))
$ update_portrait('oc001_01 9', 'p1', [l(-2), dark, flip], 5)
get_char('c5243') '[convertstrid(1121207)]' (**arg(9, 1121207))
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121208)]' (**arg(10, 1121208))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c5243') '[convertstrid(1121500)]' (**arg(11, 1121500))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121209)]' (**arg(12, 1121209))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c5243') '[convertstrid(1121210)]' (**arg(13, 1121210))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7073.ogg"
get_char('c11') '[convertstrid(1121211)]' (**arg(14, 1121211))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 7', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121212)]' (**arg(15, 1121212))
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 19', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121501)]' (**arg(16, 1121501))
return