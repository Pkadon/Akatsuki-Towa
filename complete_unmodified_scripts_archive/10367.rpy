label avg10367:

$ play_music("ed7100.ogg")
scene avg_bg_023
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
$ update_narrator('c2391')
window show
with fade_in
get_char('c2391') '[convertstrid(1132046)]' (**arg(1, 1132046))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132047)]' (**arg(2, 1132047))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132048)]' (**arg(3, 1132048))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132049)]' (**arg(4, 1132049))
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132050)]' (**arg(5, 1132050))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132051)]' (**arg(6, 1132051))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132052)]' (**arg(7, 1132052))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132053)]' (**arg(8, 1132053))
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1132054)]' (**arg(9, 1132054))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132055)]' (**arg(10, 1132055))
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132056)]' (**arg(11, 1132056))
hide p2
$ update_portrait('st040_01 1', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1132057)]' (**arg(12, 1132057))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
play sfx2 "other_7027.ogg"
get_char('c2391') '[convertstrid(1132058)]' (**arg(13, 1132058))
hide p1
$ update_portrait('st040_01 5', 'p239', [l(-19), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1132059)]' (**arg(14, 1132059))
hide p3
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132060)]' (**arg(15, 1132060))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132061)]' (**arg(16, 1132061))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132062)]' (**arg(17, 1132062))
$ update_portrait('st040_01 5', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132063)]' (**arg(18, 1132063))
hide p239
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132064)]' (**arg(19, 1132064))
$ update_portrait('oc002_01 18', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132067)]' (**arg(20, 1132067))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1132068)]' (**arg(21, 1132068))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1132069)]' (**arg(22, 1132069))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1132070)]' (**arg(23, 1132070))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1132071)]' (**arg(24, 1132071))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1132072)]' (**arg(25, 1132072))
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('st040_01 1', 'p239', [l(-19), light, flip], 6)
get_char('c2391') '[convertstrid(1132073)]' (**arg(26, 1132073))
return