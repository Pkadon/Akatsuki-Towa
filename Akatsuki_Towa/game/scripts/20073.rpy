label avg20073(trans=fade_in):

$ play_music("ed7117.ogg")
scene avg_bg_021
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1003930)]' (**arg(1, 1003930))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003931)]' (**arg(2, 1003931))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003932)]' (**arg(3, 1003932))
hide p1
hide p3
get_char('c0') '[convertstrid(1003933)]' (**arg(4, 1003933))
play sfx2 "other_7004.ogg"
get_char('c6541') '[convertstrid(1003934)]' (**arg(5, 1003934))
get_char('c6553') '[convertstrid(1003935)]' (**arg(6, 1003935))
get_char('c6541') '[convertstrid(1003936)]' (**arg(7, 1003936))
get_char('c6541') '[convertstrid(1003937)]' (**arg(8, 1003937))
get_char('c6541') '[convertstrid(1003938)]' (**arg(9, 1003938))
get_char('c6553') '[convertstrid(1003939)]' (**arg(10, 1003939))
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c31') '[convertstrid(1003940)]' (**arg(11, 1003940))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1123026)]' (**arg(12, 1123026))
hide p3
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003941)]' (**arg(13, 1003941))
hide p4
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003942)]' (**arg(14, 1003942))
return "avg20073"