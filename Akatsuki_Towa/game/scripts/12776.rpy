label avg12776:

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1175747)]' (**arg(1, 1175747))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 5', 'p1304', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c13041') '[convertstrid(1175748)]' (**arg(2, 1175748))
hide p1304
hide p1
get_char('c0') '[convertstrid(1175749)]' (**arg(3, 1175749))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175750)]' (**arg(4, 1175750))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175751)]' (**arg(5, 1175751))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175752)]' (**arg(6, 1175752))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175753)]' (**arg(7, 1175753))
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175754)]' (**arg(8, 1175754))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 2', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1175755)]' (**arg(9, 1175755))
hide p3
$ update_portrait('st061_01 2', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1175756)]' (**arg(10, 1175756))
hide p4
hide p1304
get_char('c0') '[convertstrid(1175757)]' (**arg(11, 1175757))
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1175758)]' (**arg(12, 1175758))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1175759)]' (**arg(13, 1175759))
hide p4
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1175760)]' (**arg(14, 1175760))
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1175761)]' (**arg(15, 1175761))
hide p3
hide p1
get_char('c0') '[convertstrid(1175762)]' (**arg(16, 1175762))
return