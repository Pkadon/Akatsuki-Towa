label avg12676(trans=fade_in):

$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1166914)]' (**arg(1, 1166914))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166915)]' (**arg(2, 1166915))
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166916)]' (**arg(3, 1166916))
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166917)]' (**arg(4, 1166917))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166918)]' (**arg(5, 1166918))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1166919)]' (**arg(6, 1166919))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166920)]' (**arg(7, 1166920))
stop music
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1166921)]' (**arg(8, 1166921))
$ play_music("ed7511.ogg")
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166922)]' (**arg(9, 1166922))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7080.ogg"
get_char('c31') '[convertstrid(1166923)]' (**arg(10, 1166923))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
play sfx2 "other_7079.ogg"
get_char('c43') '[convertstrid(1166924)]' (**arg(11, 1166924))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6019.ogg"
get_char('c21') '[convertstrid(1166925)]' (**arg(12, 1166925))
hide p4
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1166926)]' (**arg(13, 1166926))
return "avg12676"