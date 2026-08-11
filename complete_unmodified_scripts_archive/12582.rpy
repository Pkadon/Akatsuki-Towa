label avg12582(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_080
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with trans
get_char('c31') '[convertstrid(1155411)]' (**arg(1, 1155411))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155412)]' (**arg(2, 1155412))
hide p3
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155413)]' (**arg(3, 1155413))
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155414)]' (**arg(4, 1155414))
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155415)]' (**arg(5, 1155415))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155416)]' (**arg(6, 1155416))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155417)]' (**arg(7, 1155417))
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1155418)]' (**arg(8, 1155418))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155419)]' (**arg(9, 1155419))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1155420)]' (**arg(10, 1155420))
hide p4
$ update_portrait('oc003_01 12', 'p3', [l(-6), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c31') '[convertstrid(1155421)]' (**arg(11, 1155421))
hide p1
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 10', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155422)]' (**arg(12, 1155422))
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1155423)]' (**arg(13, 1155423))
hide p4
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1155424)]' (**arg(14, 1155424))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1155425)]' (**arg(15, 1155425))
return "avg12582"