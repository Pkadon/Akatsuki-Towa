label avg12660(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1166418)]' (**arg(1, 1166418))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
get_char('c13351') '[convertstrid(1166419)]' (**arg(2, 1166419))
hide p2
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166420)]' (**arg(3, 1166420))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1166421)]' (**arg(4, 1166421))
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166422)]' (**arg(5, 1166422))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166423)]' (**arg(6, 1166423))
hide p4
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166424)]' (**arg(7, 1166424))
get_char('c13351') '[convertstrid(1166425)]' (**arg(8, 1166425))
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1166426)]' (**arg(9, 1166426))
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
get_char('c13351') '[convertstrid(1166427)]' (**arg(10, 1166427))
get_char('c13351') '[convertstrid(1166428)]' (**arg(11, 1166428))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166429)]' (**arg(12, 1166429))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
get_char('c13351') '[convertstrid(1166430)]' (**arg(13, 1166430))
get_char('c13351') '[convertstrid(1166431)]' (**arg(14, 1166431))
hide p1
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1166432)]' (**arg(15, 1166432))
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166433)]' (**arg(16, 1166433))
hide p2
get_char('c13351') '[convertstrid(1166434)]' (**arg(17, 1166434))
get_char('c13351') '[convertstrid(1166435)]' (**arg(18, 1166435))
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1166436)]' (**arg(19, 1166436))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 23', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1166437)]' (**arg(20, 1166437))
return "avg12660"