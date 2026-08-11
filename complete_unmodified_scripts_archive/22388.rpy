label avg22388(trans=fade_in):

$ play_music("ed7201.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "fight_6024.ogg"
get_char('c23') '[convertstrid(1134047)]' (**arg(1, 1134047))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1134048)]' (**arg(2, 1134048))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1134049)]' (**arg(3, 1134049))
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1134050)]' (**arg(4, 1134050))
hide p1
$ update_portrait('oc002_01 23', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1134051)]' (**arg(5, 1134051))
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1134052)]' (**arg(6, 1134052))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1134053)]' (**arg(7, 1134053))
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1134054)]' (**arg(8, 1134054))
hide p2
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 6)
get_char('c33') '[convertstrid(1134055)]' (**arg(9, 1134055))
hide p3
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1134056)]' (**arg(10, 1134056))
return "avg22388"