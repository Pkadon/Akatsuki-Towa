label avg12634(trans=fade_in):

$ play_music("ed7126.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7057.ogg"
get_char('c13') '[convertstrid(1162707)]' (**arg(1, 1162707))
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 3', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1162708)]' (**arg(2, 1162708))
hide p1
$ update_portrait('oc003_01 3', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st062_01 1', 'p1308', [r(-16), light], 6)
get_char('c13083') '[convertstrid(1162709)]' (**arg(3, 1162709))
hide p3
$ update_portrait('st062_01 1', 'p1308', [r(-16), dark], 5)
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1162710)]' (**arg(4, 1162710))
$ update_portrait('sc010_01 1', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('st062_01 4', 'p1308', [r(-16), light], 6)
get_char('c13083') '[convertstrid(1162711)]' (**arg(5, 1162711))
hide p18
$ update_portrait('st062_01 4', 'p1308', [r(-16), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), l_shake, light, flip], 6)
get_char('c41') '[convertstrid(1162712)]' (**arg(6, 1162712))
hide p1308
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1162713)]' (**arg(7, 1162713))
hide p4
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc010_01 5', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1162714)]' (**arg(8, 1162714))
hide p2
$ update_portrait('sc010_01 5', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('st062_01 1', 'p1308', [r(-16), light], 6)
get_char('c13083') '[convertstrid(1162715)]' (**arg(9, 1162715))
$ update_portrait('st062_01 1', 'p1308', [r(-16), dark], 5)
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1162716)]' (**arg(10, 1162716))
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1162717)]' (**arg(11, 1162717))
hide p1308
$ update_portrait('sc010_01 1', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1162718)]' (**arg(12, 1162718))
hide p2
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1162719)]' (**arg(13, 1162719))
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('sc010_01 2', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1162720)]' (**arg(14, 1162720))
$ update_portrait('sc010_01 5', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1162721)]' (**arg(15, 1162721))
hide p18
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1162722)]' (**arg(16, 1162722))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1162723)]' (**arg(17, 1162723))
hide p3
hide p1
get_char('c0') '[convertstrid(1162724)]' (**arg(18, 1162724))
get_char('c0') '[convertstrid(1162725)]' (**arg(19, 1162725))
return "avg12634"