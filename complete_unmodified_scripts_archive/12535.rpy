label avg12535(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with trans
get_char('c31') '[convertstrid(1151748)]' (**arg(1, 1151748))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151749)]' (**arg(2, 1151749))
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1151750)]' (**arg(3, 1151750))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151751)]' (**arg(4, 1151751))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1151752)]' (**arg(5, 1151752))
hide p2
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151753)]' (**arg(6, 1151753))
hide p1
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151754)]' (**arg(7, 1151754))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1151755)]' (**arg(8, 1151755))
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151756)]' (**arg(9, 1151756))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1151757)]' (**arg(10, 1151757))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151758)]' (**arg(11, 1151758))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151759)]' (**arg(12, 1151759))
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151760)]' (**arg(13, 1151760))
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1151761)]' (**arg(14, 1151761))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1151762)]' (**arg(15, 1151762))
hide p4
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1151763)]' (**arg(16, 1151763))
return "avg12535"