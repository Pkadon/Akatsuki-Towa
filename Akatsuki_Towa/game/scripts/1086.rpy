label avg1086(trans=fade_in):

$ play_music("ed7202.ogg")
scene avg_bg_079
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
play sfxvoice "avg_vocal_li02.ogg"
get_char('c41') '[convertstrid(2101872)]' (**arg(1, 2101872))
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101873)]' (**arg(2, 2101873))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 23', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(2101874)]' (**arg(3, 2101874))
$ update_portrait('oc004_01 23', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101875)]' (**arg(4, 2101875))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101876)]' (**arg(5, 2101876))
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
get_char('c13') '[convertstrid(2101877)]' (**arg(6, 2101877))
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101878)]' (**arg(7, 2101878))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101879)]' (**arg(8, 2101879))
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101880)]' (**arg(9, 2101880))
$ update_portrait('oc004_01 10', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101881)]' (**arg(10, 2101881))
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101882)]' (**arg(11, 2101882))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101883)]' (**arg(12, 2101883))
hide p4
hide p1
get_char('c0') '[convertstrid(2101884)]' (**arg(13, 2101884))
$ update_portrait('oc001_01 1', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(2101885)]' (**arg(14, 2101885))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(2101886)]' (**arg(15, 2101886))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2101887)]' (**arg(16, 2101887))
return "avg1086"