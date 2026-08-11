label avg14015(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1202324)]' (**arg(1, 1202324))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202325)]' (**arg(2, 1202325))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202326)]' (**arg(3, 1202326))
hide p2
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202327)]' (**arg(4, 1202327))
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202328)]' (**arg(5, 1202328))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202329)]' (**arg(6, 1202329))
hide p28
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
with fade
get_char('c281') '[convertstrid(1202330)]' (**arg(7, 1202330))
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202331)]' (**arg(8, 1202331))
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202332)]' (**arg(9, 1202332))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202333)]' (**arg(10, 1202333))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202334)]' (**arg(11, 1202334))
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202335)]' (**arg(12, 1202335))
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202336)]' (**arg(13, 1202336))
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202337)]' (**arg(14, 1202337))
hide p28
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202338)]' (**arg(15, 1202338))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202339)]' (**arg(16, 1202339))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202340)]' (**arg(17, 1202340))
hide p2
hide p1
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1202341)]' (**arg(18, 1202341))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202342)]' (**arg(19, 1202342))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1202343)]' (**arg(20, 1202343))
stop music
hide p2
hide p1
get_char('c0') '[convertstrid(1202344)]' (**arg(21, 1202344))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202345)]' (**arg(22, 1202345))
hide p1
$ update_narrator('c20161')
with fade
play sfx2 "other_7079.ogg"
get_char('c20161') '[convertstrid(1202346)]' (**arg(23, 1202346, size=(1.2)))
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 3', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1202347)]' (**arg(24, 1202347))
hide p1
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202348)]' (**arg(25, 1202348))
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202770)]' (**arg(26, 1202770, size=(1.2)))
$ update_portrait('sc020_01 4', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1202771)]' (**arg(27, 1202771, size=(1.2)))
hide p1
$ update_portrait('oc002_01 16', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1202772)]' (**arg(28, 1202772, size=(1.2)))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
get_char('c281') '[convertstrid(1202773)]' (**arg(29, 1202773, size=(1.2)))
return "avg14015"