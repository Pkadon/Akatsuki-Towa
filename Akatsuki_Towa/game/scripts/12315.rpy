label avg12315(trans=fade_in):

$ play_music("ed7305.ogg")
scene avg_bg_052
$ update_narrator('c23')
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "other_7051.ogg"
get_char('c23') '[convertstrid(1133288)]' (**arg(1, 1133288))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133289)]' (**arg(2, 1133289))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 3', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133290)]' (**arg(3, 1133290))
hide p1
$ update_portrait('oc004_01 3', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133291)]' (**arg(4, 1133291))
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133292)]' (**arg(5, 1133292))
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133293)]' (**arg(6, 1133293))
hide p3
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133294)]' (**arg(7, 1133294))
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133295)]' (**arg(8, 1133295))
hide p2
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133296)]' (**arg(9, 1133296))
$ update_portrait('oc004_01 20', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1133297)]' (**arg(10, 1133297))
hide p1
$ update_portrait('oc004_01 20', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1133298)]' (**arg(11, 1133298))
return "avg12315"