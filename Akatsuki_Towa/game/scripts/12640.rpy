label avg12640:

$ play_music("ed7203.ogg")
scene avg_bg_070
$ update_narrator('c13251')
window show
with fade_in
play sfx2 "fight_6027.ogg"
get_char('c13251') '[convertstrid(1162998)]' (**arg(1, 1162998))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162999)]' (**arg(2, 1162999))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1163000)]' (**arg(3, 1163000))
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1163001)]' (**arg(4, 1163001))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163002)]' (**arg(5, 1163002))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1163003)]' (**arg(6, 1163003))
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163004)]' (**arg(7, 1163004))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
get_char('c13251') '[convertstrid(1163005)]' (**arg(8, 1163005))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1163006)]' (**arg(9, 1163006))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1163007)]' (**arg(10, 1163007))
hide p1
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1163008)]' (**arg(11, 1163008))
hide p3
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
get_char('c13251') '[convertstrid(1163009)]' (**arg(12, 1163009))
return