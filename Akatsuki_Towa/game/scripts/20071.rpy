label avg20071(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_019
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1003905)]' (**arg(1, 1003905))
hide p1
get_char('c0') '[convertstrid(1003906)]' (**arg(2, 1003906))
$ update_portrait('oc004_01 2', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(1003907)]' (**arg(3, 1003907))
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
get_char('c6523') '[convertstrid(1003908)]' (**arg(4, 1003908))
get_char('c6523') '[convertstrid(1003909)]' (**arg(5, 1003909))
get_char('c6523') '[convertstrid(1003910)]' (**arg(6, 1003910))
hide p4
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1003911)]' (**arg(7, 1003911))
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003912)]' (**arg(8, 1003912))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c6533') '[convertstrid(1003913)]' (**arg(9, 1003913))
get_char('c6533') '[convertstrid(1003914)]' (**arg(10, 1003914))
get_char('c6533') '[convertstrid(1003915)]' (**arg(11, 1003915))
get_char('c6533') '[convertstrid(1003916)]' (**arg(12, 1003916))
get_char('c6523') '[convertstrid(1003917)]' (**arg(13, 1003917))
get_char('c6533') '[convertstrid(1003918)]' (**arg(14, 1003918))
hide p2
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003919)]' (**arg(15, 1003919))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003920)]' (**arg(16, 1003920))
return "avg20071"