label avg14024:

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1202493)]' (**arg(1, 1202493))
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "fight_6019.ogg"
get_char('c21') '[convertstrid(1202494)]' (**arg(2, 1202494))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1202495)]' (**arg(3, 1202495))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202496)]' (**arg(4, 1202496))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202497)]' (**arg(5, 1202497))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202498)]' (**arg(6, 1202498))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202499)]' (**arg(7, 1202499))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202500)]' (**arg(8, 1202500))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202501)]' (**arg(9, 1202501))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202502)]' (**arg(10, 1202502))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202503)]' (**arg(11, 1202503))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202504)]' (**arg(12, 1202504))
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
with fade
get_char('c11') '[convertstrid(1202506)]' (**arg(13, 1202506))
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1202507)]' (**arg(14, 1202507))
return