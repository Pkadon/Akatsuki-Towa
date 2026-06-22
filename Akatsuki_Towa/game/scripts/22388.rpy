label avg22388:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc002_01 11', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6024.ogg"
get_char('c23') '[convertstrid(1134047)]' (**arg(1, 1134047))
$ update_portrait('oc002_01 11', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134048)]' (**arg(2, 1134048))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1134049)]' (**arg(3, 1134049))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 20', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134050)]' (**arg(4, 1134050))
$ update_portrait('oc001_01 20', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1134051)]' (**arg(5, 1134051))
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1134052)]' (**arg(6, 1134052))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134053)]' (**arg(7, 1134053))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1134054)]' (**arg(8, 1134054))
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1134055)]' (**arg(9, 1134055))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1134056)]' (**arg(10, 1134056))
return