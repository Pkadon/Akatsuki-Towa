label avg12611:

$ play_music("ed7111.ogg")
scene avg_bg_012
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1161439)]' (**arg(1, 1161439))
$ update_portrait('oc003_01 13', 'p3', [r_entrance(-6), light], 6)
play sfx2 "other_7046.ogg"
get_char('c33') '[convertstrid(1161440)]' (**arg(2, 1161440))
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
get_char('c7091') '[convertstrid(1161441)]' (**arg(3, 1161441))
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161442)]' (**arg(4, 1161442))
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161443)]' (**arg(5, 1161443))
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
get_char('c7091') '[convertstrid(1161444)]' (**arg(6, 1161444))
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1161445)]' (**arg(7, 1161445))
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161446)]' (**arg(8, 1161446))
hide p709
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161447)]' (**arg(9, 1161447))
return