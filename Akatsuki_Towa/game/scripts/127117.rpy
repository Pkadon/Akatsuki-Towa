label avg127117(trans=fade_in):

$ play_music("ED6202.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1179486)]' (**arg(1, 1179486))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179487)]' (**arg(2, 1179487))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179488)]' (**arg(3, 1179488))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179489)]' (**arg(4, 1179489))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179490)]' (**arg(5, 1179490))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179491)]' (**arg(6, 1179491))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179492)]' (**arg(7, 1179492))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179493)]' (**arg(8, 1179493))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1179494)]' (**arg(9, 1179494))
$ update_portrait('st061_01 1', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179495)]' (**arg(10, 1179495))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179496)]' (**arg(11, 1179496))
hide p1304
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1179497)]' (**arg(12, 1179497))
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7080.ogg"
get_char('c13') '[convertstrid(1179498)]' (**arg(13, 1179498))
hide p1
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
play sfx2 "other_7079.ogg"
get_char('c13043') '[convertstrid(1179499)]' (**arg(14, 1179499))
$ update_portrait('st061_01 4', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1179500)]' (**arg(15, 1179500))
return "avg127117"