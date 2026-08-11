label avg12735(trans=fade_in):

stop music
scene avg_bg_070
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1172745)]' (**arg(1, 1172745))
get_char('c0') '[convertstrid(1172746)]' (**arg(2, 1172746))
get_char('c0') '[convertstrid(1172747)]' (**arg(3, 1172747))
get_char('c0') '[convertstrid(1172748)]' (**arg(4, 1172748))
$ play_music("ed7150.ogg")
scene avg_bg_038
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1172749)]' (**arg(5, 1172749))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172750)]' (**arg(6, 1172750))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172751)]' (**arg(7, 1172751))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172752)]' (**arg(8, 1172752))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172753)]' (**arg(9, 1172753))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172754)]' (**arg(10, 1172754))
hide p3
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1172755)]' (**arg(11, 1172755))
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172756)]' (**arg(12, 1172756))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1172757)]' (**arg(13, 1172757))
hide p1304
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172758)]' (**arg(14, 1172758))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172759)]' (**arg(15, 1172759))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172760)]' (**arg(16, 1172760))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172761)]' (**arg(17, 1172761))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1172762)]' (**arg(18, 1172762))
hide p3
$ update_portrait('st061_01 5', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1172763)]' (**arg(19, 1172763))
$ update_portrait('st061_01 5', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1172764)]' (**arg(20, 1172764))
return "avg12735"