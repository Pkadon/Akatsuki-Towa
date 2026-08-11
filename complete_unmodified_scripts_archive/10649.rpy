label avg10649(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_008
$ update_narrator('c0')
window show
with trans
play sfx2 "other_7018.ogg"
get_char('c0') '[convertstrid(1164723)]' (**arg(1, 1164723))
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164724)]' (**arg(2, 1164724))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164725)]' (**arg(3, 1164725))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164726)]' (**arg(4, 1164726))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164727)]' (**arg(5, 1164727))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164728)]' (**arg(6, 1164728))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164729)]' (**arg(7, 1164729))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1164730)]' (**arg(8, 1164730))
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1164731)]' (**arg(9, 1164731))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1164732)]' (**arg(10, 1164732))
return "avg10649"